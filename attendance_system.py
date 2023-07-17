import face_recognition
import numpy as np
import csv
from datetime import datetime
import cv2


class AttendanceSystem:
    def __init__(self, video_capture, csv_file_path):
        self.video_capture = video_capture
        self.csv_file_path = csv_file_path
        self.known_face_encodings = []
        self.known_face_names = []
        self.students = []
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.window_padding = 10
        self.running = True

    def read_csv_to_list(self):
        data_list = []
        with open(self.csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                data_list.append(row)
        return data_list

    def read_csv_column(self, column_index):
        column_data = []
        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                column_value = row[column_index]
                column_data.append(column_value)
        return column_data

    def load_known_faces(self):
        column_data_image = self.read_csv_column(4)
        self.known_face_names = self.read_csv_to_list()

        for image_path in column_data_image:
            pro_img = face_recognition.load_image_file(image_path)
            pro_encoding = face_recognition.face_encodings(pro_img)[0]
            self.known_face_encodings.append(pro_encoding)

        self.students = self.known_face_names.copy()

    def mark_attendance(self, name):
        if name in self.students:
            self.students.remove(name)
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S %p")
            with open(f"{now.strftime('%Y-%m-%d')}.csv", "a") as f:
                lnwriter = csv.writer(f)
                lnwriter.writerow([name[0], name[1], name[2], current_time])

    def process_frame(self, frame):
        frame_height, frame_width = frame.shape[:2]
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        self.face_names = []

        for face_encoding in self.face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"  # Default name set to "Unknown"
            face_distance = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            self.face_names.append(name)
            self.mark_attendance(name)

    def run(self):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")

        cv2.namedWindow("Smart Attendance system by Tarak's Team")
        f = open(f"{current_date}.csv", "w+", newline="")
        lnwriter = csv.writer(f)

        self.load_known_faces()

        while self.running:
            _, frame = self.video_capture.read()
            frame_height, frame_width = frame.shape[:2]

            self.process_frame(frame)

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4 - 2
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 50), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name[1], (left + 6, bottom - 36), font, 0.7, (255, 255, 255), 1)
                cv2.putText(frame, f"Semester:{name[2]}", (left + 6, bottom - 20), font, 0.6, (255, 255, 255), 1)
                cv2.putText(frame, f"Roll:{name[0]}", (left + 6, bottom - 4), font, 0.6, (255, 255, 255), 1)

            cv2.rectangle(frame, (self.window_padding, self.window_padding),
                          (frame_width - self.window_padding, frame_height - self.window_padding),
                          (0, 255, 0), 2)

            cv2.imshow("Smart Attendance system by Tarak's Team", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty(
                    "Smart Attendance system by Tarak's Team", cv2.WND_PROP_VISIBLE) < 1:
                self.running = False

        self.video_capture.release()
        cv2.destroyAllWindows()
        f.close()
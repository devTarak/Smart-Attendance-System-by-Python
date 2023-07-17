import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

try:
    video_capture = cv2.VideoCapture(0)

    tarak_image = face_recognition.load_image_file("photos/Tarak.JPG")
    tarak_encoding = face_recognition.face_encodings(tarak_image)[0]

    shahed_image = face_recognition.load_image_file("photos/Shahed123.png")
    shahed_encoding = face_recognition.face_encodings(shahed_image)[0]

    hanif_image = face_recognition.load_image_file("photos/Hanif.jpg")
    hanif_encoding = face_recognition.face_encodings(hanif_image)[0]

    known_face_encoding = [
        tarak_encoding,
        shahed_encoding,
        hanif_encoding,
    ]

    known_faces_names = [
        ["Tarak Rahman", "3", "676961"],
        ["Shahed Bin Amin", "3", "689214"],
        ["Md. Abu Hanif", "3", "689264"],
    ]

    students = known_faces_names.copy()

    face_locations = []
    face_encodings = []
    face_names = []
    s = True

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    f = open(current_date + ".csv", "w+", newline="")
    lnwriter = csv.writer(f)

    window_padding = 10  # Padding size in pixels

    # Initialize a flag variable to track program status
    running = True

    while running:
        _, frame = video_capture.read()
        frame_height, frame_width = frame.shape[:2]

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                name = ""
                face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
                best_match_index = np.argmin(face_distance)

                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]

                face_names.append(name)

                if name in known_faces_names:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottomLeftCornerOfText = (10, 30)
                    fontScale = 0.8
                    fontColor = (200, 180, 3)
                    thickness = 1
                    lineType = 2

                    if name in students:
                        students.remove(name)
                        current_time = now.strftime("%I:%M:%S %p")
                        lnwriter.writerow([name[0], name[1], name[2], current_time])

                    # Add a background rectangle
                    # Add a background rectangle
                    # Add a background rectangle
                    textSize, _ = cv2.getTextSize(name[0] + " Present", font, fontScale, thickness)
                    backgroundPadding = 15
                    margin_top = -15  # Adjust the top margin value as needed
                    margin_left = -2  # Adjust the left margin value as needed

                    backgroundRectangle = (
                        bottomLeftCornerOfText[0] - margin_left, bottomLeftCornerOfText[1] - textSize[1] - backgroundPadding - margin_top,
                        textSize[0] + 2 * backgroundPadding + margin_left, textSize[1] + 2 * backgroundPadding + margin_top)
                    cv2.rectangle(frame, backgroundRectangle, fontColor, cv2.FILLED)

                    # Add the text
                    textPosition = (bottomLeftCornerOfText[0] - margin_left, bottomLeftCornerOfText[1] - backgroundPadding - margin_top)
                    cv2.putText(frame, name[0] + " Present", textPosition, font, fontScale, (255, 255, 255), thickness, lineType)

        # Draw face detection boxes
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled down
            top *= 4 - 2
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name, semester, and roll number below the face
            cv2.rectangle(frame, (left, bottom - 50), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name[0], (left + 6, bottom - 36), font, 0.7, (255, 255, 255), 1)
            cv2.putText(frame, f"Semester:{name[1]}", (left + 6, bottom - 20), font, 0.6, (255, 255, 255), 1)
            cv2.putText(frame, f"Roll:{name[2]}", (left + 6, bottom - 4), font, 0.6, (255, 255, 255), 1)

        # Add a rectangle around the frame
        cv2.rectangle(frame, (window_padding, window_padding),
                      (frame_width - window_padding, frame_height - window_padding), (0, 255, 0), 2)

        cv2.imshow("Smart Attendance system by Tarak's Team", frame)

        # Check for the 'q' key or window close event
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Smart Attendance system by Tarak's Team", cv2.WND_PROP_VISIBLE) < 1:
            running = False

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

except Exception as e:
    print(e)

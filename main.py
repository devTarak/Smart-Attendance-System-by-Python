import cv2
from attendance_system import AttendanceSystem

if __name__ == '__main__':
    video_capture = cv2.VideoCapture(0)
    file_path = 'student-list.csv'
    attendance_system = AttendanceSystem(video_capture, file_path)
    attendance_system.run()

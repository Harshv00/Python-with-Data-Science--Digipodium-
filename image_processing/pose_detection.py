import cv2
import mediapipe as np

np_drawing = np.solutions.drawing_utils
np_drawing_styles = np.solutions.drawing_styles
np_pose = np.solutions.pose

camera = cv2.VideoCapture(0)
with np_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while camera.isOpened():
        success, image = camera.read()
        if not success: continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        results = pose.process(image)

        np_drawing.draw_landmarks(image, results.pose_landmarks, np_pose.POSE_CONNECTIONS, landmark_drawing_spec=np_drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('MediaPipe Pose Demo', image)
        if cv2.waitKey(5) == 27: break
cv2.destroyAllWindows()
camera.release()

        
"""
Configuration globale du projet Smart Door Lock.
"""

FACE_DISTANCE_THRESHOLD = 0.55
LOCK_OPEN_DURATION_SECONDS = 3.0
GPIO_LOCK_PIN = 17

KNOWN_FACES_DIR = "data/known_faces"
ATTENDANCE_FILE_PATH = "data/attendance.csv"

ALLOWED_IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")
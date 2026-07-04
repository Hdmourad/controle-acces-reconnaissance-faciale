def create_opencv_camera_capture(camera_index: int = 0, video_capture_factory=None):
    """
    Crée une capture caméra OpenCV.

    camera_index = 0 correspond généralement à la webcam principale.

    video_capture_factory est injectable pour faciliter les tests unitaires.
    En utilisation réelle, on utilise cv2.VideoCapture.
    """
    if video_capture_factory is None:
        import cv2

        video_capture_factory = cv2.VideoCapture

    return video_capture_factory(camera_index)
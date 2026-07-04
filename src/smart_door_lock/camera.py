class CameraReadError(RuntimeError):
    """
    Erreur levée lorsque la caméra ne retourne pas d'image valide.
    """


class CameraService:
    """
    Service de lecture caméra.

    Ce service reçoit un objet compatible avec OpenCV.
    Exemple réel :
    cv2.VideoCapture(0)
    """

    def __init__(self, camera_capture):
        self.camera_capture = camera_capture

    def read_frame(self):
        """
        Lit une image depuis la caméra.
        """
        success, frame = self.camera_capture.read()

        if not success or frame is None:
            raise CameraReadError("Impossible de lire une image depuis la caméra.")

        return frame

    def release(self) -> None:
        """
        Libère la caméra.
        """
        self.camera_capture.release()
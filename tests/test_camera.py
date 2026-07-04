import pytest

from smart_door_lock.camera import CameraReadError, CameraService


class FakeCameraCapture:
    def __init__(self, success=True, frame="fake-frame"):
        self.success = success
        self.frame = frame
        self.released = False

    def read(self):
        return self.success, self.frame

    def release(self):
        self.released = True


def test_read_frame_returns_frame_when_camera_successful():
    camera_capture = FakeCameraCapture(success=True, frame="frame-1")
    camera_service = CameraService(camera_capture)

    frame = camera_service.read_frame()

    assert frame == "frame-1"


def test_read_frame_raises_error_when_camera_fails():
    camera_capture = FakeCameraCapture(success=False, frame=None)
    camera_service = CameraService(camera_capture)

    with pytest.raises(CameraReadError):
        camera_service.read_frame()


def test_release_releases_camera_capture():
    camera_capture = FakeCameraCapture()
    camera_service = CameraService(camera_capture)

    camera_service.release()

    assert camera_capture.released is True
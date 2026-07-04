from smart_door_lock.opencv_camera import create_opencv_camera_capture


class FakeVideoCapture:
    def __init__(self, camera_index):
        self.camera_index = camera_index


def test_create_opencv_camera_capture_uses_default_camera_index():
    capture = create_opencv_camera_capture(video_capture_factory=FakeVideoCapture)

    assert capture.camera_index == 0


def test_create_opencv_camera_capture_uses_custom_camera_index():
    capture = create_opencv_camera_capture(
        camera_index=1,
        video_capture_factory=FakeVideoCapture,
    )

    assert capture.camera_index == 1
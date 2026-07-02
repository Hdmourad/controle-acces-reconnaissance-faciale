from smart_door_lock.lock_control import LockController


class FakeGPIO:
    def __init__(self):
        self.actions = []

    def on(self):
        self.actions.append("on")

    def off(self):
        self.actions.append("off")


def test_open_lock_activates_then_deactivates_gpio():
    fake_gpio = FakeGPIO()
    lock = LockController(fake_gpio)

    lock.open_lock(duration=0)

    assert fake_gpio.actions == ["on", "off"]
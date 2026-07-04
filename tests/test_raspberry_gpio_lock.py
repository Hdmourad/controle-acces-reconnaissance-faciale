from smart_door_lock.raspberry_gpio_lock import create_raspberry_pi_lock_controller


class FakeOutputDevice:
    def __init__(self, pin):
        self.pin = pin
        self.actions = []

    def on(self):
        self.actions.append("on")

    def off(self):
        self.actions.append("off")


def test_create_raspberry_pi_lock_controller_uses_default_gpio_pin():
    controller = create_raspberry_pi_lock_controller(
        output_device_factory=FakeOutputDevice,
    )

    assert controller.gpio_output.pin == 17


def test_raspberry_pi_lock_controller_can_open_lock():
    controller = create_raspberry_pi_lock_controller(
        gpio_pin=22,
        output_device_factory=FakeOutputDevice,
    )

    controller.open_lock(duration=0)

    assert controller.gpio_output.pin == 22
    assert controller.gpio_output.actions == ["on", "off"]
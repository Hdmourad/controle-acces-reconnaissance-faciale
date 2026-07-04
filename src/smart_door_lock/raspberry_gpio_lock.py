from smart_door_lock.config import GPIO_LOCK_PIN
from smart_door_lock.lock_control import LockController


def create_raspberry_pi_lock_controller(
    gpio_pin: int = GPIO_LOCK_PIN,
    output_device_factory=None,
):
    """
    Crée un contrôleur de serrure pour Raspberry Pi.

    En réel :
    GPIO17 -> résistance -> Gate MOSFET -> serrure 12 V
    """
    if output_device_factory is None:
        from gpiozero import OutputDevice

        output_device_factory = OutputDevice

    gpio_output = output_device_factory(gpio_pin)
    return LockController(gpio_output)
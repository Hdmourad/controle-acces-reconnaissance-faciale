from time import sleep


class LockController:
    """
    Contrôle l'ouverture de la serrure via une sortie GPIO.

    Dans le montage réel :
    GPIO17 Raspberry Pi -> résistance -> Gate MOSFET
    MOSFET -> commande la serrure électrique 12 V
    """

    def __init__(self, gpio_output):
        self.gpio_output = gpio_output

    def open_lock(self, duration: float = 3.0) -> None:
        """
        Active la serrure pendant une durée donnée puis la désactive.
        """
        self.gpio_output.on()
        sleep(duration)
        self.gpio_output.off()
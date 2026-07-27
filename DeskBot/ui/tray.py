"""
DeskBot System Tray Module

Handles background tray functionality.
"""


class Tray:

    def __init__(self, config):
        self.config = config
        self.running = False


    def start(self):
        """
        Start tray service.
        """

        self.running = True

        print("DeskBot tray started.")


    def stop(self):
        """
        Stop tray service.
        """

        self.running = False

        print("DeskBot tray stopped.")


    def status(self):
        """
        Return current tray status.
        """

        return {
            "running": self.running
        }
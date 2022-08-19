from random import randint, random
from time import sleep
from threading import Thread


def get_random_delay():
    """
    Just return radom value from 0 to 2.
    Represents seconds of delay.
    """
    # return random() * randint(1, 2)
    return 2

def get_random_countdown():
    """Just return integer in range 1 <= N <= 5."""
    return 6
    # return randint(3, 7)


class Rocket:
    """
    This class is responsible for running rockets.
    Every rocket has its own delay and countdown.
    """

    def __init__(self, name) -> None:
        self.delay = get_random_delay()
        self.countdown = get_random_countdown()
        self.name = name

    def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            print(f"{i}...")
            sleep(1)

    def _delay(self):
        print(f"🕐 Delay for {self.delay} seconds...")
        sleep(self.delay)

    def run(self):
        # Do the countdown before start the rocket
        print(f"\nPrepare the {self.name} ✅")
        self._countdown()

        # Check the delay
        self._delay()

        # Show success message
        print(f"🚀 Rocket go to the moon...{self.name}")


def main():
    r1 = Rocket(name="Rocket 1")
    r2 = Rocket(name="Rocket 2")
    r3 = Rocket(name="Rocket 3")

    rock1 = Thread(target=r1.run)
    rock2 = Thread(target=r2.run)
    rock3 = Thread(target=r3.run)
    rock1.start()
    rock2.start()
    rock3.start()


if __name__ == "__main__":
    main()

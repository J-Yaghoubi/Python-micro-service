import time

from rabbit import QueuePublisher
from simulator import Co2Sensor, CoSensor, VocSensor


def run():
    """
    Generate and send sensors data to Queue every 3 second
    """
    try:
        QueuePublisher().publish(Co2Sensor.generate())
        QueuePublisher().publish(CoSensor.generate())
        QueuePublisher().publish(VocSensor.generate())
        time.sleep(3)
        run()

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    run()

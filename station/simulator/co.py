import random
from datetime import datetime


class CoSensor:
    """
    Carbon Monoxide (CO) Sensor simulator
    """

    value = round(random.uniform(1, 1000), 2)

    @classmethod
    def generate(cls):
        cls.value = max(
            0,
            min(
                round(random.uniform(cls.value - 20, cls.value + 20), 2),
                1000,
            ),
        )

        return {
            'sensor_id': 'GKI-802',
            'gas_type': 'C0',
            'value': cls.value,
            'timestamp': "{:.6f}".format(datetime.now().timestamp()),
        }

import random
from datetime import datetime


class VocSensor:
    """
    Volatile organic compound (VOC) Sensor simulator
    """

    value = round(random.uniform(1, 100), 2)

    @classmethod
    def generate(cls):
        cls.value = max(
            0,
            min(
                round(random.uniform(cls.value - 5, cls.value + 5), 2),
                100,
            ),
        )

        return {
            'sensor_id': 'YUA-200',
            'gas_type': 'VOC',
            'value': cls.value,
            'timestamp': "{:.6f}".format(datetime.now().timestamp()),
        }

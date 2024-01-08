import json

import pika


class QueuePublisher:
    """
    A class to publish given data to Queue through RabbitMq
    """

    connection_params = pika.ConnectionParameters('localhost')
    queue_name = 'sensors_data'

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue_name)

    def publish(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=json.dumps(message),
        )

        print(f"Sent to RabbitMQ: {message}")
        self.close()

    def close(self) -> None:
        self.connection.close()

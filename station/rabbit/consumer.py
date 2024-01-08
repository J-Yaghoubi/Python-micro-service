import pika


class QueueConsumer:
    """
    A class to consume data from Queue through RabbitMq
    """

    connection_params = pika.ConnectionParameters('localhost')
    queue_name = 'sensors_data'

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue_name)

    def consume(self) -> bytes | None:
        method_frame, _, body = self.channel.basic_get(queue=self.queue_name)

        if method_frame:
            self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            print("Received message:", body)
        else:
            print("No message available")

        return body

import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost','1234', '/', credentials)
#parameters = pika.ConnectionParameters('rabbitmq','5672', '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


message = {
    "video_fid": '6558f277fff850d756e33ccf',
    "mp3_fid": '6558f277fff850d756e33cc2',
    "username": 'georgio@email.com',
}


channel.basic_publish(
    exchange="",
    routing_key="mp3",
    body=json.dumps(message),
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ),
)

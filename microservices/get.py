import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq','5672', '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel2 = connection.channel()

def callback_vid(ch, method, properties, body):
    print('From vid')
    #ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body)

def callback_mp3(ch, method, properties, body):
    print('From mp3')
    #ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body)

channel.basic_consume(
            queue='video', on_message_callback=callback_vid
            )
channel2.basic_consume(
            queue='mp3', on_message_callback=callback_mp3
            )

print("Waiting for messages. To exit press CTRL+C")

channel.start_consuming()
channel2.start_consuming()

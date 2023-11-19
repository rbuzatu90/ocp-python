print('test ok')
import pika, sys, os, time
from send import email


def main():
    # rabbitmq connection
    print("Started Notification")
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    def callback(ch, method, properties, body):
        err = email.notification(body)
        if err:
          print('nack')
        #    ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
          print('ack')
        #    ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue='mp3', on_message_callback=callback
        #queue=os.environ.get("MP3_QUEUE"), on_message_callback=callback
    )

    print("Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()

print('dlol')
if __name__ == "__main__":
    print("Waiting for messages. from mai n")
    main()
#    try:
#        main()
#    except KeyboardInterrupt:
#        print("Interrupted")
#        try:
#            sys.exit(0)
#        except SystemExit:
#            os._exit(0)

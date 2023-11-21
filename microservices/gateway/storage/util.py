import pika, json
import time


def upload(f, fs, channel, access):
    time.sleep(1)
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        return "internal server error 1", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except (pika.exceptions.StreamLostError, pika.exceptions.AMQPHeartbeatTimeout):
        print("exception StreamLostError")
        fs.delete(fid)
        upload(f, fs, channel, access)
    except (pika.exceptions.ChannelWrongStateError):
        print("exception ChannelWrongStateError")

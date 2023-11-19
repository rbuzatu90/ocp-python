import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor


def start(message, fs_videos, fs_mp3s, channel):
    print("########################################################################### 5")
    message = json.loads(message)

    # empty temp file
    tf = tempfile.NamedTemporaryFile()
    # video contents
    out = fs_videos.get(ObjectId(message["video_fid"]))
    print("########################################################################### 5.1", out)
    # add video contents to empty file
    tf.write(out.read())
    # create audio from temp video file
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()
    print("########################################################################### 6", audio)

    # write audio to the file
    tf_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"
    audio.write_audiofile(tf_path)
    print("########################################################################### 6.1", str(tf_path))

    # save file to mongo
    f = open(tf_path, "rb")
    print("########################################################################### 6.2", tf_path)
    data = f.read()
    fid = fs_mp3s.put(data)
    print("########################################################################### 6.3", fid)
    f.close()
    os.remove(tf_path)

    message["mp3_fid"] = str(fid)
    print("########################################################################### 7")
    print(message)
    try:
        channel.basic_publish(
            exchange="",
            routing_key="mp3",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        fs_mp3s.delete(fid)
        return "failed to publish message"
    print("########################################################################### 8")

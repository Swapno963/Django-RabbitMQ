import pika
import json

def publish_message(message):
    params = pika.URLParameters('amqps://ydaqwhaq:o88LdMvVVd-0FJpmA0JxMC2bPYKBu_SG@dingo.rmq.cloudamqp.com/ydaqwhaq')
    connection = pika.BlockingConnection(params)    
    channel = connection.channel()
    channel.queue_declare("my_queue")
    data = {
        "email":"swapnom73@gamil.com",
        "message":"hi this is a message"
    }
    channel.basic_publish(exchange="",
                          routing_key="my_queue",
                          body=json.dumps(data),
                          )

    channel.close()

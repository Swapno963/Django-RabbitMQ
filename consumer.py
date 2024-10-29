import pika
import json
def email_sender(message):
    messages = json.loads(message)
    email = messages.get('email')
    message = messages.get('message')
    print("email and message from email_sender: ",email,message)


def callback(ch,method,properties,body):
    # print(ch,method,properties,body)
    print("body from callback:", body)
    message = body.decode()
    email_sender(message)    
    
    
    
    
params = pika.URLParameters('amqps://ydaqwhaq:o88LdMvVVd-0FJpmA0JxMC2bPYKBu_SG@dingo.rmq.cloudamqp.com/ydaqwhaq')
connection = pika.BlockingConnection(params)    
channel = connection.channel()
channel.queue_declare("my_queue")
channel.basic_consume(queue="my_queue",
                    on_message_callback=callback,
                    auto_ack=True
                    )
print("worked")
channel.start_consuming()

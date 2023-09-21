import pika

params = pika.URLParameters("amqps://rqcrzgvu:Tl0IOB_ajOW8leP0s-7xdc-9M6E0yLGd@porpoise.rmq.cloudamqp.com/rqcrzgvu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
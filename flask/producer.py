import pika, json

params = pika.URLParameters("amqps://rqcrzgvu:Tl0IOB_ajOW8leP0s-7xdc-9M6E0yLGd@porpoise.rmq.cloudamqp.com/rqcrzgvu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
import pika, json

params = pika.URLParameters("amqps://lciwlelw:Le62_s1GjgyHGlKChiTo7JvLwu_TmiHf@jackal.rmq.cloudamqp.com/lciwlelw")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
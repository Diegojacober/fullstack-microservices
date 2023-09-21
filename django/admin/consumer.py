import pika

params = pika.URLParameters("amqps://rqcrzgvu:Tl0IOB_ajOW8leP0s-7xdc-9M6E0yLGd@porpoise.rmq.cloudamqp.com/rqcrzgvu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

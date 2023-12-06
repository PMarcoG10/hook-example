#!/usr/bin/env python
import pika

# establish a connection to RabbitMQ server
# this insures that we are connected to a broker on our local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# in order to send a message we must make sure that a recipeint queue exists
channel.queue_declare(queue="hello")

# this contains a string which well be sent to our 'hello' queue
# the excahnge helps us to specify exacty which queue the message will be sent to
# our queue name has be specofied in the 'routing_key' parameter
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

# helps us with the network buffers being flushed
# and our messages was successfully sent
connection.close()

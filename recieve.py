#!/usr/bin/env python
import pika, sys, os


def main():
    # connecting to the RabbbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # making sure that the queue exists
    channel.queue_declare(queue="hello")

    # when receiving a messgae this function is called by the Pika library
    # this will also print the contents of the message on the terminal
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # this function lets RabbitMQ should receive messages from our 'hello' queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    # a never ending loop that waits for data and runs callbacks whenever necessary 
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

# catches 'keyboardInterrupts during program shutdown' 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

import logging
import socket


__author__ = "Ejie Emmanuel Ebuka"

# TCP

"""
Transmission Control Protocol (TCP) defines how to establish and maintain a network
conversation through which application programs can exchange data.
TCP works with the internet protocol (IP), which defines how computers
send packets of data to each other. It uses a 3 way handshake
c > syn
s > syn/ack
c > ack

server - listens for incoming connections via TCP
client - connects to the server via TCP
network - A network consists of two or more computers that are linked together
IP - The number that represents the machine on the network (IP4 vs IP6)
port - A communication end point
protocol - Defined means of application communication

"""

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# TCP client
def client(server, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f'Connecting... {server} : {port}')
    sock.connect(address)
    logging.info('Connected!')
    logging.info('Send')
    sock.send(b'Hello\r\n')
    logging.info("Recieve")
    data = sock.recv(1024)
    logging.info('Closing...')
    sock.close()
    logging.info(f'Data: {data}')


def main():
    client("youtube.com", 81)

if __name__ == "__main__":
    main()


# TCP server
def server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    logging.info(f"Bind {ip} : {port}")
    sock.bind(address)
    logging.info("Listening...")
    sock.listen(1)
    conn, addr = sock.accept()
    logging.info(f"Connecting... {addr}")
    while True:
        data = conn.recv(1024)
        if len(data) == 0:
            logging.info("Exiting...")
            conn.close()
            break
        logging.info(f'Data: {data}')
    logging.info('Closing the server')
    sock.close()

def main():
    server("localhost", 8181)

if __name__ == "__main__":
    main()

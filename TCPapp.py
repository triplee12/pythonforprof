import logging
import socket
import select
import multiprocessing


__author__ = "Ejie Emmanuel Ebuka"

# TCP application
# Make a TCP server in a multi-process that executes multiple clients request

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Server
def server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f"Binding {ip} : {port}")
    address = ((ip, port))
    sock.bind(address)
    sock.setblocking(False)
    sock.listen(200)
    logging.info(f"Listening o {ip} : {port}")
    reader = [sock]
    while True:
        readable, writable, errors = select.select(reader, [], [], 0.5)
        for s in readable:
            try:
                if s == sock:
                    client, addr = s.accept()
                    client.setblocking(False)
                    reader.append(client)
                    logging.info(f"Connection: {addr}")
                else:
                    data = s.recv(1024)
                    if data:
                        logging.info(f"Echo: {data}")
                        s.send(data)
                    else:
                        logging.info(f"Remove: {s}")
                        s.close()
                        reader.remove()
            except Exception as e:
                logging.warning(e.args)
            finally:
                logging.info(f"Connection terminated!")

def main():
    sv = multiprocessing.Process(target=server, args=["localhost", 8181], daemon=True, name="server")
    while True:
        commands = input('Enter a command (start or stop) ')
        if commands == "start":
            logging.info('Starting the server')
            sv.start()
        if commands == "stop":
            logging.info('Stopping the server')
            sv.terminate()
            sv.join()
            sv.close()
            logging.info('Server stopped')
            break
    logging.info('TCP Application finished!')

if __name__ == "__main__":
    main()

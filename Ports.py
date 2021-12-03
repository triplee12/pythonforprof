import logging
import socket


__author__ = "Ejie Emmanuel Ebuka"

# Determine / scan port availability
# Find out if a port is already in use

"""
google - google is your friend; how to find ports in use (OS)
sudo lsof -i -P -n
sudo lsof -i -P  -n | grep LISTEN
"""
logging.basicConfig(format="%(levelname)s - %(asctime)s - %(message)s", datefmt='%H:%M:%S', level=logging.DEBUG)

# Check ports
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip} : {port}')
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        conn = sock.connect_ex((ip, port))
        logging.debug(f'Returning {ip} : {port} = {conn}')
        sock.close()
        if conn == 0:
            ret = False
            logging.debug(f'{ip} : {port} is in use')
        else:
            ret = True
            logging.debug(f'{ip} : {port} is not in use')
    except Exception as e:
        ret = False
        logging.debug(f'Error {ip} : {port} = {e.msg}')
    finally:
        logging.debug(f'Returning {ip} : {port} = {ret}')
        return ret

# Ckeck port range
def check_range(ip, scope):
    ret = {}
    for s in scope:
        r = check_port(ip, s, 5.0)
        ret[s] = r
    return ret


def main():
    p = check_port('127.0.0.1', 100, 3.0)
    logging.info(f"Port 100 usable {p}")

    # Range ports
    ports = check_range('127.0.0.1', range(10, 8181))
    for k, v in ports.items():
        logging.info(f"Port {k} usable {v}")

if __name__ == "__main__":
    main()

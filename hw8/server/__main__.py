import yaml
import socket
import logging
import select
from argparse import ArgumentParser
import json
import threading
from resolvers import resolve
from protocol import validate_request,make_response
from handlers import handle_tcp_request
#from echo.controllers import echo_controller

def read(sock, connections, requests, buffersize):
    try:
        bytes_request = sock.recv(buffersize)
    except Exception:
        connections.remove(sock)
    else:
        requests.append(bytes_request)

def write (sock, connection, resoponse):
    try:
        sock.send(resoponse)
    except Exception:
        connections.remove(sock)

config = {
    'host': '127.0.0.1',
    'port': 8000,
    'buffersize': 1024
}


parser = ArgumentParser()


parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)


args = parser.parse_args()


if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s-%(levelname)s-%(message)s',
    handlers = (
        logging.FileHandler('server.log'),
        logging.StreamHandler()

    )
)
requests= []

connections = []

host, port = config.get('host'), config.get('port')

try:
    
    sock = socket.socket()
    sock.bind((host, port))
    sock.settimeout(0)
    sock.setblocking(False)
    sock.listen(5)

    logging.info(f'Server started with {host}:{port}')

    while True:
        try:    
            client, address = sock.accept()
            client_host, client_port = address
            logging.info(f'Client was detected {client_host}:{client_port}')
            connections.append(client)
        except:
            pass

        if connections:
            rlist, wlist, xlist = select.select (connections, connections, connections, 0)

            for read_client in rlist:
                read_thread=threading.Thread(target=read,daemon = True, args = (
                    read_client, connections, requests, config.get('buffersize')))
                # bytes_request = read_client.recv(config.get('buffersize'))
                # requests.append(bytes_request)
                read_thread.start()
            if requests:
                bytes_request = requests.pop()
                bytes_response = handle_tcp_request(bytes_request)

                for write_client in wlist:      
                    write_thread = threading.Thread(target=write,daemon = True, args=(
                        write_client, connections, bytes_response
                        ))
                    # write_client.send(bytes_response)
                    write_thread.start()

except KeyboardInterrupt:
    
    logging.info('Server shutdown')
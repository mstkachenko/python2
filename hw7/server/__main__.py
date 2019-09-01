import yaml
import socket
import logging
import select
from argparse import ArgumentParser
import json
from resolvers import resolve
from protocol import validate_request,make_response
from handlers import handle_tcp_request
#from echo.controllers import echo_controller


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

        if connections !=[]:
            rlist, wlist, xlist = select.select (connections, connections, connections, 0)

            for read_client in rlist:
                bytes_request = read_client.recv(config.get('buffersize'))
                requests.append(bytes_request)

            if requests:
                bytes_requests = requests.pop()
                bytes_response = handle_tcp_request(bytes_request)

                for write_client in wlist:      
                    write_client.send(bytes_response)

except KeyboardInterrupt:
    
    logging.info('Server shutdown')
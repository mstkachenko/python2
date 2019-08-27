import yaml
import socket
import logging
from argparse import ArgumentParser
import json
from resolvers import resolve
from protocol import validate_request,make_response
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


# logger = logging.getLogger('server')

# formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
# file_handler = logging.FileHandler('server.log')
# stream_handler=logging.StreamHandler()

# logger.setLevel(logging.DEBUG)
# file_handler.setLevel(logging.DEBUG)
# stream_handler.setLevel(logging.DEBUG)

# file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)



host, port = config.get('host'), config.get('port')

try:
    
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    logging.info(f'Server started with {host}:{port}')

    while True:
        
        client, address = sock.accept()
        client_host, client_port = address
        logging.info(f'Client was detected {client_host}:{client_port}')

        
        bytes_request = client.recv(config.get('buffersize'))
        
       
        request=json.loads(
            bytes_request.decode()
        )
        

        if validate_request(request):             
            action = request.get('action')
            controller = resolve(action)
            if controller:
                try:
                    response=controller(request)
                    logging.debug(f'Client {host}:{port} send request {request}')
                except Exception as err:
                    response = response = make_response(
                    request,500, f'Internal server error'
                    )
                    logging.critical(f'Exception - {err}')

            else: 
                response = response = make_response(
                request,404, f'Action {action} is not supported'
                )
                logging.error(f'Client {host}:{port} call action with name {action}')
        else:
            response = (
                request,400, 'Wrong request'
            )
            logging.error(f'Client {host}:{port} send wrong request {request}')
        
        string_response = json.dumps(response)

        client.send(string_response.encode())

        client.close()
except KeyboardInterrupt:
    
    logging.info('Server shutdown')
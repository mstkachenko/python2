import yaml
import socket
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

host, port = config.get('host'), config.get('port')



try:
    
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    print(f'Server started with {host}:{port}')

    while True:
        
        client, address = sock.accept()
        client_host, client_port = address
        print(f'Client was detected {client_host}:{client_port}')

        
        bytes_request = client.recv(config.get('buffersize'))
        
       
        request=json.loads(
            bytes_request.decode()
        )
        

        if validate_request(request):             
            action = request.get('action')
            controller = resolve(action)
            if controller:
                try:
                    response = controller(request)
                    print(f'Client {host}:{port} send request {request}')
                except Exception as err:
                    response = (
                    request,500, f'Internal server error'
                    )
                    print(f'Exception - {err}')

            else: 
                response = (
                request,404, f'Action {action} is not supported'
                )
                print(f'Client {host}:{port} call action with name {action}')
        else:
            response = (
                request,400, 'Wrong request'
            )
            print(f'Client {host}:{port} send wrong request {request}')
        
        string_response = json.dumps(response)

        client.send(string_response.encode())

        client.close()
except KeyboardInterrupt:
    
    print('Server shutdown')
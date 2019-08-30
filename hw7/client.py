import yaml
import socket
import zlib
import hashlib
from argparse import ArgumentParser
import json
from datetime import datetime

READ_MODE = 'read'
WRITE_MODE = 'write'




def make_request(action,data,token=None):
    return{
        'action':action,
        'data':data,
        'time':datetime.now().timestamp(),
        'token':token
    }


config={
    'host':'127.0.0.1',
    'port':8000,
    'buffersize': 1024
}

parser = ArgumentParser()

parser.add_argument(
    '-c','--config',type=str, required=False,
    help = 'Sets config file path'
)

parser.add_argument(
    '-ht','--host',type=str, required=False,
    help = 'Sets server host'
)

parser.add_argument(
    '-p','--port',type=int, required=False,
    help = 'Sets server port'
)

parser.add_argument(
    '-m','--mode',type=str, default=READ_MODE,
    help = 'Sets client mode'
)

args = parser.parse_args()

if args.config:
    with open (args.config) as file:
        file_config = yaml.safe_load(file)
      #  config.update(file_config or {})
    
#if args.host:
#    config['host'] = args.host
    config['host'] = args.host

if args.port:
#    config['port'] = args.port
    config['port'] = args.port


if __name__ == '__main__':
    try:
        sock=socket.socket()
        sock.connect((config.get('host'),config.get('port')))
 
        print ('Client was started')
        while True:
            
            if args.mode == WRITE_MODE:

                action = input('Enter action: ')
                data = input('Enter data: ')
                
                hash_obj = hashlib.sha256()
                hash_obj.update(
                    str(datetime.now().timestamp()).encode()
                )

                request = make_request(action,data,hash_obj.hexdigest())

                string_request=json.dumps(request)

                bytes_request = zlib.compress(string_request.encode())

                sock.send(bytes_request)
                print('Client send data')
            
            else:
                compressed_response = sock.recv(config.get('buffersize'))
                print(compressed_response)
                bytes_response = zlib.decompress(compressed_response)
                print(bytes_response.decode())


    except KeyboardInterrupt:

        sock.close()
        print('Client shutdown')
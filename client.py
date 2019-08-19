# import yaml
import sys
import socket
from argparse import ArgumentParser

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

args = parser.parse_args()

if args.config:
    #with open (args.config) as file:
     #   file_config = yaml.safe_load(file)
      #  config.update(file_config or {})
    
#if args.host:
#    config['host'] = args.host
    config['host'] = args.host

#if args.port:
#    config['port'] = args.port
    config['port'] = args.port


if __name__ == '__main__':
    try:
        sock=socket.socket()
        sock.connect((config.get('host'),config.get('port')))
        # if args.config:
        #     with open (args.config) as file:
        #         file_config = yaml.safe_load(file)
        #         config.update(file_config or {})
        
        # if args.host:
        #     config['host'] = args.host

        # if args.port:
        #     config['port'] = args.port
        # (2-й способ)
        # if 'config' in sys.argv:
        #     config_name = sys.argv[2]
        #     with open(config_name) as file:
        #         file_config = yaml.safe_load(file)
        #         config.update(file_config or {})
        # print(config.get('host'), config.get('port'))

    # print(config)
        print ('Client was started')

        data = input('Enter data: ')

        sock.send(data.encode())
        print('Client send data')
        bytes_response = sock.recv(config.get('buffersize'))
        print(bytes_response.decode())
        sock.close()
    except KeyboardInterrupt:
        # client.close()
        sock.close()
        print('Client shutdown')
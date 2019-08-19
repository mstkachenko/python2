import socket
if __name__=='__main__':
    try:    
        sock=socket.socket()
        sock.bind(('localhost', 8000))              
        sock.listen(5)


        print(f'Server started with localhost:8000')

        while True:
            client, address = sock.accept()
            client_host,client_port = address
            print(f'Client was detected {client_host}:{client_port}')

            bytes_request = client.recv(1024)

            print(f'Client send message {bytes_request.decode()}')
        
            client.send(bytes_request)
            client.close()
    except KeyboardInterrupt:
        # client.close()
        # sock.close()
        print('Server shutdown')
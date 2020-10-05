import socket
import json

class Server_chain:

    def __init__(self):

        self.socket = socket.socket()
        self.socket.bind(('89.223.122.217', 2048))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.bufer_size = 0
        self.json_data = 0

    def main(self):

        try:
            while 1 == 1:
                    self.connection, self.address = self.socket.accept()

                    self.bufer_size = self.connection.recv(8).decode('utf-8')

                    if self.bufer_size.isdigit():
                        pass
                    else:
                        self.connection.close()
                        continue

                    data_recieve = self.connection.recv(int(self.bufer_size)).decode('utf-8')

                    data_recieve = json.loads(data_recieve)

                    request_data = data_recieve[0]
                    self.json_data = data_recieve[1]


                    if request_data == 'download':
                        self.get_data()
                    elif request_data == 'items':
                        self.get_items()
                    elif request_data == 'update':
                        self.update_data()

        except Exception as ex:
            print(ex)
        finally:
            self.socket.close()
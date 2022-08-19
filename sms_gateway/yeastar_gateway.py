import socket
from time import sleep
from datetime import datetime
from random import randint


class Yeastar:
    """
    Configuration for Yeastar tg800 GSM 8-port gateway
    connect_to_yeastar  -> connection to Yeastar gateway
    send_command        -> sending text commands to gateway
    send_sms            -> sending sms message from Yeastar gateway to specified phone_number using sim_port
    generate_id         -> generates random id
    """
    BUFFER_SIZE = 1024
    LoggedIn = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host: str, port: int, username: str, secret: str):
        self.host = host
        self.port = port
        self.username = username
        self.secret = secret

    def connect_to_yeastar(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        data = self.s.recv(self.BUFFER_SIZE)
        if data.decode().__contains__("Asterisk"):
            data = self.send_command(f"Action: login\r\nUsername: {self.username}\r\nSecret: {self.secret}\r\n\r\n".encode(), 3)
            if data.decode().__contains__("Success"):
                self.LoggedIn = True
            if data.decode().__contains__('Error'):
                self.s.close()

    def send_command(self, message: bytes, timeout: int):
        self.s.send(message)
        data = self.s.recv(self.BUFFER_SIZE)
        sleep(timeout)
        return data

    def close_command(self):
        self.s.close()
        sleep(5)

    def send_sms(self, sim_port: int, phone_number: str, message: str):
        self.send_command(
            message=f'Action: smscommand\r\ncommand: gsm send sms {sim_port+1} {phone_number} "{message}" {generate_id}\r\n\r\n'.encode(),
            timeout=6
        )


def generate_id():
    now = datetime.now()
    dt_string = now.strftime('%Y%m%d%H%M%S')
    return (dt_string + randint(1, 10000).__str__()).__str__()

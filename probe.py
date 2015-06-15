from time import sleep

__author__ = 'soroosh'

import click
import socket


def connect(hostname, port):
    sock = socket.socket()
    sock.connect((hostname, int(port)))


def try_connect(hostname, port, retries=10, time_interval=1):
    for i in range(0, retries):
        try:
            connect(hostname, port)
            return
        except:
            sleep(time_interval)
            pass

    raise Exception("Could not connect to {0}:{1} after {2} retries".format(hostname, port, retries))


if __name__ == "__main__":
    try_connect('localhost', 9042)
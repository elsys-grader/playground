import xmlrpc.client
import os

rpc = xmlrpc.client.ServerProxy('http://172.17.0.1:' + os.environ['PORT'])
token = os.environ['AUTH']


def start_container():
    rpc.start_container(token)


def exec_step(command):
    return rpc.exec_step(token, command)

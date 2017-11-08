import xmlrpc.client

rpc = xmlrpc.client.ServerProxy('http://172.17.0.1:8000')


def exec_command(command):
    key = "BLABLA"
    rpc.exec_command(key, command)

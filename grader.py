import xmlrpc.client

rpc = xmlrpc.client.ServerProxy('http://172.17.0.1:9000')


def start_container():
    rpc.start_container()


def exec_step(command):
    return rpc.exec_step(command)

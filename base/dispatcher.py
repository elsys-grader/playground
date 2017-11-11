import threading
from .docker import docker_container_create, docker_container_exec
from xmlrpc.server import SimpleXMLRPCServer
import os


class Dispatcher(threading.Thread):
    def __init__(self, docker_image, input_file):
        threading.Thread.__init__(self)
        self.server = SimpleXMLRPCServer(('0.0.0.0', 9000), allow_none=True)
        self.server.register_instance(self)
        self.docker_image = docker_image
        self.input_file = input_file

    def run(self):
        self.server.serve_forever()

    def start_container(self):
        input_file_host_path = os.path.abspath(self.input_file)
        self.input_file_container_path = '/grader/testing/input.file'

        self.container = docker_container_create(
            self.docker_image, ['sleep', 'infinity'],
            crippled=True)
        self.container.start()

    def stop(self):
        self.server.shutdown()

    def exec_step(self, command):
        return docker_container_exec(self.container, command)

from xmlrpc.server import SimpleXMLRPCServer
from base.docker import docker_image_build
from base.runners import GradingRunner, TestingRunner
from multiprocessing import Process
import time


def listen():
    server = SimpleXMLRPCServer(('0.0.0.0', 8000), allow_none=True)
    server.register_function(exec_command, 'exec_command')
    server.serve_forever()


def exec_command(key, command):
    print("test", key, command)
    return 5


if __name__ == '__main__':
    grading_image = docker_image_build("teacher", "Dockerfile.grading", ".")
    testing_image = docker_image_build("student", "Dockerfile.testing", ".")
    test_file_path = "cat.c"
    p = Process(target=listen)
    p.start()

    with GradingRunner(grading_image) as grading_runner, \
            TestingRunner(testing_image, test_file_path) as testing_runner:
        time.sleep(5)

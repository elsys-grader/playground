from xmlrpc.server import SimpleXMLRPCServer
from base.docker import docker_image_build
from base.dispatcher import Dispatcher
from base.docker import docker_container_create
from base.docker import docker_container_exec
from base.docker import docker_container_run
import time


if __name__ == '__main__':
    grading_image = docker_image_build("teacher", "Dockerfile.grading", ".")
    testing_image = docker_image_build("student", "Dockerfile.testing", ".")
    test_file_path = "cat.c"
    disp = Dispatcher(testing_image, test_file_path)
    disp.start()

    time.sleep(1)

    container = docker_container_run(grading_image, ['python', 'task.py'], crippled=False)
    print(container)

    disp.stop()

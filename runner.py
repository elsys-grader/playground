from base.dispatcher import Dispatcher
import time
import sys
import argparse
from base.utils import wait_for_port
DEBUG_AUTH_TOKEN = '12345'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', help='port to listen on', default=0, type=int)
    parser.add_argument('image', help='image to use')
    parser.add_argument('input', help='input file to use')
    args = vars(parser.parse_args())

    disp = Dispatcher(args['image'], args['input'])
    disp.start()

    wait_for_port('localhost', disp.server.server_address[1])
    print("Running at: {}".format(disp.server.server_address))

import time
import socket


def wait_for_port(host, port, timeout=2):
    start = time.time()
    end = start + timeout

    while True:
        try:
            s = socket.create_connection((host, port), timeout)
            s.close()
            return True
        except socket.error:
            pass

        time.sleep(.1)
        if time.time() > end:
            return False

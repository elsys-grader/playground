import grader
import time


if __name__ == '__main__':
    grader.start_container()
    rc, stdout, _, _ = grader.exec_step("echo a")
    print("return code: {} stdout: {}".format(rc, stdout))

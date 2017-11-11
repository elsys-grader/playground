import grader
import time

time.sleep(50)
grader.start_container()
print(grader.exec_step("echo a"))
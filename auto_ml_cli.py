from testing import testing_module
import time


class the_end:
    def __init__(self):
        start = time.time()
        test = testing_module()
        over = test.testing_user_input()
        end = time.time()
        print("------%s seconds------ " % (round(end - start, 2)))


proj = the_end()

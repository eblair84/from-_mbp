import os
import sys
import inspect
import traceback

def log(msg,what = inspect.currentframe().f_back):
    # print('{} and pid of {}'.format(msg, what_called))
    # print(what_called)
    # what_called = traceback.print_stack()
    print('About to print what')
    previous_frame = inspect.currentframe().f_back
    (filename, line_number, 
     function_name, lines, index) = inspect.getframeinfo(previous_frame)
    print(filename)
    # print(what)
    # for item in inspect.currentframe():
      #   print(type(item))
    # print(inspect.stack())

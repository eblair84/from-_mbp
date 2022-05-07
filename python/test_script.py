import utils
import sys
import inspect
import time

def write_hello(msg):
    print( msg)

def main():
    
    while True:
        print('Going to check function output')
        # write_hello('Hello')

        utils.log('what is this')
        # print(inspect.getsourcefile(sys._getframe(1)))
        time.sleep(1)

if __name__ == "__main__":
    main()

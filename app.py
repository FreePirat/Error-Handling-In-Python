import time

startTime = time.time()
try:
    time.sleep(0.5)
    1/0
except ZeroDivisionError:
    print('There was a 0 division error')
except Exception as e:
    print(e)
finally:
    print(f'This took {time.time() - startTime} to execute')

print(4)

def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a 0 division error!')
        except Exception:
            print('There was some sort of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()

class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError function')

# causeError()

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'

def raiseServerError():
    raise ServerError()

# raiseServerError()
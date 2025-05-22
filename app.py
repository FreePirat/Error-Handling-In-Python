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
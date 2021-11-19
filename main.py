import time

def speed_calc_decorator(function):
  def wrapper_function():
    start = time.time()
    function()
    end = time.time()
    diff = end-start
    print(f"{function.__name__} took {diff} seconds to run")
  return wrapper_function


# example functions to make a comparison between

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()

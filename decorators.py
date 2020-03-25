from functools import wraps

# timer
import time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        
        print(f'Function {func.__name__!r} elapsed {run_time:.4f} sec')
        return result
    return wrapper

@timer
def squares(num_times):
    for _ in range(num_times):
        return sum([n**3 for n in range(10000)])


print(squares(3))


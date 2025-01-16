import time
from . import matching

def measure_matching_speed(text, pattern):
    start_time = time.perf_counter()
    
    position = matching(text, pattern)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    formatted_elapsed_time = "{:.10f}".format(elapsed_time)

    return position, formatted_elapsed_time
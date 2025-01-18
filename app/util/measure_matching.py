import time
from .. import kmp, boyer_more

def measure_matching_speed(text, pattern, mode='boyer_more'):
    start_time = time.perf_counter()
    
    if mode == boyer_more:
        position = boyer_more(text, pattern)
    else:
        position = kmp(text, pattern)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    formatted_elapsed_time = '{:.10f}'.format(elapsed_time)

    return position, formatted_elapsed_time
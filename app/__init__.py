'''matching string (boyer_more)'''
# from .matching.boyer_more import boyer_more as matching
from .matching.kmp import kmp as matching

from .measure_matching import measure_matching_speed as matching_speed

'''function'''
from .search_pattern import search_pattern
from .describe import describe
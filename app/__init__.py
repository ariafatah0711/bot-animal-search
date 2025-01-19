'''util'''
from .util.argument import getArgument  
from .util.print_text import print_text

'''matching string (boyer_more)'''
from .matching.boyer_more import boyer_more
from .matching.kmp import kmp

from .util.measure_matching import measure_matching_speed as matching_speed

'''function'''
from .search_pattern import search_pattern, search_pattern_with
from .describe import describe
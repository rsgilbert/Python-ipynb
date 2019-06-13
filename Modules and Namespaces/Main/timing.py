# timing.py

# description / __doc__
"""
Returns the average running time of a function
"""

from time import perf_counter
from collections import namedtuple

import argparse # allows us to pick arguments from the commandline

Timing = namedtuple('Timing', ['repeats', 'avg_time'])

                    
def timeit(code, repeats=5):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    avg_time = (perf_counter() - start) / repeats
    return Timing(repeats, avg_time)


if __name__ == '__main__': # the code below will only run if you are calling timing.py directly, not importing it
    
    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help="Python code to be timed")
    parser.add_argument('-r', '--repeats', type=int, default=5, help="Number of repeats")
    args = parser.parse_args()
    print(f'timing: {args.code}..')
    time_taken = timeit(code=str(args.code), repeats=args.repeats)
    print(time_taken)
     
     
# there are python modules and packages that provide the commandline functionality forexample zipfile
# you can run this from the commandline to zip files: 
    #python -m zipfile -c main.zip mod.py run.py timing.py

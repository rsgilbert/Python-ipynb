 
# run.py

import timing

code = '[x ** 0.1 for x in range(1000)]'

result_tuple = timing.timeit(code, 10)
print(result_tuple)


result_tuple2 = timing.timeit(code, 5)
print(result_tuple2)

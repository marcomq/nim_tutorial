
from time import perf_counter
import nimporter
import nmath  # Nim imports!

print('Measuring Nim...')
start_py = perf_counter()
for i in range(0, 40):
    print(nmath.fib(i))
end_py = perf_counter()

print('---------')
print('Nim      Elapsed: {:.2f}'.format(end_py - start_py))
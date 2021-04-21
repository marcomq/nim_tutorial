
from time import perf_counter
import pmath


print('Measuring Python...')
start_py = perf_counter()
for i in range(0, 40):
    print(pmath.fib(i))
end_py = perf_counter()

print('---------')
print('Python Elapsed: {:.2f}'.format(end_py - start_py))
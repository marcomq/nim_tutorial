
import times
import nmath


echo "Measuring Nim..."
let startMeasure =  cpuTime()
for i in 0 ..< 40:
    echo nmath.fib(i)
let endMeasure = cpuTime()

echo "---------"
echo "Time   Elapsed: ", endMeasure - startMeasure 
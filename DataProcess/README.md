# Algorithm to recognise the breath pattern from Oculus controller using in UE5

## My current strategy is:

$$ AverageSignal(i) - AverageSignal(i-10) > 0.15 $$
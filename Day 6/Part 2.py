import math
import numpy as np

input = """
Time:        48     98     90     83
Distance:   390   1103   1112   1360"""

times = ["".join(input.split("\n")[1].split(":")[1].split())]
dists = ["".join(input.split("\n")[2].split(":")[1].split())]

races = tuple(zip(times, dists))
ans = []

for race in races:
    time = int(race[0])
    dist = int(race[1])
    begin = 1
    end = time

    measures = []
    for x in range(begin, end):
        if ((x * 1) * (time - x)) > dist:
            measures.append("W")
    ans.append(len(measures))
print(np.prod(ans))

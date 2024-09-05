import sys
import numpy as np
from collections import defaultdict

capacity = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        wh_capacity, num_req_fill = line.split(',')
        
        if wh_capacity == 'Small':
            wh_capacity = 0
        elif wh_capacity == 'Mid':
            wh_capacity = 1
        else:
            wh_capacity = 2
        
        num_req_fill = int(num_req_fill)
    
    except ValueError:
        continue

    capacity[wh_capacity].append(num_req_fill)

wh_capacities = np.array(list(capacity.keys()))
avg_fill = np.array([np.mean(val) for val in capacity.values()])

corr = np.corrcoef(wh_capacities, avg_fill)
print("Correlation is:", corr[1, 0])


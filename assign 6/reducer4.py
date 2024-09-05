import sys

curr_storage = None
curr_sum = 0
curr_count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        storage, product = line.split(',')
        product = int(product)
    except ValueError:
        continue

    if storage != curr_storage:
        if curr_storage is not None:
            print(f"Storage Issue - {curr_storage}, product trasported : {curr_sum / curr_count:.2f}")
        
        curr_storage = storage
        curr_sum = product
        curr_count = 1
    else:
        curr_sum += product
        curr_count += 1

if curr_storage is not None:
    print(f"Storage Issue - {curr_storage}, product trasported : {curr_sum / curr_count:.2f}")


import sys

curr_transport = None
curr_sum = 0
curr_count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        transport, product = line.split(',')
        product = int(product)
    except ValueError:
        continue

    if transport != curr_transport:
        if curr_transport is not None:
            print(f"Transport Issue - {curr_transport}, product trasported : {curr_sum / curr_count:.2f}")
        
        curr_transport = transport
        curr_sum = product
        curr_count = 1
    else:
        curr_sum += product
        curr_count += 1

if curr_transport is not None:
    print(f"Transport Issue - {curr_transport}, product trasported : {curr_sum / curr_count:.2f}")


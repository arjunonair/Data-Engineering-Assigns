"""mapper2.py"""
import sys

for line in sys.stdin:
    
    lines = line.split(',')
    wh_capacity = lines[3].strip()
    num_req_fill = lines[6].strip()

    print(f"{wh_capacity},{num_req_fill}")

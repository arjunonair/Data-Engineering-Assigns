"""mapper3.py"""
import sys

for line in sys.stdin:

	lines = line.strip().split(',')
	product = lines[-1]
	transport = lines[7]
	try :
		if int(transport) > 0 :
			transport = 'Yes'
		else:
			transport = 'No'
	except:
		continue
	
	print(f"{transport},{product}")
	

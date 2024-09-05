"""mapper4.py"""
import sys

for line in sys.stdin:

	lines = line.strip().split(',')
	product = lines[-1]
	storage = lines[-6]
	
	try :
		if int(storage) > 0 :
			storage = 'Yes'
		else:
			storage = 'No'
	except:
		continue

	print(f"{storage},{product}")

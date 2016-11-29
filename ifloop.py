# printing range
# range prints total number of value and not till that value
for i in range(5):
	print(i)

print("printing specific range")	
for i in range(5,10):
	print(i)
	
print("printing negative value")	
for i in range(-5,0):
	print(i)

print("printing with some proper increment. Below will print from 0-10 with difference of 3 between them as 0,3,6,9")
for i in range(0,10,3):
	print(i)
	
	
x=["raghu",["padma","bhuvan","ruthu"],"autodesk","singapore"]
for i in range(len(x)):
	"""if len(i) > 1:
		for t in range(len(x[i])):
			print("printing inner index")
			print(t,x[i,t])"""
	#if:
	print(i,x[i]+" with length "+len(x[i]))
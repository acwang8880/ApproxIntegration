import math

# math.pi
# math.e

def setPartitions(start, end, x):
	partitions = []
	diffx = (end - start) / x
	for n in range(x+1):

		partitions.append(start)
		start = start + diffx

	print("These are the partitions: ", partitions, "\n")

	return (partitions, diffx)
	

def trapezoid(partsAndDiffX):
	partitions = partsAndDiffX[0]
	diffx = partsAndDiffX[1]
	print("Trapezoid: \n")
	solution = f(partitions[0]) + f(partitions[len(partitions)-1])
	for x in partitions[1:len(partitions)-1]:
		# print(f(x))
		solution += 2*f(x)


	return diffx/2*solution

def midpoint(partsAndDiffX):
	partitions = partsAndDiffX[0]
	diffx = partsAndDiffX[1]
	solution = 0
	mid = 0
	print("midpoint: \n")
	for x in range(len(partitions)-1):
		mid = (1/2)*(partitions[x] + partitions[x+1])
		solution += f(mid)

	return diffx * solution

def simpsons(partsAndDiffX):
	partitions = partsAndDiffX[0]
	diffx = partsAndDiffX[1]
	solution = f(partitions[0]) + f(partitions[len(partitions)-1])
	for x in partitions[1:len(partitions)-1:2]:
		solution += 4*f(x)
	for x in partitions[2:len(partitions)-1:2]:
		solution += 2*f(x)

	return diffx/3*solution

def f(x):
	return (1/x)

print(simpsons(setPartitions(1, 2, 10)))
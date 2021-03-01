import random
from matplotlib import pyplot as plt
def getResults(digits, size):
	accuracy = 10 ** digits
	normal = []
	reroll = []

	#create normal and rerolled random sets
	i = 0
	while i < accuracy:
		normal.append(random.randint(1,size))
		reroll.append(random.randint(1,size))
		if(reroll[-1] < size//2+1):
			del reroll[-1]
			reroll.append(random.randint(0,size))
		i += 1
	return normal, reroll, accuracy

def calculatePercentage(normal, reroll, accuracy):
	#calculate normal set average
	amount = 0
	for n in normal:
		amount += n
	finalNormal = amount/accuracy

	#calculate rerolled set average
	amount = 0
	for n in reroll:
		amount += n
	finalReroll = amount/accuracy

	return round((finalReroll/finalNormal)*100-100, 2)


def calculateAll():
	percentages = []
	digits = 7
	i = 1
	loops = 50
	while i < loops:
		print(f"Calculating for {i}...")
		normal,reroll,accuracy = getResults(digits,i)
		perc = calculatePercentage(normal,reroll,accuracy)
		#percentages.append((i,perc))
		percentages.append(perc)
		i += 1
	plt.plot(percentages)
	plt.suptitle('Percentage increase of dice roll if you reroll low numbers')
	plt.ylabel('Percentage increase')
	plt.xlabel('Number of sides')
	plt.savefig(f'{digits}digits{loops}dice.png')

print("Starting calculations.")
calculateAll()	

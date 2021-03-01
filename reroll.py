import random
digits = input("Digits of accuracy (more = slower, more accurate. Default:6): ")
if digits.isdigit():
	if int(digits) < 1 or int(digits) > 9:
		digits = 6
else:
	digits = 6
digits = int(digits)
accuracy = 10 ** digits
size = ""
while size.isdigit() == False or int(size) < 1:
	size = input("Size of sample:")
size = int(size)
print("Calculating results...")
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

#display results
print(f"\nAfter {accuracy} number of tests, here are the results:")
print("No reroll: ", finalNormal)
print("With reroll: ", finalReroll)

percentage = round((finalReroll/finalNormal)*100-100, 2)
print(f"Percent imrovement: {percentage}%")


import json
import random

num = 5
lis = []
lis0 = []
words = json.load(open('1000-words.json'))

for i in words:
    lis.append(i)

for i in range (0,num):
    lis0.append(random.choice(lis).capitalize() + random.choice(lis).capitalize() + str(random.randrange(0,9999)))

json.dump(lis0,open('generatedResults.json', "w+"))

print('Generated ' + str(num) + ' Results')

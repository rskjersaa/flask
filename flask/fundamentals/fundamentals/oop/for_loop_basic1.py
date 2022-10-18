# basic
for i in range(0, 151):
    print(i)

#multiples of five
for i in range (5, 1000, 5):
    print(i)

#counting the Dojo way
for i in range(1, 101):
    
    if i%5==0 and i%10==0:
        print("Coding Dojo")
        continue
    elif i%5==0:
        print('coding')
        continue
    print(i)

#countdown by fours
for i in range(2018, 0, -4):
    print(i)

#more whoa that sucker is huge fail

total = 0

for i in range(1, i +1, 2):
    total +=i
    print(total)

#whoa that sucker is huge fail
total = 0
for i in range(1, i+1):
    total += i * (i % 2)
    print(total)

#Whoa that sucker is huge success!



total_odds = sum(range(1, 500001,2))
print(total_odds)

#flexible counter
for i in range(1, 45):
    if i%3==0:
        print(i)
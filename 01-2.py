with open('01b.txt') as fin:
    contents = [line.strip() for line in fin]

sum1 = []
sum2 = []

for line in contents:
    pieces = line.split()
    sum1.append(int(pieces[0]))
    sum2.append(int(pieces[1]))

sim = 0
for num in sum1:
    if num not in sum2:
        continue
    sim += num * sum2.count(num)

print(sim)
with open('01b.txt') as fin:
    contents = [line.strip() for line in fin]

sum1 = []
sum2 = []

for line in contents:
    pieces = line.split()
    sum1.append(int(pieces[0]))
    sum2.append(int(pieces[1]))

sum1.sort()
sum2.sort()
diff = 0
for idx, num in enumerate(sum1):
    diff += abs(num - sum2[idx])

print(diff)
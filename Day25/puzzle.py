input = [13316116,13651422]

sn = 1
loop_size=0
while sn != input[0]:
    sn *= 7
    sn %= 20201227
    loop_size += 1

sn = 1
for _ in range(loop_size):
    sn *= input[1]
    sn %= 20201227
    
print('Puzzle 1: ', sn)

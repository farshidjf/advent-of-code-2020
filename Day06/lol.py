groups = open('./Day6/large_input').read().strip().split('\n\n')
print(sum(len(set(g.replace('\n', ''))) for g in groups))
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))
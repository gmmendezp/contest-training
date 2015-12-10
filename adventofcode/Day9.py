from itertools import permutations
def solve():
    dist = [[0 for j in range(3)] for i in range(3)]
    index = {}
    x = 0
    for line in fin:
        s = line.rstrip().split(' ')
        if not s[0] in index:
            index[s[0]] = x
            x += 1
        if not s[2] in index:
            index[s[2]] = x
            x += 1
        dist[index[s[0]]][index[s[2]]] = int(s[4])
        dist[index[s[2]]][index[s[0]]] = int(s[4])
    print(min([sum([dist[p[a+1]][p[a]] for a in range(len(p)-1)]) for p in permutations(range(len(dist)))]))
    print(max([sum([dist[p[a+1]][p[a]] for a in range(len(p)-1)]) for p in permutations(range(len(dist)))]))


fin = open('test.in', 'r')
solve()
fin.close()

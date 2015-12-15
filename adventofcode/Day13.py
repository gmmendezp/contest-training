from itertools import permutations
def solve():
    dist = [[0 for j in range(9)] for i in range(9)]
    index = {}
    x = 0
    for line in fin:
        s = line.strip()[:-1].split(" ")
        if not s[0] in index:
            index[s[0]] = x
            x += 1
        if not s[10] in index:
            index[s[10]] = x
            x += 1
        v = int(s[3]) if s[2] == 'gain' else -int(s[3])
        dist[index[s[0]]][index[s[10]]] = int(v)
    print(max([sum([dist[p[a-1]][p[a]] + dist[p[a]][p[a-1]] for a in range(len(p))]) for p in permutations(range(len(dist)))]))

fin = open('test.in', 'r')
solve()
fin.close()



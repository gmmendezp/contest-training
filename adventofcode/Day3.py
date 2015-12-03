def solve():
    x = interface.r()
    i, j = [[0,0] for z in range(2)]
    w = 0
    a = set([(0, 0)])
    for c in x:
        if c == '>':
            i[w] += 1
        elif c == '<':
            i[w] -= 1
        elif c == 'v':
            j[w] += 1
        elif c == '^':
            j[w] -= 1
        a.add((i[w], j[w]))
        w ^= 1
    print(len(a))

class interface:
    @staticmethod
    def w(s):
        #fout.write(s + "\n")
        print(s)
    @staticmethod
    def r():
        return fin.readline().rstrip()
        #return input()

fin = open('test.in', 'r')
solve()
fin.close()

def solve():
    m = [[0 for j in range(1000)] for i in range(1000)];
    for i in range(300):
        s = interface.r().split(' ')
        if s[0] == 'turn':
            val = -1
            a = [int(i) for i in s[2].split(',')]
            b = [int(i) for i in s[4].split(',')]
            if s[1] == 'on':
                val = 1
            for i in range(a[0], b[0]+1):
                for j in range(a[1], b[1]+1):
                    m[i][j] += val
                    if m[i][j] < 0:
                        m[i][j] = 0
        else:
            a = [int(i) for i in s[1].split(',')]
            b = [int(i) for i in s[3].split(',')]
            for i in range(a[0], b[0]+1):
                for j in range(a[1], b[1]+1):
                    m[i][j] += 2
    interface.w(sum([sum(x) for x in m]))

class interface:
    @staticmethod
    def w(*s):
        #fout.write(s + "\n")
        print(*s)
    @staticmethod
    def r():
        return fin.readline().rstrip()
        #return input()

fin = open('test.in', 'r')
solve()
fin.close()

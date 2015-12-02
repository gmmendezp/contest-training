def solve():
    paper = ribbon = 0
    for i in range(1000):
        x = [int(i) for i in interface.r().split('x')]
        a = x[0] * x[1]
        b = x[0] * x[2]
        c = x[1] * x[2]
        paper += 2 * (a + b + c) + min(a,b,c)
        ribbon += 2 * (x[0] + x[1] + x[2] - max(x[0], x[1], x[2])) + x[0] * x[1] * x[2]
    interface.w(paper, ribbon)


class interface:
    @staticmethod
    def w(s):
        fout.write(s + "\n")
        #print(s)
    @staticmethod
    def r():
        return fin.readline().rstrip()
        #return input()

fin = open('test.in', 'r')
solve()
fin.close()

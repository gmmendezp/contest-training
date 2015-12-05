def solve():
    T = int(interface.r()) + 1
    f = "Case #%d: %s";
    for t in range(1,T):
        interface.w(f % (t, interface.r()))

class interface:
    @staticmethod
    def w(*s):
        fout.write(s + "\n")
        #print(*s)
    @staticmethod
    def r():
        return fin.readline().rstrip()
        #return input()

fin = open('test.in', 'r')
fout = open('test.out', 'w')
solve()
fin.close()
fout.close()

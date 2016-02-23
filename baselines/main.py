import sys

def solve():
    T = int(io.readline()) + 1
    f = "Case #{0}: {1}";
    for t in range(1,T):
        io.write(f.format(t, io.readline()))

class InOut:
    def __init__(self, inFile=True, outFile=True):
        self.fin = open('test.in', 'r') if inFile else sys.stdin
        self.fout = open('test.out', 'w') if outFile else sys.stdout
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.fin.close()
        self.fout.close()
    def write(self, *s, sep='', end='\n'):
        print(*s, sep=sep, end=end, file=self.fout)
    def readline(self):
        return self.fin.readline().rstrip()
    def read(self):
        return self.fin.read().rstrip()

with InOut(False, False) as io:
    solve()

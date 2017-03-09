import sys

class Solver:
    def solve(self, params):
        return params

class InOut:
    def __init__(self, inFile=True, outFile=True):
        self.fin = open('test.in', 'r') if inFile else sys.stdin
        self.fout = open('test.out', 'w') if outFile else sys.stdout
    def __enter__(self):
        return self
    def __exit__(self):
        self.fin.close()
        self.fout.close()
    def write(self, *s, sep='', end='\n'):
        print(*s, sep=sep, end=end, file=self.fout)
    def readline(self):
        return self.fin.readline().rstrip()
    def read(self):
        return self.fin.read().rstrip()

class Main:
    def __init__(self):
        self.io = InOut()
        self.solver = Solver()
        self.resultTemplate = 'Case #%s: %s'
    def printResult(self, result):
        self.io.write(self.resultTemplate % result)
    def readInput(self):
        return self.io.readline()
    def start(self):
        T = int(self.io.readline()) + 1
        for t in range(1,T):
            params = self.readInput()
            self.printResult((t, self.solver.solve(params)))

Main().start()

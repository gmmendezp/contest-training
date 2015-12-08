from queue import Queue

m = {}
def solve():
    temp = Queue()
    for line in fin:
        temp.put(line)
    while not temp.empty():
        line = temp.get()
        s = line.strip().split(' ')
        if s[0] == 'NOT':
            if not testKey(s[1]):
                temp.put(line)
                continue
            m[s[3]] = (~getValue(s[1])) & 0xffff
        else:
            if not testKey(s[0]):
                temp.put(line)
                continue
            if s[1] != '->':
                if not testKey(s[2]):
                    temp.put(line)
                    continue
            if s[1] == 'AND':
                m[s[4]] = (getValue(s[0]) & getValue(s[2])) & 0xffff
            elif s[1] == 'OR':
                m[s[4]] = (getValue(s[0]) | getValue(s[2])) & 0xffff
            elif s[1] == 'LSHIFT':
                m[s[4]] = (getValue(s[0]) << getValue(s[2])) & 0xffff
            elif s[1] == 'RSHIFT':
                m[s[4]] = (getValue(s[0]) >> getValue(s[2])) & 0xffff
            else:
                m[s[2]] = getValue(s[0])
    print(m['a'])

def testKey(x):
    if not x.isdigit() and x not in m:
        return False
    return True

def getValue(x):
    if x.isdigit():
        return int(x)
    return m[x]

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

m = {}
def solve():
    for line in fin:
        s = line.strip().split(' ')
        if s[0] == 'NOT':
            m[s[3]] = (~m[s[1]]) & 0xffff
        elif s[1] == 'AND':
            m[s[4]] = (m[s[0]] & m[s[2]]) & 0xffff
        elif s[1] == 'OR':
            m[s[4]] = (m[s[0]] | m[s[2]]) & 0xffff
        elif s[1] == 'LSHIFT':
            m[s[4]] = (m[s[0]] << int(s[2])) & 0xffff
        elif s[1] == 'RSHIFT':
            m[s[4]] = (m[s[0]] >> int(s[2])) & 0xffff
        elif s[0].isdigit():
            m[s[2]] = int(s[0]) & 0xffff
        else:
            m[s[2]] = m[s[0]]
    print(m['a'])

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

def solve():
    x = interface.r()
    count = minus1 = 0
    found = False
    for i in range(len(x)):
        c = x[i]
        count += 1 if c == '(' else -1;
        if count == -1 and not found:
            found = True
            minus1 = i
    interface.w(count, minus1)

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

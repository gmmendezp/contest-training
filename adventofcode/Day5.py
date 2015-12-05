def solve():
    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']
    count1 = count2 = 0
    for i in range(1000):
        s = interface.r()
        # first half
        countVowels = 0
        twice = False
        nice = True
        last = '';
        for x in s:
            if x in vowels:
                countVowels += 1
            if x == last:
                twice = True
            for f in forbidden:
                if x == f[1] and last == f[0]:
                    nice = False
            last = x
        if nice and twice and countVowels >= 3:
            count1 += 1
        # end first half
        # second half
        x = set();
        twice = False
        trio = False
        last = ''
        for i in range(len(s)-1):
            current = s[i:i+2]
            if current in x:
                twice = True
            if last != '':
                x.add(last)
            last = current
            if i < len(s) - 2:
                temp = s[i:i+3]
                if temp[0] == temp[2]:
                    trio = True
        if twice and trio:
            count2 += 1
        # end second half
    interface.w(count1, count2)


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

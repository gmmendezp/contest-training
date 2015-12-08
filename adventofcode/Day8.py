def solve():
    totalDecode = 0
    totalEncode = 0
    for line in fin:
        s = line.rstrip()
        totalDecode += decoderCount(s)
        totalEncode += encoderCount(s)
    print(totalDecode, totalEncode)

def decoderCount(s):
    total = 0
    i = 0
    while i < len(s):
        if s[i] != '\"':
            if s[i] == '\\':
                i += 1
                if s[i] == 'x':
                    total += 3
                    i += 2
                else:
                    total += 1
        else:
            total += 1
        i += 1
    return total

def encoderCount(s):
    total = 2
    for c in s:
        if c in ['\"', '\\']:
            total += 1
    return total

fin = open('test.in', 'r')
solve()
fin.close()

import re
def solve(s):
    b = False
    while not b:
        s = sum1(s)
        m = min([s.find(i) for i in ['i','o','l']], key=lambda x: x if x >= 0 else float('inf'))
        while m > -1:
            s = s[0:m+1] + (len(s)-m-1) * 'z'
            s = sum1(s)
            m = min([s.find(i) for i in ['i','o','l']], key=lambda x: x if x >= 0 else float('inf'))
        if re.findall('|'.join(['abcdefghijklmnopqrstuvwxyz'[i:i+3] for i in range(24)]), s) and len(re.findall(r'([a-z])\1', s)) > 1:
            b = True
    print(s)

def sum1(s):
    b = True
    i = -1
    while b:
        s = s[0:i] + chr(ord(s[i]) + 1) + (s[i+1:] if i < -1 else '')
        if not s[i].isalpha():
            s = s[0:i] + 'a' + (s[i+1:] if i < -1 else '')
            i -= 1
        else:
            b = False
    return s

s = 'vzbxxyzz';
solve(s)

import re, json
def solve():
    total1 = 0
    for line in fin:
        total1 += sum([int(n) for n in re.findall(r'[-\d]+', line)])
        total2 = readJSON(json.loads(line))
    print(total1, total2)

def readJSON(obj):
    total = 0
    if isinstance(obj, dict):
        for k,v in obj.items():
            if isinstance(v, int):
                total += v
            if isinstance(v, str) and v == 'red':
                return 0
            total += readJSON(v)
    elif isinstance(obj, list):
        for i in obj:
            if isinstance(i, int):
                total += i
            total += readJSON(i)
    return total

fin = open('test.in', 'r')
solve()
fin.close()



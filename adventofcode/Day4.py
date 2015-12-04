import hashlib
s = 'iwrupvqb%d'
i = 0
val = ''
while val[0:6] != '000000':
    i += 1
    val = hashlib.md5((s % i).encode('utf-8')).hexdigest()
print(val, i)

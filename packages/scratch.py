from pprint import pprint as pp


names = ['David Jones', 'Karen Smith', 'Stanley Baldwin', 'Maggie Thatcher']

s = sorted(names, key=lambda name: name.split()[-1])

for n in s:
    pp(n)


pp('{first}, {last}'.format(first='David', last='Harris'))

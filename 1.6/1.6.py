from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

######################################################
e = defaultdict(set)

e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

print(e)

######################################################
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)

print(d)

######################################################

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
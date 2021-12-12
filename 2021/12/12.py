#!/usr/bin/env python3


from collections import defaultdict


nodes = defaultdict(set)
with open('input.txt') as f:
    lines = f.read().splitlines()
    for n in lines:
        n1, n2 = n.split('-')
        nodes[n1].update([n2])
        nodes[n2].update([n1])


def filter1(visited):
    return lambda n: n[0].isupper() or (n not in visited and n[0].islower())

def filter2(visited):
    def f(n):
        if n[0].isupper(): return True
        if n == 'end': return True
        if n == 'start': return False
        # node is lower
        if n not in visited and len(n) > 1: return True
        # node is single letter
        if sum([i==n for i in visited]) < 2: return True

    return f

def go(node, nodes, visited, f):
    global res

    if node == 'end':
        #print(visited)
        #print(set(tuple(visited,)))
        res.add(tuple(visited))
        return
    nn = filter(f(visited), nodes[node])
    #print(visited, nn)
    for n in nn:
        vis = visited[:] + [n]
        go(n, nodes, vis, f)


def do_day12(nodes, filt):
    global res

    nn = nodes['start']
    for n in nn:
        visited = ['start'] + [n]
        go(n, nodes, visited, filt)
    return len(res)


def single(path):
    res = defaultdict(lambda: 0)
    small = filter(lambda n: n[0].islower(), path)
    for node in small:
        res[node] += 1
    twices = 0
    for v in res.values():
        if v == 2: twices += 1
    if twices < 2:
        return True


res = set()
print(do_day12(nodes, filter1))

res = set()
do_day12(nodes, filter2)
res = list(res)
res.sort()
res = list(filter(single, res))
#res = [','.join(i) for i in res]
#for r in res:
#    print(r)
print(len(res))

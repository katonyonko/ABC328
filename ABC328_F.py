import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
3 5
1 2 2
3 2 -3
2 1 -1
3 3 0
1 3 5
200000 1
1 1 1
5 20
4 2 125421359
2 5 -191096267
3 4 -42422908
3 5 -180492387
3 3 174861038
2 3 -82998451
3 4 -134761089
3 1 -57159320
5 2 191096267
2 4 -120557647
4 2 125421359
2 3 142216401
4 5 -96172984
3 5 -108097816
1 5 -50938496
1 2 140157771
5 4 65674908
4 3 35196193
4 4 0
3 4 188711840
"""

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
       x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x
  def size(self, x):
    return -self.parents[self.find(x)]
  def same(self, x, y):
    return self.find(x) == self.find(y)
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
  def group_count(self):
    return len(self.roots())
  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}
  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def solve(test):
  N,Q=map(int, input().split())
  dist=[None]*N
  uf=UnionFind(N)
  G=[[] for _ in range(N)]
  ans=[]
  for i in range(Q):
    a,b,d=map(int, input().split())
    a-=1; b-=1
    if uf.same(a,b):
      if (a==b and d==0) or (dist[a]!=None and dist[b]!=None and dist[a]==dist[b]+d):
        ans.append(i+1)
    else:
      ans.append(i+1)
      dq=deque()
      used=set([a,b])
      if uf.size(a)<uf.size(b):
        dq.append(a)
      else:
        dq.append(b)
      if dist[b] is None and dist[a] is None:
        dist[b]=0
        dist[a]=dist[b]+d
      elif dist[b] is None:
        dist[b]=dist[a]-d
      elif dist[a] is None:
        dist[a]=dist[b]+d
      else:
        if uf.size(a)<uf.size(b): dist[a]=dist[b]+d
        else: dist[b]=dist[a]-d
      while dq:
        x=dq.popleft()
        for y,dd in G[x]:
          if y in used: continue
          used.add(y)
          dist[y]=dist[x]+dd
          dq.append(y)
      uf.union(a,b)
      G[a].append((b,-d))
      G[b].append((a,d))
  print(*ans)

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)
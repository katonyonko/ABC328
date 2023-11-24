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
5 6 328
1 2 99
1 3 102
2 3 86
2 4 94
2 5 95
3 4 81
6 5 998244353
1 2 337361568
1 6 450343304
2 3 61477244
2 5 745383438
4 5 727360840
8 28 936294041850197
1 2 473294720906780
1 3 743030800139244
1 4 709363019414774
1 5 383643612490312
1 6 557102781022861
1 7 623179288538138
1 8 739618599410809
2 3 857687812294404
2 4 893923168139714
2 5 581822471860662
2 6 740549363586558
2 7 307226438833222
2 8 447399029952998
3 4 636318083622768
3 5 44548707643622
3 6 307262781240755
3 7 12070267388230
3 8 700247263184082
4 5 560567890325333
4 6 704726113717147
4 7 588263818615687
4 8 549007536393172
5 6 779230871080408
5 7 825982583786498
5 8 713928998174272
6 7 751331074538826
6 8 449873635430228
7 8 11298381761479
"""

def solve(test):
  N,M,K=map(int, input().split())
  edges=[]
  for i in range(M):
    u,v,w=map(int, input().split())
    edges.append((u-1,v-1,w))
  ans=10**20
  def bfs(c):
    G=[[] for _ in range(N)]
    for i in range(N-1):
      j=c[i]
      G[edges[j][0]].append(edges[j][1])
      G[edges[j][1]].append(edges[j][0])
    inf=10
    D=[inf]*len(G)
    D[0]=0
    dq=deque()
    dq.append(0)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    if max(D)==inf:
      return False
    return True
  for c in combinations(range(M),N-1):
    tmp=0
    if bfs(c)==False: continue
    for i in range(N-1):
      tmp+=edges[c[i]][2]
      tmp%=K
    ans=min(ans,tmp)
  if test==0:
    print(ans)
  else:
    return None

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
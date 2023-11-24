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
5 1
3 1 4 1 5
9 2 6 5 3
5 1000000000
3 1 4 1 5
9 2 6 5 3
22 467772225675200
814424018890229 837987908732596 281175505732576 405797525366223 319378664987871 305374284356649 519144936694626 316916938328237 590332737480143 506785561790072 945769796193819 365498597798550 5386616044591 672368930784037 478017750715806 340276460237787 176509793332130 2734777402752 677509027289850 250325127275409 260270543315523 103584313625431
720386673780641 77160494100361 540947273460639 255177791002759 969333325196025 477751866935037 369600749728569 466236682780196 343161112138696 541310338013515 42740499599240 165778332156355 618106559852784 16582487395877 591851763813728 221861304303645 982850624742022 728669467505250 337968530842725 746724490610504 61587851254728 451153536869240
"""

def solve(test):
  ans=0
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
main(1)
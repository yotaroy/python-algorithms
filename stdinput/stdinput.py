# N
N = int(input())

# N K
N, K = map(int, input().split())

# A B C
A, B, C = map(int, input().split())

# a0 a1 ... aN-1
a = [int(i) for i in input().split()]

# strstrstr
S = input()

# N
# d0
# d1
# ...
# dN-1
N = int(input())
d = [int(input()) for i in range(N)]


# N
# t1 x1 y1
# t2 x2 y2
# ...
# tN xN yN
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# N
# A1 B1 C1
# ...
# AN BN CN
N = int(input())
A = []
B = []
C = []
for i in range(N):
    a, b, c = [int(i) for i in input().split()]
    A.append(a)
    B.append(b)
    C.append(c)

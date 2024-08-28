# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)

for i in range(n):
    ch = input().strip()
    a[ch].append(i + 1)
     
for i in range(m):
    ch = input().strip()
    if ch in a:
        print(" ".join(map(str, a[ch]))) 
    else:
        print(-1)  
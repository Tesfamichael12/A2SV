# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    s = set(map(int, input().split()))
    if not a.issuperset(s): 
        print("False")
        exit()
    
print("True")
    
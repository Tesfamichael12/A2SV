# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
en = set(map(int, input().split()))
m = int(input())
fr = set(map(int, input().split()))

print(len(en.difference(fr)))

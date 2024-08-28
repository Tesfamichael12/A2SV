if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        c = input().split()
        if c[0] == "insert":
            l.insert(int(c[1]), int(c[2]))
        if c[0] == "print":
            print(l)
        if c[0] == "remove":
            l.remove(int(c[1]))
        if c[0] == "append":
            l.append(int(c[1]))
        if c[0] == "sort":
            l.sort()
        if c[0] == "pop":
            l.pop()
        if c[0] == "reverse":
            l.reverse()
        
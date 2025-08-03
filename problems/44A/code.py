s=[]
t=int(input())
for _ in range(t):
    s1 = input()
    if s1 not in s:
        s.append(s1)
print(len(s))


t = int(input())
for _ in range(t):
    n = int(input())
    ropes = [tuple(map(int, input().split())) for _ in range(n)]
    hang_heights = [a - b for a, b in ropes]
    
    hang_heights.sort(reverse=True)
 
    cuts = 0
    while hang_heights and hang_heights[0] > 0:
        hang_heights.pop(0)  
        cuts += 1
    print(cuts)

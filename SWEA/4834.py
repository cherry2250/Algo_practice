T = int(input())
for j in range(1, T + 1):
    n = int(input())
    list_a = list(map(int, str(input())))
    cnt = [0] * 10
    for i in list_a :
        cnt[i] += 1
    
    sorting = 0
    sorting_index = 0
    for i in range(1, 10):
        if sorting <= cnt[i]:
            sorting_index = i
            sorting = cnt[i]

print(f'#{j} {sorting_index} {sorting}')
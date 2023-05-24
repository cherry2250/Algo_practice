from collections import deque
from copy import deepcopy
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N=int(input())

room=[list(map(int,input().split())) for _ in range(N)]

answer=[]
for _ in range(4):
    now_socre=0
    #1 bfs
    visited=[[0]*N for _ in range(N)]
    groups=[set()]
    g_face=[[]]
    g_num=[0]
    g_now=[0]
    cnt=1
    for x in range(N):
        for y in range(N):
            if visited[x][y]==0:
                q=deque()
                q.append((x,y))
                now=room[x][y]
                visited[x][y]=cnt
                face=[]
                n_g=set()
                n_g.add((x,y))
                while q:
                    px,py=q.popleft()

                    for d in range(4):
                        nx=px+dx[d]
                        ny=py+dy[d]

                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            continue
                        if room[nx][ny]!=now:
                            face.append((nx,ny))
                            continue

                        if visited[nx][ny]!=0:
                            continue

                        visited[nx][ny]=cnt
                        q.append((nx,ny))
                        n_g.add((nx,ny))

                cnt+=1
                groups.append(n_g)
                g_num.append(len(n_g))
                g_now.append(now)
                g_face.append(face)

    for i in range(1,len(groups)):
        now_group=groups[i]
        ax,ay=0,0
        for px,py in now_group:
            ax,ay=px,py
            break
        a_num=room[ax][ay]
        a_len=len(now_group)
        f_num=[0]*len(groups)
        for fx,fy in g_face[i]:
            f_g=visited[fx][fy]
            f_num[f_g]+=1


        for k in range(i,len(f_num)):
            if f_num[k]==0:
                continue
            b_num=g_now[k]
            b_len=g_num[k]

            score=(a_len+b_len)*a_num*b_num*f_num[k]
            now_socre+=score


    answer.append(now_socre)

    mx=N//2
    my=N//2
    new_room=deepcopy(room)

    #1구역

    for x in range(mx):
        for y in range(my):
            new_room[y][my-x-1]=room[x][y]

    #2구역
    for x in range(mx):
        for y in range(my+1,N):
            new_room[y-my-1][N - x-1] = room[x][y]

    #3구역
    for x in range(mx+1,N):
        for y in range(my):
            new_room[mx+1+y][N - x-1] = room[x][y]
    #4구역
    for x in range(mx+1,N):
        for y in range(my+1,N):
            new_room[N-my+y-N//2-1][N+mx-x] = room[x][y]

    #가운데 돌려주기
    #가운데 1
    for y in range(my):
        new_room[N-1-y][my]=room[mx][y]
    #가운데 2
    for x in range(N-1,mx,-1):
        new_room[mx][x]=room[x][my]
    #가운데 3
    for y in range(N-1,my,-1):
        new_room[N-1-y][my]=room[mx][y]
    #가운데 4
    for x in range(mx):
        new_room[mx][x]=room[x][my]
    room=deepcopy(new_room)
print(sum(answer))
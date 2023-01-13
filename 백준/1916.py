from heapq import heappush, heappop
from sys import maxsize #maxsize 배웠습니다
import sys

input = sys.stdin.readline

n = int(input()) #도시의 개수
m = int(input()) #버스의 개수

graph = [[] for _ in range(n + 1)]
visited = [maxsize] * (n + 1) #방문체크

for _ in range(m):
    start, end, cost = map(int, input().split()) #출발지, 도착지, 비용
    graph[start].append((cost, end))

start, end = map(int, input().split()) #찾고자 하는 비용 경로(출발지, 도착지)


def dijkstra(x):
    heap = []
    heappush(heap, (0, x)) #시작지점 힙에 추가
    visited[x] = 0  #시작지점 0으로 초기화

    while heap:
        d, x = heappop(heap)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                heappush(heap, (nd, nx))
                visited[nx] = nd


dijkstra(start)

print(visited[end])
# 유사한 문제 : SWEA 화물도크 / #백준 1931 회의실 배정

import sys
import heapq
input = sys.stdin.readline

n = int(input())
lecture_list = [list(map(int, input().split())) for _ in range(n)]
lecture_list.sort() #회의 시작시간을 기준으로 정렬

queue = []
heapq.heappush(queue, lecture_list[0][1]) # 첫 회의의 종료시간을 큐에 넣음

for i in range(1, n):
  if lecture_list[i][0] < queue[0]: # 지금 강의 종료시간보다 다음 강의시작이 빠를때 -> 강의실을 새로 만들어야 됨
    heapq.heappush(queue, lecture_list[i][1])
  else: # 지금 강의 끝나고 다음 강의를 시작할 수 있을 때 -> 이어서 강의하기
    heapq.heappop(queue)
    heapq.heappush(queue, lecture_list[i][1])

print(len(queue))
import sys

sys.stdin = open("input.txt", "r")
T = int(input())

if T[0] < T[1] : 
    print("<")
elif T[0] == T[1]:
    print('=')
else : 
    print(">")

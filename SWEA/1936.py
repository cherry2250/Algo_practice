# 1:1 가위바위보
arr = list(map(str, input().split()))

if int(arr[0]) > int(arr[1]) :
    print('A')
elif int(arr[0]) < int(arr[1]) :
    print('B')
else : 
    False
T = int(input())
 
for i in range(T):
    strlist = input().split()
     
    if strlist[0] in strlist[1] or strlist[1] in strlist[0]:
        a = len(strlist[0])
        b = len(strlist[1])
        if a==b:
            print("#{} yes".format(i+1))
            continue
        if strlist[0]*b ==strlist[1]*a:
            print("#{} yes".format(i+1))
        else:
            print("#{} no".format(i+1))
    else:
        print("#{} no".format(i+1))
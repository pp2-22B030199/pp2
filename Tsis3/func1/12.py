def histogram(li):
    for i in li:
        i = int(i)
        for k in range(i):
            k = int(k)
            print('*',end ='')
        print()

li = input().split()
histogram(li)
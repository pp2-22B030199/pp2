l = input()
def multiply(x):
    cnt = 0
    # cnt1 = 0
    for i in x:

        if i >= "a" and i <= "z":
            cnt +=1
    #     elif i >= "A" and i <= "Z":
    #         cnt1 +=1
    # return cnt,cnt1
    return cnt

print("lower case letters:",multiply(l))

def upper(y):
    cnt1 = 0
    for i in y:
        if i >= "A" and i <= "Z":
             cnt1 +=1
    return cnt1
print("upper case letters:",upper(l))


def uniq(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1
li = input().split()
print(uniq(li))
a = [1,2,3,4,5,8,9,10]
missing_element = []
for i in range(a[0], a[-1]+1):
    if i not in a:
        missing_element.append(i)

print(missing_element)

with open('classes.xml') as f:
    s = f.readlines()

class_list = []
for item in s:
    if 'displayName' in item:
        it = item
        it = it.replace('<', ' ').replace('>', ' ').split()
        class_list += [it[1]]
print(class_list[:100])
'''for i in range(len(class_list)):
    print(i, class_list[i])'''
        



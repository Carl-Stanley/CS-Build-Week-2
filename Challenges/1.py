# 217. Contains Duplicate
#x = ['ai', 'ba', 'xx', 'ddd', 'test1', 'test2', 'xxx', 'ya', 'test'] # No dupes
x = ['ai', 'ba', 'xx', 'ddd', 'test1', 'test', 'xxx', 'ya', 'test'] # Dupes
def checkForDuplicates_1(x):
    if len(x) == len(set(x)):
        return False
    else:
        return True


y = checkForDuplicates_1(x)

if y:
    print('There are dupes')
else:
    print('No dupes found ')    
list1 = []
for _ in range(0,int(input())):
	list1.append(int(input()))
a = sorted(set(list1), reverse = True)
print('Second max is:', a[1])
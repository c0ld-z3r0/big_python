num = int(input("Enter n.o of person : "))
arr = list (n for n in range(1,num+1))
i=1
kill = []
def fusion_reactor(ivar):
	global arr
	global kill
	global i
	
	while ivar <= len(arr):
		kill.append(arr[ivar])
		ivar += 2
		if ivar >= len(arr):
			if arr[-1] == kill[-1]:
				i = 1
			elif arr[-1] != kill[-1]:
				i = 0
			break
while True :
	fusion_reactor(i)
	arr = list(set(arr).difference(set(kill)))
	arr.sort()
	if len(arr) == 1:
		print("The Last person alive is :",arr[0])
		break
	kill = []

filename = './SC_TestSet/scpe1.txt'

File = open(filename).read()
lines = File.split('\n')
arr = []
arr.append([])
i = 0
for el in lines:       
    a = el.split(' ')
    if len(a) == 3:
     	i = i + 1
     	arr.append([])
     	arr[i].append(a[1])
     	continue
    arr[i] = arr[i] + a
while '' in  arr[0]:
	 arr[0].remove('')

# weights
len_weights = arr[0][1]
len_data = arr[0][0]
weights = arr[0][2:len(arr[0])]

# Si
data = arr[1:len(arr)]
for el in data:
	 while '' in el:
	 	el.remove('')
i = 0
for feature in data:
	if len(feature) == 0:
		i = i + 1
		continue
	if int(feature[0]) != len(feature) - 1:
		if len(data[i+1]) == 1:	
			feature.append(data[i+1].pop())
	i = i + 1
while [] in  data:
	 data.remove([])

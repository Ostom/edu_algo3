
def data_to_int(data):
	arr = []
	i = 0
	for feature in data:
		arr.append([])
		for el in feature:
			arr[i].append(int(el))
		i = i + 1
	return arr

def get_data(filename):
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
	len_weights = int(arr[0][1])
	len_data = int(arr[0][0])
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
	return [data_to_int(data), weights, len_data, len_weights]

def ProcessCombinations(A,n,k):
	if k == 0:
		Process(A)
	else:
		for i in xrange(k, n):
			A[k] =i;
			ProcessCombinations(A,i-1, k-1)
def main():
	filename = './SC_TestSet/scpe1.txt'
	ret_args = get_data(filename)
	len_weights = ret_args.pop() 
	len_data = ret_args.pop() 
	weights = ret_args.pop() 
	data = ret_args.pop() 
	print len(data)
	print data
	for k in xrange(1,len_data):
		pass
main()

# global

len_weights = 0
len_data = 0
weights = []
data = []

def data_to_int(data):
	'''
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
		 '''

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
	x = 0
	while x < len(lines):
	#for x in xrange(0,len(lines) - 1):	
	#for el in lines:       
	    el = lines[x]
	    a = el.split(' ')
	    while  '' in a:
	    	a.remove('')
	    if len(a) == 1:
	     	i = i + 1
	     	arr.append([])
	     	#arr[i].append(a[0])	   
	     	boundary = int(a[0])
	     	xcounter = x
	     	counter = 0
	     	while counter < boundary:
	     		xcounter = xcounter + 1
	     		el = lines[xcounter]
	     		a = el.split(' ')
	     		while '' in a:
			    	a.remove('')
	     		#print counter
	     		arr[i] = arr[i] + a
	     		counter = counter + len(a)
	     		x = xcounter + 1
	     	print '' + str(counter) + ' ' + str(boundary)
	     	continue
	    x = x + 1 

	    
	#while '' in  arr[0]:
	#	 arr[0].remove('')
	
	print arr[1:len(arr)]

	# weights
	lens = lines[0].split(' ')
	while '' in lens:
		lens.remove('')
	len_weights = int(lens[1])
	len_data = int(lens[0])
	weights = []#arr[0][2:len(arr[0])]

	# Si
	data = arr[1:len(arr)]
	for el in data:
		 while '' in el:
		 	el.remove('')
	
	return [data_to_int(data), weights, len_data, len_weights]
def Process(A):
	global len_weights 
	global len_data 
	global weights 
	global data 
	print A
	flag = False
	for string in data:
		for el in A:
			if el not in string:
				return False
			else: 
				flag = True 
				break
	if flag:
		print "S: "
		print A
	open("res.txt",'w').write(' '.join(A))
	return flag

def ProcessCombinations(A,n,k):
	if k == 0:
		if Process(A):
			exit()
	else:
		for i in xrange(k, n):
			A[k] =i-1;
			ProcessCombinations(A,i-1, k-1)
def main():
	global len_weights 
	global len_data 
	global weights 
	global data 
	filename = './SC_TestSet/SetCover01.txt'
	#filename = './SC_TestSet/SetCover01.txt'
	
	ret_args = get_data(filename)
	len_weights = ret_args.pop() 
	len_data = ret_args.pop() 
	weights = ret_args.pop() 
	data = ret_args.pop() 
	print len(data)
	#print data
	A = [0] * len_weights
	for k in xrange(1,len_weights):
		print "K: " + str(k) + "n:" + str(len_weights)
		ProcessCombinations(A, len_weights, k)
main()
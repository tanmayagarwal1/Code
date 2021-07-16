def DecodePerm(arr):
	if not arr : raise ValueError 
	First_ele = 0 
	for i in range(1, len(arr) + 2):
		First_ele = First_ele ^ i 
	tmp = 0 
	for i in range(1, len(arr), 2):
		tmp = tmp ^ arr[i]

	# res[0] ^ tmp = First_ele => First_ele ^ tmp = res[0] 

	first = First_ele ^ tmp 
	res = [first]
	for num in arr:
		res.append(res[-1] ^ num)
	return res 

arr = [6,5,4,6]
print(DecodePerm(arr))

'''
This problem is very similar to the first problem : decode XOR array 
In this we are missing the first element of the output array as the input 
The task is to find the first element 
To do this we use the Que in the problem description : The output array is a permutation of numbers from [1 - N], N being the length of the array
Also it is told that N is always odd 

How do we find res[0]? We know the XOR of the entire output array, as it comprises the first n positive numbers: (The first for loop does this task)
In the first for loop we start from one and go all the way to length of given length of input array + 2 : NOTE : ge go till len(given_arr) + 2 because if the length of the 
- input array is 'n', the length of the output (Decoded) array will be N =  n + 1 (refer to the first version of this problem), and as the output array also 
includes N as an element, we need to incliude N as a part of the XOR. So we go from 1 - n + 2 (n + 1 ensures that N is covered and the next +1 is to make sure it is 
included (as the for loop stops at x - 1)) => First_ele = 1 XOR 2 XOR ... XOR N

No we also find the XOR Of all the elements excluding the first element. tmp =  out_arr[1] XOR out_arr[2]  XOR  out_arr[3] XOR ... XOR  out_arr[n-2] XOR out_arr[n-1]
Now we can workout that : let output_arr = x and input arr = y and tmp = b 

b =  x[1] XOR x[2]  XOR  x[3] XOR x[4]  XOR ... XOR  x[n-2] XOR x[n-1]
  = (x[1] XOR x[2]) XOR (x[3] XOR x[4]) XOR ... XOR (x[n-2] XOR x[n-1])
  =       y[1]      XOR       y[3]      XOR ... XOR       y[n-2]

and then finally as tmp is only missing the xor with the first elemet, and the First_ele contains XOR of all element we can say that 
Out_arr[0] ^ tmp = First_ele => First_ele ^ tmp = Output_arr[0] 

The rest is trivial and is covered in the previous version 

'''
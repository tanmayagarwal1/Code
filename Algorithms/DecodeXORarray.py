def DecodeArrayXord(arr, first):
	if not arr : raise ValueError 
	res = [first]
	for num in arr:
		res.append(res[-1] ^ num)
	return res 



arr = [6, 2, 7, 3]
first = 4
print(DecodeArrayXord(arr, first)) # [4, 2, 0, 7, 4]


'''
You are given the encoded array. You are also given an integer first, that is the first element of arr(original array), i.e. arr[0].
The encoded array is an XOred array of the original array 
ex :    if original array    = [1, 2, 3, 4]
        encoded(given) array = [(1 ^ 2), (2 ^ 3), (3 ^ 4)]

Notice the length of the encoded array is 1 less than the output array. Out task is to find the original array 

Solution : We know that : if : (a XOR b) = c, then a = (c XOR b) or b = (a XOR c)
basically the array which is given to us is : given_array[i] = output_arr[i] ^ output_arr[i + 1] ( which is in the form of a ^ b = c)

Hence : it can be re-written as : output_arr[i + 1] = output_arr[i] ^ given_arr[i]
Here we know the first element of the output array which is given to us : output_arr[0] = given

Hence output_arr[0] = [first_given_element]
then  output_arr[1] = output_arr[0] ^ given_arr[0]
then  output_arr[2] = output_arr[1] ^ given_arr[1]
then  output_arr[3] = output_arr[2] ^ given_arr[2]
.
.
.
.

And so on. 

'''
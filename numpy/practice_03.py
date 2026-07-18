import numpy as np

# ------------ Stack func() -------------

"""
Stacking is same as concatenation, the only difference is that stacking is done along a new axis
"""

arr1 = np.array([1,3,5,7])
arr2 = np.array([2,4,6,8])

data = np.stack((arr1, arr2), axis=1)

# print(data)


# ----------> Stacking Along Rows

rdata = np.hstack((arr1, arr2))   #  helper function: hstack() to stack along rows
# print(rdata)

# ----------> Stacking Along Columns

cdata = np.vstack((arr1, arr2))  #  helper function: vstack()  to stack along columns
# print(cdata)

# ----------> Stacking Along Height (depth)

hdata = np.dstack((arr1, arr2))  #  helper function: dstack() to stack along height, which is the same as depth
# print(hdata)


# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------

# ------------ array_split func() -------------

"""
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.
"""

arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)   # Split the array in 3 parts  
# newarr = np.array_split(arr, 4)   # Split the array in 4 parts  

# print(newarr)


# --------------------> Split Into Arrays

"""
The return value of the array_split() method is a list containing each of the split as an array.

If you split an array into 3 arrays, you can access them from the result just like any array element:
"""

# newarr = np.array_split(arr, 3)

# print(f"Array 1: {newarr[0]}")
# print(f"Array 2: {newarr[1]}")
# print(f"Array 3: {newarr[2]}")


# --------------------> Splitting 2-D Arrays

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)
# newarr = np.array_split(arr, 3, axis=1)   #  An alternate solution is using hsplit()

# print(newarr)


# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------


# ------------ searchsorted func() -------------

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)  # Find the index where the value 7 is

# print(f"index: {x}")

# --------------------> Search From the Right Side

rx = np.searchsorted(arr, 7, side='right')

# print(f"index: {rx}")


# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------


# ------------ Filtering Arrays -------------

arr = np.array([41, 42, 43, 44])

"""
--------> One way:

filter_arr = []  # Create an empty list

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

"""
# -----------> Another way: 
filter_arr = arr > 42


newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

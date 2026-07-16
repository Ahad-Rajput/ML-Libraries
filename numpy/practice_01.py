import numpy as np


arr = np.array([1,2,3,4,5], ndmin=5)  # Create an array with 5 dimension
# print(arr)
# print("No. of dimensions: ", arr.ndim)

brr = np.array([1,2,3,4,5,6])
# print(brr[5] + brr[0])   # Access the 5th and 0th index of array and add them

# Access an element in 2D array
ar = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(ar[1,3]) # 1st parameter show which 1D array to see, 2nd parameter show which 0D element to see 


arr_0 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr_0[1,1,1]) # 1st paramerter show which 2D to see, 2nd parameter show which 1D array to see, and 3rd parameter show which 0D array to see.


#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------


# Slicing in 2D array

arr_1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr_1[1, 0:4]) 
# print(arr_1[0:2, 2])

"""
Explaination of arr_1[0:2, 2]

        Col0 Col1 Col2 Col3 Col4
Row0 →   1    2   [3]   4    5
Row1 →   6    7   [8]   9   10

output: [3,8]

"""

# print(arr_1[0:2, 1:4])


#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------


# Data type

arr_2 = np.array(['apple', 'banana', 'cherry'])
# print(arr_2.dtype)

arr_3 = np.array([1,2,3,4], dtype='S')   # Create an array with data type string
# print(arr_3)
# print(arr_3.dtype)

arr_4 = np.array([1, 2, 3, 4], dtype='i4')

# print(arr_4)
# print(arr_4.dtype)

new_arr_4 = arr_4.astype('f')  # creates a copy of the array, and allows you to specify the data type as a parameter
# print(new_arr_4)
# print(new_arr_4.dtype)

newarr_4 = arr_4.astype(float) # Anoter way
# print(newarr_4)
# print(newarr_4.dtype)

arr_5 = np.array([1, 0, 3])

newarr_5 = arr_5.astype(bool)

# print(newarr_5)
# print(newarr_5.dtype)


#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

# Copy and View

arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()  # copy is a new array
# arr[0] = 32
# print(f"Original arr: {arr}")
# print(f"Copied arr: {arr_copy}")

arr_view = arr.view()  # view is just a view of the original array
arr[0] = 22
# print(f"Original arr: {arr}")
# print(f"Viewed arr: {arr_view}")

arr_view[1] = 55
# print(f"Original arr: {arr}")
# print(f"Viewed arr: {arr_view}")


#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------


# Shape of an Array

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

"""

(1, 1, 1, 1, 4)

Box
└── 1 Box
    └── 1 Box
        └── 1 Box
            └── 1 Array
                ├──1
                ├──2
                ├──3
                └──4

"""


import numpy as np

arr = np.arange(2, 22, 2)   # Printing 2 table
# print(arr)

a = np.array([[3, 4, 6, 1, 10], [2, 5, 7, 0, 9]])
# print(a)
# print(a.ndim)

a.sort()  # Sorting 'a' array
# print(a)

b = a.T   # Taking Transpose of 'a'
# print(b)

# ---------- Zeroes func() -----------

arr_0 = np.zeros(10)
# print(arr_0)

# ---------- Ones func() -----------

# arr_1 = np.ones(10)
arr_1 = np.ones(5, dtype='f')
# print(arr_1)

# ---------- Empty func() -----------

# arr_2 = np.empty(10)
arr_2 = np.empty(10, dtype=np.int64)
# print(arr_2)

# ---------- Full func() -----------

brr = np.full(5, 2)
# print(brr)

brr_2 = np.full((3,4), 5, dtype='f')
# print(brr_2)

# ---------- Linespace func() ----------

# ls_arr = np.linspace(2, 10, num=5)
ls_arr = np.linspace(2,100, num=54)
# print(ls_arr)

# ---------- Concatenate func() ----------

# For 1D:
a = np.array([1, 3, 5, 7, 9])
b = np.array([2, 4, 6, 8, 10])

# print(np.concatenate((a, b)))

# For 2D:
a_2 = np.array([[1,3,5],[7,9,11]])
b_2 = np.array([[2,4,6],[8,10,12]])

# print(np.concatenate((a_2, b_2), axis=0))
# print(np.concatenate((a_2, b_2), axis=1))

# For 3D:

a_3 = np.array([[[0,1,2],[6,7,8]], [[0,9,5],[4,5,3]], [[10,20,30],[100,90,80]]])

b_3 = np.array([[[10,20,30],[40,50,60]], [[100,99,98],[1,2,3]], [[3,5,7],[2,4,8]]])

# print(a_3)
# print("-----------------------------------")
# print(b_3)
# print("-----------------------------------")
# print(np.concatenate((a_3, b_3), axis=1))
# print(np.concatenate((a_3, b_3), axis=2))

# ----------------------------------------------------------------------

# print(a_3.ndim)
# print(a_3.size)
# print(a_3.shape)

# ---------------- Reshape -----------------

arr = np.arange(9)
# print(arr)

brr = arr.reshape(3,3)
brr = arr.reshape(9,1)
# print(brr)

# --------------- adding new_axis -----------------

a = np.array([1,2,33,10,9,5])
print(a)
b = a[np.newaxis, :]  # for row wise
c = a[:, np.newaxis]  # for col wise
# print(b)
# print(c)

# ---------------- basic math func() -----------------

# print(a+6)
# print(a-6)
# print(a*6)

# print(a.sum())
# print(a.mean())

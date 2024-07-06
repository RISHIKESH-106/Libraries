"NUMPY BASIC"
import numpy as np
arr= np.array([[1,2,3],[4,5,6]])
# Printing type of array object
print("Array in type of:",type(arr))
#dimmenisons of the array
print("No.of.dimmensions:",arr.ndim)
#shape of the array
print("Shape of Array:",arr.shape)
#Size of the  array
print("Size of the Arry is:",arr.size)
#type of the given array
print("Arry stores the elements of the type:",arr.dtype)


#1. CREATION OF NUMPY USING LISTS:
import numpy as np
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)

#2.CREATION OF NUMPY USING TUPLES:
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)


#3.CREATE ARRAY OF FIXED SIZE:
# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("An array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("An array initialized with all 6s." 
            "Array type is complex:\n", d)

# Create an array with random values
e = np.random.random((3, 3))
print ("A random array:\n", e)

#4.CREATE USING arrange() FUNCTION:
# Create a sequence of integers 
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("A sequential array with steps of 5:\n", f)

#Create a sequence of integers
#from 1 to 50 with steps of 2
ab=np.arange(1,50,2)
print("A sequential array with steps of 2:\n",ab)

#5.CREATE USING linspace() FUNCTION:
#Create a sequence of 10 values in range form 0 to 3
g=np.linspace(0,3,10)
print("A sequential array with 10 values between \"0 to 3\":\n",g)

#6. RESHAPING ARRAY USING RESHAPE METHOD:
#Reshaping the 3x4 array into 2x2x3 array
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
newarr=arr.reshape(2,2,3)
print("Original arrray:\n",arr)
print("----------------------------")
print("Reshaped array:\n",newarr)

#7.FLATTEN ARRAY:
arr=np.array([[1,2,3],[4,5,6]])
flat_arr=arr.flatten()
print("Original array:\n",arr)
print("Flattened array:\n",flat_arr)


#NUMPY BASIC OPERATIONS:
#1.OPERATIONS ON A SINGLE NUMPY ARRAY:
a=np.array([1,2,3,4,5,6,7,8,9])

#adding 1 to every element
print("Adding 1 to every element:",a+1)

#subtract 4 from every element
print("Subtracting 3 from each element:",a-3)

#multiply each element by 10
print("Multiplying every element by 10:",a*10)

#square each element
print("Squaring every element:",a**2)

#modify existing array
a*=2
print("Doubled each element of original array:",a)

#transpose of array
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nOriginal array:\n",a)
print('-------------------')
print("Transpose of array:\n",a.T)

#UNARY OPERATORS:

arr=np.array([[1,5,6],[4,7,2],[3,1,9]])

#max element of array
print("Largest element is:",arr.max())
print("Row wise max elements:",arr.max(axis=1))

#min element of array
print("Coloumn wise min elements:" ,arr.min(axis=0))

#sum of array elements
print("Sum of all array elements:",arr.sum())

#cumulative sum along each row
print("Cumulative sum along each row:\n",arr.cumsum(axis=1))



#BINARY OPERATORS:
a=np.array([[1,2],[3,4]])
b=np.array([[4,3],[2,1]])

#add arrays
print("Array sum:\n",a+b)

#multiply arrays(elementwise multiplication)
print("Array multiplication:\n",a*b)

#matrix multiplication
print("Matrix multiplication:\n",a.dot(b))

#exponential of array values (e^x,where x= 2.718281, eg:2*2.718281=2.e+0)
a = np.array([0, 9, 4, 16])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.square(a)* np.sign(a))



#NUMPY SORTING ARRAYS:
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]       
# Creating array
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))      
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))


#LIST TO  ARRAY:
# creating list
list = [1, 2, 3, 4]
# creating numpy array
sample_array = np.array(list)
print("List in python : ", list)
print("Numpy Array in python :",sample_array)


#MULTI-DEMENSIONAL ARRAY:
# creating list 
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
# creating numpy array
sample_array = np.array([list_1, list_2,list_3])
print("Numpy multi dimensional array in python\n",sample_array)
#shape of the array
print("The shape of the array:",sample_array.shape)
#datatype of the array
print("the datattype of the array:",sample_array.dtype)

#numpy.fromiter():
iterable = (a*a for a in range(8))
arr = np.fromiter(iterable, int)
print("fromiter() array :",arr)

#numpy.arrange():
b=np.arange(1, 20 , 2, dtype = np.int64)
print("arrange() arrary:",b)

#numpy.empty():     
#creates a random array without inserting the numbers

c=np.empty([4, 3],dtype = np.int32)
print("empty array:\n",c)

#numpy.ones():
d=np.ones([4, 3],dtype = np.int32)
print("arrays of ones:\n",d)

#numpy.zeroes():
e=np.zeros([4,3],dtype=np.int32)
print("Arrays of zeros:\n",e)

#SLICING OF THE ARRAY:
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
 #slicing
temp = arr[:2, ::2]
print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp)
 
temp1=arr[:2,:2]
print("Array with first 2 rows and 2 columns:\n",temp1)

temp2=arr[:3,:3]
print("Array with first 3 rows and 3 columns;\n",temp2)
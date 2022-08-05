def double_zero(array):

 i=0
 while i<len(array):
    if array[i]==0:
        array.insert(i,0)
        i=i+2
    elif  array==array:
      i=i+1     
 print (array)


double_zero([1,0,2,3,0,4,5,0])
double_zero([1,2,3])
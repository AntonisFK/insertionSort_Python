def insertionSort(arr):
  for i in xrange(len(arr)):
    j=i 
    while(j>0 and arr[j] < arr[j-1]):
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1
  print arr

arr = [100, 3, 4, 10, 8]
insertionSort(arr)

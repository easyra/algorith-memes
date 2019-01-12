def bubbleSort(arr):
  count = 1
  while count != 0:
    count = 0
    for i in range(len(arr) -1):
      if arr[i] > arr[i+1]:
        greaterInt = arr[i]
        smallerInt = arr[i+1]
        arr[i] = smallerInt
        arr[i+1] = greaterInt
        count += 1    

  print(arr)

bubbleSort([2, 6, 3, 9, 6, 1, 6, 8, 0, 4, 7, 5])
arr1 = [2, 6, 3, 9, 6, 1, 6, 8, 0, 4, 7, 5]

def selectionSort(arr):
  count = 0  
  while len(arr) != count:
    i = count
    for n in range(count, len(arr)):
      if arr[n] < arr[i]:
        i = n  
    arr.insert(count, arr[i])
    del arr[i+1]
    count += 1

  print(arr)  

selectionSort(arr1)   

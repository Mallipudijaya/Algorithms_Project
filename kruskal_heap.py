def heapify(arr, n, i): 
    smallest = i #Initialize max as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].w > arr[l].w:
      smallest = l
   
    if r < n and arr[smallest].w > arr[r].w:
      smallest = r

 
    if smallest != i:
      arr[i], arr[smallest] = arr[smallest], arr[i]
      heapify(arr, n, smallest) 

def heapsort(arr):
  n = len(arr)

  #Build MaxHeap
  for i in range(n //2, -1, -1):
    heapify(arr, n, i)

  #Extract elements from heap one by one
  for i in range(n - 1, 0, -1): 
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
  return arr
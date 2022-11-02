import heapq

def heapsort(iterable):
  h=[]
  result=[]
  for value in iterable:
    heapq.heappush(h,value)

  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1,3,6,2,6,84,68,5,3,5])
print(result)
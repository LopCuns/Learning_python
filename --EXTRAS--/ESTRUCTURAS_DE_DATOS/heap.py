import heapq

H = [2,5,89,14,87,45,7,1,31,81,44,56,92]

heapq.heapify(H)
heapq.heappush(H,3)
heapq.heappop(H)
heapq.heapreplace(H,8)
print(H)
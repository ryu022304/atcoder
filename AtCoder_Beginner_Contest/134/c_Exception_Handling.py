import heapq
n = int(input())
a_list = [int(input()) for _ in range(n)]
a_list_heap = list(map(lambda x:(-1)*x,a_list))
heapq.heapify(a_list_heap)
max_num = a_list_heap[0]*(-1)

for i in range(len(a_list)):
    if a_list[i] != max_num:
        print(max_num)
    else:
        tmp = heapq.heappop(a_list_heap)
        print(a_list_heap[0]*(-1))
        heapq.heappush(a_list_heap,tmp)

import heapq

def popHeap(heap, status, types):
    while heap:
        num = types*heapq.heappop(heap)
        
        if status[num]>0:
            status[num] -= 1
            break

def getHeapRoot(heap, status, types):
    while heap:
        num = types*heap[0]
        if status[num]>0:
            break
        
        heapq.heappop(heap)
    
    return types*heap[0] if heap else 0

def solution(operations):
    maxHeap = []
    minHeap = []
    status = {}
    
    for operation in operations:
        command, num = operation.split(' ')
        num = int(num)
        
        if command=='I':
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, num)
            status[num] = status.get(num,0)+1
            
        elif command=='D':
            if num==1:
                popHeap(maxHeap, status, -1)
            
            elif num==-1:
                popHeap(minHeap, status, 1)
    
    minHeapRoot = getHeapRoot(minHeap, status, 1)
    maxHeapRoot = getHeapRoot(maxHeap, status, -1)
    
    return [maxHeapRoot, minHeapRoot]
import heapq

CLEANING = 10

def time_to_minutes(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h*60+m

def solution(book_time):
    reservations = []
    for s, e in book_time:
        reservations.append((time_to_minutes(s), time_to_minutes(e)))

    reservations.sort()
    
    heap = []
    for start, end in reservations:
        available_time = end+CLEANING
        
        if heap and heap[0]<=start:
            heapq.heappop(heap)
        
        heapq.heappush(heap, available_time)
            
    return len(heap)
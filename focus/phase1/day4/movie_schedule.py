class PriorityQueue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self, items):
        self.queue.append(tuple(items))

    def dequeue(self): 
        curr = self.queue.pop(0)
        if len(self.queue) > 0:
            curr = curr
            for i,item in enumerate(self.queue):
                if curr[0] > item[0]: curr, self.queue[i] = item, curr
                if curr[0] == item[0]:
                    if curr[2] == "START" and item[2] == "END": curr, self.queue[i] = item, curr
                    if curr[1] > item[1]: curr, self.queue[i] = item, curr
        return curr

    def sort(self):
        self.queue.sort()
    

class Movie:
    def __init__(self, cinema_id, start_time, duration_time, break_time, closing):
        self.cinema_id = int(cinema_id)
        self.start_time = int(start_time)
        self.duration_time = int(duration_time)
        self.break_time = int(break_time)
        self.closing = int(closing)

    def main(self):
        end_point = self.start_time + self.duration_time
        while end_point <= self.closing:
            pq.enqueue((self.start_time, self.cinema_id, "START"))
            pq.enqueue((end_point, self.cinema_id, "END"))
            self.start_time += (self.duration_time + self.break_time) 
            end_point = (self.start_time + self.duration_time)
            
        
if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        cine, closing =  map(int, input().split())
        pq = PriorityQueue()
        for _ in range(cine):
            cinema_id, start_time, duration_time, break_time = map(int, input().split())
            movie = Movie(cinema_id, start_time, duration_time, break_time, closing)
            movie.main()

        pq.sort()
        print(f"Case #{tc}:")
        while len(pq.queue) > 0:
            res = pq.dequeue()
            print(f"{str(res[0])} {str(res[1])} {str(res[2])}")
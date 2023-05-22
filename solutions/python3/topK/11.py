# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/
import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time_spent=0
        cnt = collections.Counter(tasks)
        #create a PQ
        max_heap = []
        for task,freq in cnt.items():
            heapq.heappush(max_heap, (-freq, task))
        heapq.heapify(max_heap)

        while max_heap:
            tasks_available_in_round = n + 1
            cool_down_queue = collections.deque()
            # per round
            while max_heap and tasks_available_in_round:
                (freq, task) = heapq.heappop(max_heap)
                freq+=1
                time_spent+=1
                tasks_available_in_round-=1
                if freq<0:
                    cool_down_queue.append((freq,task))

            # add tasks for next round
            max_heap.extend(cool_down_queue)
            heapq.heapify(max_heap)

            # add idle time only if waiting tasks
            if max_heap:
                time_spent += tasks_available_in_round  #idle time

        return time_spent
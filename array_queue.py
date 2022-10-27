data_list = [1,2,3,4,5] # create list
data_list

print(data_list[0])

# use queue
import queue
data_queue = queue.Queue()

#isnert data
data_queue.put('funcoding')
data_queue.put(1)
data_queue.qsize() # check data size

# get data
data_queue.get()
data_queue.qsize()
data_queue.get()
data_queue.qsize()

# LifoQueue

import queue
data_queue = queue.LifoQueue()

data_queue.put('funcoding')
data_queue.put(1)

data_queue.qsize()
data_queue.get()

#PriorityQueue
"""
It is widely used to implement process scheduling 
method for multi-tasking.

"""

import queue

data_queue = queue.PriorityQueue()
#make sure put tuple into the put() 
data_queue.put((10, "korea"))
data_queue.put((5,1))
data_queue.put((15, 'china'))

data_queue.qsize()
data_queue.get()
data_queue.get()

#impelement enqueue, dequeue
queue_list = []

# define enqueue function
def enqueque(data):
    queue_list.append(data)

# define dequeue function
def dequeue(data):
    data = queue_list[0]
    del queue_list[0]
    return data

    








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




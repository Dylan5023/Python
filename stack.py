"""
what is a stack?
: Structure with limited access to data
- A structure in which data can be inserted or 
removed from only one end. 

Queue = FIFO
Stakc = LIFO

"""
# rcursive function

def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data -1)
        print('returned', data)

# use push and pop

#push
data = list()
data.append(1)
data.append(2)

#pop
data.pop()
data.pop()

# hands on stack
stack_list = list()

#push
def push(data):
    stack_list.append(data)
#pop
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data







from queue import Queue # FIFO Queue

q = Queue()
q.put('a')
q.put('b')
q.put('c')
q.put('d')

print(q.queue[0])  # a

from queue import Queue
class Buffer(object):
	'''Store pkts until their turn to be processed'''
	def __init__(self):
		self.queue = Queue()

	def enqueue(self, dev_pkt):
		'''Add dev, pkt tuple to be enqueue according to FIFO'''
		self.queue.put_nowait(dev_pkt)

	def dequeue(self):
		'''Remove and return according to FIFO'''
		return self.queue.get_nowait()

	def peek(self):
		'''View next item to be dequeued without removing it'''
		try:
			return self.queue.queue[0]
		except IndexError:
			return None

	def __iter__(self):
		return QueueIterator(self.queue)


class QueueIterator(object):
	def __init__(self, queue):
		self.queue = queue
		self.iteratorIndex = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.iteratorIndex < self.queue.qsize():
			item = self.queue.queue[self.iteratorIndex]
			self.iteratorIndex = self.iteratorIndex + 1
			return item
		else:
			 raise StopIteration


q = Buffer()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

for num in q:
	print(num)

if 1 in q:
	print('hooray')

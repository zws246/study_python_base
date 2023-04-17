"""
队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
队列是一种先进先出的（First In First Out）的线性表，简称 FIFO。允许插入的一端为
队尾，允许删除的一端为队头。队列不允许在中间部位进行操作！假设队列是 q=（a1，
a2，……，an），那么 a1 就是队头元素，而 an 是队尾元素。这样我们就可以删除时，总是
从 a1 开始，而插入时，总是在队列最后。这也比较符合我们通常生活中的习惯，排在第一
个的优先出列，最后来的当然排在队伍最后。
队列的操作：
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个 item 元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.items.insert(0, item)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.items == None

    def dequeue(self):
        """从头部删除一个元素"""
        return self.items.pop()

    def size(self):
        """返回队列的长度"""
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("bjsxt")
    print(q.size())
    print(q.dequeue())
    print (q.dequeue())
    print(q.dequeue())
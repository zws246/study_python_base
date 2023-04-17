"""
栈（stack），有些地方称为堆栈，是一种容器，可存入数据元素、访问元素、删除元素，
它的特点在于只能允许在容器的一端（称为栈顶端指标，英语：top）进行加入数据（英语：
push）和输出数据（英语：pop）的运算。没有了位置概念，保证任何时候可以访问、删除
的元素都是此前最后存入的那个元素，确定了一种默认的访问顺序。
由于栈数据结构只允许在一端进行操作，因而按照后进先出（LIFO, Last In First Out）
的原理运作
栈结构实现
实现步骤：
（1） Stack() 创建一个新的空栈
（2） push(item) 添加一个新的元素 item 到栈顶
（3） pop() 弹出栈顶元素
（4） peek() 返回栈顶元素
（5） is_empty() 判断栈是否为空
（6） size() 返回栈的元素个数
"""
class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == None

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的长度"""
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("bjsxt")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())




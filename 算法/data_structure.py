"""
数据结构（data structure)
数据是一个抽象的概念，将其进行分类后得到程序设计语言中的基本类型。如：int，float，
char 等。数据元素之间不是独立的，存在特定的关系，这些关系便是结构。数据结构指数据
对象中数据元素之间的关系。
Python 给我们提供了很多现成的数据结构类型，这些系统自己定义好的，不需要我们
自己去定义的数据结构叫做 Python 的内置数据结构，比如列表、元组、字典。而有些数据
组织方式，Python 系统里面没有直接定义，需要我们自己去定义实现这些数据的组织方式，
这些数据组织方式称之为 Python 的扩展数据结构，比如栈，队列等。
顺序表
在程序中，经常需要将一组（通常是同为某个类型的）数据元素作为整体管理和使用，
需要创建这种元素组，用变量记录它们，传进传出函数等。一组数据中包含的元素个数可能
发生变化（可以增加或删除元素）。
对于这种需求，最简单的解决方案便是将这样一组元素看成一个序列，用元素在序列里
的位置和顺序，表示实际应用中的某种有意义的信息，或者表示数据之间的某种关系。
这样的一组序列元素的组织形式，我们可以将其抽象为线性表。一个线性表是某类元素
的一个集合，还记录着元素之间的一种顺序关系。线性表是最基本的数据结构之一，在实际
程序中应用非常广泛，它还经常被用作更复杂的数据结构的实现基础。
根据线性表的实际存储方式，分为两种实现模型：
顺序表，将元素顺序地存放在一块连续的存储区里，元素间的顺序关系由它们的存储顺
序自然表示。
链表，将元素存放在通过链接构造起来的一系列存储块中。
Python 中的 list 和 tuple 两种类型采用了顺序表的实现技术，tuple 是不可变类型，即不
变的顺序表，因此不支持改变其内部状态的任何操作，而其他方面，则与 list 的性质类似。
"""
"""
timeit 模块可以用来测试一小段 Python 代码的执行速度。
class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
Timer 是测量小段代码执行速度的类。其中 stmt 参数是要测试的代码语句（statment）；setup
第 3 页
参数是运行代码时需要的设置；timer 参数是一个定时器函数，与平台有关。
timeit.Timer.timeit(number=1000000)
Timer 类中测试语句执行速度的对象方法。number 参数是测试代码时的测试次数，默认为
1000000 次。方法返回执行代码的平均耗时，一个 float 类型的秒数。
"""
#  【示例】测试 list 列表中 append、insert 方法执行速度


from timeit import Timer


def app_test():
    lis = []
    for i in range(10000):
        lis.append(i)


def insert_test():
    lis = []
    for i in range(10000):
        lis.insert(0, i)


"""
链表的定义
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是不像顺序表一样
连续存储数据，而是在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）。 单向链表
单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信
息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接
域则指向一个空值
"""
"""
class SingleNode(object):
    #单链表的结点

    def __init__(self, item):
        # _item 存放数据元素
        self.item = item
        # _next 是下一个节点的标识
        self.next = None

is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    # 初始方法
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 判断单链表是否为空
        return self.__head == None

    def length(self):
        # 单链表的长度
        # cur 先指向链表头
        # cur = self.__head
        # cur = self.__head
        # count = 0
        # if self.is_empty():
        #     return 0
        # while cur is not None:
        #     count += 1
        #     cur = cur.next
        # return count
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            # 将指向位置后移一个节点
            cur = cur.next
        return count

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        """
#头部添加元素
"""
        # 先创建一个节点保存item的值
        node = Node(item)
        # 把节点的链接指向头部节点
        node.next = self.__head
        # 把头节点链接指向保存的节点
        self.__head = node

    def append(self, item):
        """
#尾部添加
"""
        # 保存节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """
#在指定的位置插入元素
"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 先将新节点指向插入的位置
            node.next = cur.next
            # 再把插入节点指向前移一个
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            # 如果找到了元素
            if cur.item == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


def main():
    # time1 = Timer('app_test()', 'from __main__ import app_test')
    # time2 = Timer('insert_test()', 'from __main__ import insert_test')
    # print(time1.timeit(1000))
    # print(time2.timeit(1000))
# 初始化元素值为 20 的单向链表
# singleLinkList=SingleLinkList(20)
# 初始化一个空的单向链表
    singleLinkList = SingleLinkList()
    print('是否是空链表：', singleLinkList.is_empty())
    print('链表的长度：', singleLinkList.length())
    print('----------遍历单链表----------')
    singleLinkList.travel()
    print('--------查找---------')
    print(singleLinkList.search(20))
    print(singleLinkList.search(30))
    print('------头部插入-----------')

    singleLinkList.add(1)
    singleLinkList.add(2)
    singleLinkList.add(3)
    singleLinkList.travel()
    print('------尾部追加-----------')
    singleLinkList.append(10)
    singleLinkList.append(20)
    singleLinkList.append(30)
    singleLinkList.travel()
    print('链表的长度：', singleLinkList.length())
    print('----------指定位置插入----------')
    singleLinkList.insert(2, 100)
    singleLinkList.travel()
    singleLinkList.insert(-1, 200)
    singleLinkList.travel()
    singleLinkList.insert(100, 300)
    singleLinkList.travel()
    print('---------删除节点--------')
    singleLinkList.remove(100)
    singleLinkList.travel()
    singleLinkList.remove(200)
    singleLinkList.travel()
    singleLinkList.remove(300)
    singleLinkList.travel()




# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# # 链表类
# class SingleLinkedList:
#     def __init__(self, node=None):
#         self.__head = node
#         # 判断链表是否为空
#
#     def is_empty(self, ):
#         return True if self.__head is None else False
#         # 获取链表的长度
#
#     def length(self):
#         cur = self.__head
#         count = 0
#         if self.is_empty():
#             return 0
#         while cur is not None:
#             count += 1
#             cur = cur.next
#         return count
        # 遍历链表

#     def ergodic(self):
#         cur = self.__head
#         while cur is not None:
#             print(cur.value, end="->")
#             cur = cur.next
#     # 在头部添加
#
#
# def add(self, item):
#     node = ListNode(item)
#     cur = self.__head
#     node.next = cur
#     self.__head = node
#
#     # 尾部添加节点
#
#
# def append(self, item):
#     node = ListNode(item)
#     if self.is_empty():
#         self.__head = node
#     else:
#         cur = self.__head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = node
#
#
#     # 插入节点到指定位置
#
#
# def insert(self, pos, item):
#     node = ListNode(item)
#
#
# cur = self.__head
# pre = None
# index = 0
# while index < pos - 1:
#     index += 1
# pre = cur
# cur = cur.next
# node.next = cur
# pre.next = node
#
#
#     # 查找某一节点
#     def search(self, item):
#
#         cur = self.__head
#
#
#     index = 0
#     while cur.value != item:
#         if cur is None:  # 找不到返回False
#             return False
#     index += 1
#     cur = cur.next
#     return index
#
#
#     # 删除某一节点
#     def remove(self, item):
#
#         cur = self.__head
#
#
#     pre = None
#     while cur.value != item:
#         pre = cur
#     cur = cur.next
#     if pre is None:  # 删除的是头节点
#         self.__head = cur.next
#     else:
#         pre.next = cur.next
if __name__ == '__main__':
    main()

# 总结： cur !=0  这个不能用 必须 写成 cur is not None!!!!
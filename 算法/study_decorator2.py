"""
双向链表
一种更复杂的链表是“双向链表”或“双面链表”。每个节点有两个链接：一个指向前
一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最
后一个节点时，指向空值。
"""
"""
if __name__ == '__main__':
doubleLinkList=DoubleLinkList()
doubleLinkList.add(11)
doubleLinkList.add(22)
doubleLinkList.add(33)
doubleLinkList.travel()
print('-----------追加-----------')
doubleLinkList.append(100)
doubleLinkList.append(200)
doubleLinkList.append(300)
doubleLinkList.travel()
print('指定位置插入')
doubleLinkList.insert(-1,44)
doubleLinkList.travel()
doubleLinkList.insert(100,400)
doubleLinkList.travel()
doubleLinkList.insert(2,1000)
doubleLinkList.travel()
print('------删除节点--------')
doubleLinkList.remove(44)
doubleLinkList.travel()
doubleLinkList.remove(1000)
doubleLinkList.travel()
doubleLinkList.remove(400)
doubleLinkList.travel()
print('链表的长度：',doubleLinkList.length())
print('查找节点 11',doubleLinkList.search(11))
print('查找节点 111',doubleLinkList.search(111))
"""


class Note:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    """双向链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断是否空值"""
        return self.__head == None

    def length(self):
        """获取长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历列表"""
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print()

    def add(self, item):
        """头部插入元素"""
        note = Note(item)
        if self.is_empty():
            self.__head = note
        else:
            # 把插入的元素的下一个节点指向最头部的元素
            note.next = self.__head
            # 把原来最头部的元素的上一个节点由None替换为插入的元素
            self.__head.prev = note
            # 最后把头部的元素指向插入的元素
            self.__head = note

    def append(self, item):
        """尾部插入元素"""
        note = Note(item)
        if self.is_empty():
            self.__head = note
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 最后元素指向当前元素
            cur.next = note
            # 把插入的元素的上一个节点指向当前节点
            note.prev = cur
            # 把插入的元素的下一个节点指向空值
            note.next = None

    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur.next is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def insert(self, pos, item):
        """在指定位置加入节点"""
        if pos < 1:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            note = Note(item)
            cur = self.__head
            count = 0
            # 将位置移动到位置的前一个数
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 将note的上一个节点指向cur
            note.prev = cur
            # 将note的下一个节点指向cur.next
            note.next = cur.next
            # 将cur.next的上一个节点指向node
            cur.next.prev = note
            # 将cur的下一个节点指向node
            cur.next = note

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        note = Note(item)
        while cur.next is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

if __name__ == '__main__':
    doubleLinkList=DLinkList()
    doubleLinkList.add(11)
    doubleLinkList.add(22)
    doubleLinkList.add(33)
    doubleLinkList.travel()
    print('-----------追加-----------')
    doubleLinkList.append(100)
    doubleLinkList.append(200)
    doubleLinkList.append(300)
    doubleLinkList.travel()
    print('指定位置插入')
    doubleLinkList.insert(-1,44)
    doubleLinkList.travel()
    doubleLinkList.insert(100,400)
    doubleLinkList.travel()
    doubleLinkList.insert(2,1000)
    doubleLinkList.travel()
    print('------删除节点--------')
    doubleLinkList.remove(44)
    doubleLinkList.travel()
    doubleLinkList.remove(1000)
    doubleLinkList.travel()
    doubleLinkList.remove(400)
    doubleLinkList.travel()
    print('链表的长度：',doubleLinkList.length())
    print('查找节点 11',doubleLinkList.search(11))
    print('查找节点 111',doubleLinkList.search(111))
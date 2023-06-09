"""
算法概念
我们通过计算机进行编程，计算机多才多艺，但不太善于独立思考，我们必须提供详尽
的细节，使用它们能够明白的语言将算法提供给它们。
如果将最终写好运行的程序比作战场，我们码农便是指挥作战的将军，而我们所写的代
码便是士兵和武器。数据结构和算法则是兵法。我们可以不看兵法在战场上肉搏，如此，可
能会胜利，可能会失败。即使胜利，可能也会付出巨大的代价。我们写程序亦然：如果不懂
算法，有时面对问题可能会没有任何思路，不知如何下手去解决；大部分时间可能解决了问
题，可是对程序运行的效率和开销没有意识，性能低下；有时会借助别人开发的利器暂时解
决了问题，可是遇到性能瓶颈的时候，又不知该如何进行针对性的优化。
如果我们常看兵法，便可做到胸有成竹，有时会事半功倍！同样，如果我们常看算法，
我们写程序时也能游刃有余、明察秋毫，遇到问题时亦能入木三分、迎刃而解。
"""
# 【示例】如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有 a、b、c
# 可能的组合?
import time


def all_time(func):
    def function(*args):
        print('开始运行')
        start = time.time()
        func(*args)
        end = time.time()
        print('结束运行')
        print('总花费时间为:', end - start, '秒')

    return function


@all_time
def result1(num):
    """
    方法一
    :return:
    """
    print('方法', num)
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print('a:', a, 'b:', b, 'c:', c)


@all_time
def result2(num):
    """
    方法二
    :return:
    """
    print('方法', num)
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a:', a, 'b:', b, 'c:', c)


@all_time
def result3(num):
    """
    方法三
    :return:
    """
    # 已知 a,b,c 均不能大于500
    print('方法', num)
    for a in range(1, 501):
        for b in range(1, 501):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a:', a, 'b:', b, 'c:', c)


if __name__ == "__main__":
    result1(1)
    result1(2)
    result1(3)

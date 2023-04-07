# 什么是装饰器
"""
装饰器 （Decorator）：从字面上理解，就是装饰对象的器件。可以在不修改原有代码的情况下，为被
饰的对象增加新的功能或者附加限制条件或者帮助输出。
装饰器 有很多种，有函数的装饰器，也有类的装饰器。装饰器在很多语言中的名字也不尽相同，它体现的是设
式中的装饰模式，强调的是开放封闭原则。
的语法是将@装饰器名，放在被装饰对象上面。
"""
# 例如我们要对一个函数过程执行的时间进行统计
import time


#
# def request_baidu():
#     # 请求获得百度的页面
#     start = time.time()
#     time.sleep(3)
#     print('获得百度的页面')
#     end = time.time()
#     print(f'本次爬取共计耗时{end - start}秒')


# def request_qq():
#     # 请求获得qq的页面
#     start = time.time()
#     time.sleep(2)
#     print('获得qq的页面')
#     end = time.time()
#     print(f'本次爬取共计耗时{end - start}秒')


# 在request_baidu和request_qq函数中出现了大量的重复的代码，每当我需要获得一个页面的时间的时候都要
# 使用start,end来计算，我们现在来改写代码
# def all_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'本次爬取共计耗时{end - start}秒')


# def request_baidu():
#     # 请求获得百度的页面
#     time.sleep(3)
#     print('获得百度的页面')
#
#
# def request_qq():
#     # 请求获得qq的页面
#     time.sleep(2)
#     print('获得qq的页面')

# 改写后的代码我们通过传入函数名称来完成对时间的统计
# all_time(request_baidu) all_time(request_qq)
# 但改写后的函数很难实现对参数的传入，我们继续改下函数

# def request_url(url, num):
#     """
#     :param url: 需要爬取的页面
#     :param num: 爬取页面需要的时间
#     :return:
#     """
#     time.sleep(num)
#     print(f'获得{url}的页面')


# def all_time(func):
#     def function(url, num):
#         start = time.time()
#         func(url, num)
#         end = time.time()
#         print(f'本次爬取共计耗时{end - start}秒')
#     return function

# 通过改写后的函数 我们就实现了函数对参数传入的需要，为了更灵活的传入参数，Python采用@函数名的方式来实现
# 最终的效果
def all_time(func):
    def function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'本次爬取共计耗时{end - start}秒')

    return function


@all_time
def request_url(url, num):
    """
    :param url: 需要爬取的页面
    :param num: 爬取页面需要的时间
    :return:
    """
    time.sleep(num)
    print(f'获得{url}的页面')


# 同样我们还可以对其他的参数不一样的函数进行装饰
@all_time
def sorting(lis):
    for i in range(len(lis) - 1, 0, -1):
        for j in range(i):
            if lis[j] < lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
        return lis


if __name__ == '__main__':
    request_url('百度', 3)
    request_url('qq', 2)
    lis = [2, 3, 8, 9, 6, 7, 4, 5]
    sorting(lis)

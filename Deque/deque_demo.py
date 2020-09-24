from collections import deque

def main():
    #创建双端队列，参数为可迭代序列和最大长度，最大长度不可更改
    ints = deque((i for i in range(0, 9)), maxlen = 10)
    print("ints:", ints, "长度：", len(ints))
    #在队列右侧追加一个值
    ints.append(9)
    print("ints.append(9)：", ints, "长度：", len(ints))
    #在队列左侧追加一个值
    ints.appendleft(-1)
    print("ints.appendleft(-1)：", ints, "长度：", len(ints))
    #弹出队列右侧第一个值，pop方法不可带参数
    ints.pop()
    print("ints.pop()：", ints, "长度：", len(ints))
    # 弹出队列左侧第一个值，pop方法不可带参数
    ints.popleft()
    print("ints.popleft()：", ints, "长度：", len(ints))
    #移动队列一端n个元素至另一端，n为正数时表示从右到左，负数时为由左到右
    ints.rotate(3)
    print("ints.rotate(3)：", ints, "长度：", len(ints))
    ints.rotate(-3)
    print("ints.rotate(3)：", ints, "长度：", len(ints))
    ints.extend((11,12,13))
    #在队列右端拼接上一个可迭代对象.超出尺寸时，从左端删除元素
    print("ints.extend((11,12,13))：", ints, "长度：", len(ints))
    ints.extendleft((-1,-2,-3,-4))
    # 在队列左端拼接上一个可迭代对象,顺序会与可迭代对象顺序相反。超出尺寸时，从右端删除元素
    print("ints.extendleft((-1,-2,-3,-4))：", ints, "长度：", len(ints))



if __name__ == "__main__":
    main()
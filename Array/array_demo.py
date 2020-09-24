from array import array
from random import random

def main():
    #b   int     1字节    有符号
    #B   int     1字节    无符号
    #u   unicode 2字节
    #h/H int     2字节    小写字母有符号
    #i/I int     4字节    大写字母无符号
    #L   int     4字节
    #q/Q int     8字节
    #f   float   4字节
    #d   float   8字节
    #产生100个浮点数
    floats = array("f", (random() for i in range(10**2)))
    #将这些浮点数存储为文件，必须以二进制方式写
    with open("1.txt", "wb") as fp:
        floats.tofile(fp)
    #创建一个与floats同类型的数组
    floats2 = array("f")
    #从文件读取这些浮点数，必须以二进制方式读
    with open("1.txt", "rb") as f:
        floats2.fromfile(f, 10**2)
    #二者相等
    print(floats == floats2)

    #使用memoryview，在内存中直接操作数据
    #创建一个有符号,元素长度为2字节的数组
    ints = array("h", [-2, -1, 0, 1, 2])
    #获得ints在内存中的地址
    memv = memoryview(ints)
    #将地址里的数解释为1个字节长度的无符号整数
    memv = memv.cast("B")
    #输出
    """
    数据存储的大端模式。高字节在低地址上
    -2：     1000 0000 0000 0010
    反码:    1111 1111 1111 1101
    补码:    1111 1111 1111 1110
    1字节：      255       254 
    """
    print(memv.tolist())
    #设置第五个值为4,即[254, 255, 255, 255, 0, 4, 1, 0, 2, 0]
    # 0 4 ->
    # 0000 0100 0000 0000 =>  1024
    memv[5] = 4
    #已在ints上产生修改
    print(ints)
    #输出类型
    print(ints.typecode)
    #使用memoryview后，ints不能再修改
    ints2 = array("h", [-8, -6, -5, -4, 0, 0, 4, 5, 6])
    print("ints2:", ints2)
    print("ints + ints2:",ints + ints2)
    ints2[0] = -7
    print("ints2[0] = -7:", ints2)
    ints2.append(8)
    print("ints2.append(8):", ints2)
    print("ints2.count(0)", ints2.count(0))
    print("ints2.pop():", ints2.pop())
    print("ints2.pop():", ints2.pop())
    print("ints2.pop(2)",ints2.pop(2))
    print("ints2:", ints2)
    #删除第一个出现的数字，没有该数时不报错
    ints2.remove(0)
    print("ints2.remove(0):", ints2)

if __name__ == "__main__":
    main()
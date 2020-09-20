import bisect
#草堆
haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
#针
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
#格式化字符串，":"前表示第几个变量，"2d"表示两位整数,右对齐
row_fmt = "{0:2d} @ {1:2d}		{2}{0:<2d}"
def demo():
    for needle in reversed(needles):
        #查找针在草堆中可插入的位置,即不改变草堆的排序的插入位置
        #bisects是bisect_right的别名,bisect_left与它只是在两个数相等时，插入位置有所不同
        #insort是insort_right的别名,同理有insort_left
        position = bisect.bisect(haystack, needle)
        offsect = position * "  |"
        print(row_fmt.format(needle, position, offsect))
    #insort实现查找并插入
    for needle in needles:
        bisect.insort(haystack, needle)
    print(haystack)

if __name__ == "__main__":
    print("haystack ->", ' '.join('%2d' % n for n in haystack))
    demo()
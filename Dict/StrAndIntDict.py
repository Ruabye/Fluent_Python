import  collections
class myStrtoIntDict(dict):
    """
    自定义字典(映射)类型，直接继承 dict。可以使用字符/数字作为键访问字典里的值
    映射类型有__getitem__和__missing__方法
    当__getitem__方法没有找到值时，会调用__missing__方法
    """
    def __missing__(self, key):
        """
        需要判断key是否为字符类型。否则self[str(key)]里调用__getitem__没有找到值时，会再次调用__missing__方法，导致死循环
        """
        if isinstance(key, str):
            return None
        return self[str(key)]

    def __contains__(self, item):
        """
        实现in关键字。
        需要使用self.keys(),直接item in self会再次调用__contains__方法，出现死循环
        列表的keys()方法经过优化,访问速度很快
        """
        if item in self.keys() or str(item) in self.keys():
            return True
        return False

if __name__ == "__main__":
    #my_dict[3]与my_dict["3"]返回的值是固定的，因为__getitem__会优先执行
    my_dict = myStrtoIntDict({"1":10, "2":20,"3":40, 3:20})

    print(my_dict[3])
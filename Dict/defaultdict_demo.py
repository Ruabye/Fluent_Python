import collections
#普通的dict中可以用setdefault(k,default=None)获得dict[k]的值，如果获取不到，则设置dict[k]=default
#get(k,default)获得dict[k]的值，如果获取不到，则返回default

def charcount(string):
    #统计字符出现的次数
    #创建一个默认为int的字典。可选str、list、dict
    dicts = collections.defaultdict(int)
    #defaultdict的关键是__missing__方法
    # print(collections.defaultdict.__missing__.__doc__)
    #default_factory为默认类型
    # print(dicts.default_factory)
    for s in string:
        dicts[s] += 1
    for i in sorted(dicts.keys(), key=str.upper):
        print(i, dicts[i])
if __name__ == "__main__":
    string = "safuwahofiapfao;jdfioa;jdagfliahdkjasgfialghiaHFWGF8OQGWDITG287EYafpsajfgpojapafawpjfDP[jkfpafj"
    charcount(string)
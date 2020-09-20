import collections
from random import choice
#一个只有属性，没有方法的类。用“.”方法获得变量 如：print(deck[0].rank)
Card = collections.namedtuple("Card",['rank', 'suit'])
class FrenchDeck:
    #构造牌面s
    ranks = [i for i in range(2, 10)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._card = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spade_sort(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":

    deck = FrenchDeck()
    print("纸牌数目：" + str(len(deck)))
    print("随机抽取一张卡牌：" + str(choice(deck)))
    print("纸牌信息：")
    for p in range(len(deck)):
        print(deck[p])
    print("升序排序：")#sorted默认升序，设置reverse=True改为降序
    for d in sorted(deck, key=spade_sort, reverse=True):
        print(d)



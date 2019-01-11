class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()

        list = []
        for i in range(len(deck))[::-1]:
            if len(list) != 0:
                tmp = list[0]
                list.pop(0)
                list.append(tmp)
                list.append(deck[i])

            else:
                list.append(deck[i])
        list.reverse()
        return list

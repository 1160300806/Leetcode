class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        list = set()
        for i in pattern:
             list.add(i)
        result = []
        for i in words:
            dict = {}
            flag = True
            for j in range(len(i)):
                if i[j] in dict.keys():
                    if dict[i[j]]!=pattern[j]:
                        flag = False
                        break
                else:
                    dict[i[j]] = pattern[j]
            if flag is True and len(dict) == len(list):
                result.append(i)
        return result

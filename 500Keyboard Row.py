class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        list1 = ['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p']
        list2 = ['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']
        list3 = ['Z','X','C','V','B','N','M','z','x','c','v','b','n','m']
        for i in words:
            flag = True
            if i[0] in list1:
                for j in range(1,len(i)):
                    if i[j] not in list1:
                        flag = False
                        break

            if i[0] in list2:
                for j in range(1, len(i)):
                    if i[j] not in list2:
                        flag = False
                        break
            if i[0] in list3:
                for j in range(1, len(i)):
                    if i[j] not in list3:
                        flag = False
                        break
            if flag is True:
                result.append(i)
        return result

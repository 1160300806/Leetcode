import string
class Solution(object):
    def numUniqueEmails(self, emails):
        result = set()
        for i in emails:
            local=i.split("@")[0]
            com = i.split("@")[1]
            local_real = local.split("+")[0]
            local_real = local_real.replace(".","")
            result.add(local_real+com)
        return len(result)

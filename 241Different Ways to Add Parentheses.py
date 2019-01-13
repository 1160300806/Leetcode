class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if ("-" not in input) and ("+" not in input) and ("*" not in input):
            return [(int)(input)]
        else:
            result = []
            for i in range(len(input)-1):
                if input[i] == "-":
                    for j in self.diffWaysToCompute(input[:i]):
                        for k in self.diffWaysToCompute(input[i+1:]):
                            result.append(j-k)
                elif input[i] == "+":
                    for j in self.diffWaysToCompute(input[:i]):
                        for k in self.diffWaysToCompute(input[i+1:]):
                            result.append(j+k)
                elif input[i] == "*":
                    for j in self.diffWaysToCompute(input[:i]):
                        for k in self.diffWaysToCompute(input[i+1:]):
                            result.append(j*k)
            return result

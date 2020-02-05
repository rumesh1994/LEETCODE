class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []

        # Split the string and convert to upper case and join to form a string
        s = "".join(S.split("-")).upper()
        N = len(s)

        # If length of S is not divisible by K
        if N % K != 0:
            res.append(s[: N % K])

        # Append sliced string os size K in list 
        for i in range(N % K, N, K):
            res.append(s[i : i + K])

        # Return a string by joining the list
        return "-".join(res)
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str] ["abc","deq","mee","aqq","dkd","ccc"]
        :type pattern: str 'abb'
        :rtype: List[str]
        """
        #Keeps a track of pattern 'abb'
        ptrack = []

        #Keeps a track of words 'mee' 'aqq' similar to pattern
        strack = []

        #list('abb') = ['a','b','b']
        for i in list(pattern):
            ptrack.append(list(pattern).index(i))
        #ptrack = [0,1,1]

        for t in words:
            xt = []
            for x in list(t):
                xt.append(list(t).index(x))
                #xt = [0,0,0] for 'ccc'
            #If pattern of word t matches with ptrack, append to strack
            if xt == ptrack:
                strack.append(t)
        return strack
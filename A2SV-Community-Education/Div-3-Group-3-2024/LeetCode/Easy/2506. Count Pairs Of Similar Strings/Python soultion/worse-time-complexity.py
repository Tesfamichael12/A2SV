class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        mydict = {}
       
        for word in words:
            s = str(sorted(set(word))) # we cannot use a set as a key for dicts so the must be changed to other form
            if s in mydict:
                mydict[s] += 1
            else:
                mydict[s] = 1

        for i in mydict.values():
                count += (i * (i - 1)//2)

        return count


# note 
# sorting a string takse O(n * L lon n) where L is the avarage length each string
# over all TC = O(n * L log n) + O(n)
# SP = O(n * L)
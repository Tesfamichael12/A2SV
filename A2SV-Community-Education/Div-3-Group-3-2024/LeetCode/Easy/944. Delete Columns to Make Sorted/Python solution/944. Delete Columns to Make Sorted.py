class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        c = len(strs[0])
        delete_count = 0
        all_strs = ''
        for i in range(n):
            all_strs += strs[i]
        for i in range(c):
            a, b = i, i + c
            for j in range(n - 1):
                if all_strs[a] > all_strs[b]:
                    delete_count += 1
                    break
                a += c
                b += c
        
        return delete_count
                

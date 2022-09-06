#Time complexity: O(m)
#Space complexity: O(n)
#Worked in Leetcode: Yes
#Any Issues: No

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(p)):
            c = p[i]
            hashmap[c] = hashmap.get(c, 0) + 1
            
        match = 0
        for i in range(len(s)):
            #inn
            inn = s[i]
            if inn in hashmap:
                count = hashmap.get(inn)
                count -= 1
                if count == 0:
                    match += 1
                    
                hashmap[inn] = count
                
            #out
            if i >=len(p):
                out = s[i-len(p)]
                if out in hashmap:
                    count = hashmap.get(out)
                    count += 1
                    if count == 1:
                        match -= 1
                    hashmap[out] = count
                        
            if len(hashmap) == match:
                result.append(i-len(p) + 1)
        return result

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
 
        for word in strs:
            new = tuple(sorted(word))
            anagram[new].append(word) 
        return list(anagram.values())

   
            

        
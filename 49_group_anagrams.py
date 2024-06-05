class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        AnagramsDict = {} # Sorted Anagram as Key : Actual Anagram
        for i in strs:
            SortedWord = ''.join(sorted(i))

            if SortedWord in AnagramsDict:
                AnagramsDict[SortedWord].append(i)

            else:
                AnagramsDict[SortedWord] = [i]

        return list(AnagramsDict.values())

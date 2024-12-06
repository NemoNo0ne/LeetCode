class Solution(object):
    def groupAnagrams(self, strs):
        strs_hash = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in strs_hash:
                strs_hash[sort_word] = []
            strs_hash[sort_word].append(word)

        return list(strs_hash.values())

s = Solution()

# Test cases for Group Anagrams
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(s.groupAnagrams([""]))  # Expected: [[""]]
print(s.groupAnagrams(["a"]))  # Expected: [["a"]]
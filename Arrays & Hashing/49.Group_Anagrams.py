class Solution(object):
    def groupAnagrams(self, strs):
        strs_hash = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in strs_hash:
                strs_hash[sort_word] = []
            strs_hash[sort_word].append(word)

        return list(strs_hash.values())

sol_49 = Solution()

# Test cases for 49. Group Anagrams
print(sol_49.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(sol_49.groupAnagrams([""]))                                           # Expected: [[""]]
print(sol_49.groupAnagrams(["a"]))                                          # Expected: [["a"]]

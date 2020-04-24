class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) < 2:
            return strs[0]
        result = ""
        for index in range(len(strs[0])):
            first_string_letter = strs[0][index]
            for s in range(1, len(strs)):
                if len(strs[s]) <= index or first_string_letter != strs[s][index]:
                    return result
            result += first_string_letter
        return result

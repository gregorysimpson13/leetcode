# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

# Constraints:

# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.

from typing import List
import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        words, digits = [], []
        heapq.heapify(words)
        for log in logs:
            if log[:3] == 'dig':
                digits.append(log)
            else:
                heapq.heappush(words, log)
        return words + digits

class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, words_dict = [], {}
        for log in logs:
            log_split = log.split(' ')
            if log_split[1].isnumeric():
                digits.append(log)
            else:
                words_dict[log] = (log[len(log_split[0]):], log_split[0])
        return sorted(words_dict.keys(), key=lambda x: words_dict[x]) + digits

inputs = [["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
["t kvr", "r 3 1", "i 403", "7 so", "t 54"],
["r 3 1", "i 403", "t 54"],
["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]]

for arg in inputs:
    print(Solution1().reorderLogFiles(arg))
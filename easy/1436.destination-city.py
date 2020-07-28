#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ingoing, outgoing = set(), set()
        for ingo, outg in paths:
            ingoing.add(ingo); outgoing.add(outg)
        return "".join(outgoing - ingoing)
# @lc code=end


#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        date_split = date.split()
        day, month, year = date_split[0][:-2], month_dict[date_split[1]], date_split[2]
        day = "0" + day if len(day) == 1 else day
        return "-".join([year, month, day])

# @lc code=end


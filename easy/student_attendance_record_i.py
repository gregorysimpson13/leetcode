# 551. Student Attendance Record I - EASY
# https://leetcode.com/problems/student-attendance-record-i/


# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

def checkRecord(s: str) -> bool:
    reward_map = {'A': 0, 'L': 0}
    for i in range(len(s)):
        if s[i] == 'A':
            reward_map['A'] = reward_map['A'] + 1
            if reward_map['A'] >= 2: return False
        if s[i] == 'L':
            reward_map['L'] = reward_map['L'] + 1
            if reward_map['L'] >= 3:
                return False
        else: reward_map['L'] = 0
    return True


print(checkRecord("PPALLP"), True)
print(checkRecord("PPALLL"), False)
print(checkRecord("PPALLA"), False)

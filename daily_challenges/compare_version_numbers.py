#Runtime: O(n)
#Space: O(n)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
        v1, v2 = version1.split('.'), version2.split('.')
        ptr_1, ptr_2 = 0, 0
        while ptr_1 < len(v1) or ptr_2 < len(v2):
            if ptr_1 < len(v1) and ptr_2 < len(v2):
                if int(v1[ptr_1]) > int(v2[ptr_2]): return 1
                if int(v1[ptr_1]) < int(v2[ptr_2]): return -1
            elif ptr_1 < len(v1):
                if int(v1[ptr_1]): return 1
            else:
                if int(v2[ptr_2]): return -1
            ptr_1, ptr_2 = ptr_1 + 1, ptr_2 + 1
        return 0
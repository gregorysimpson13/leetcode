class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotations(target):
            a_rot = b_rot = 0
            for a, b in zip(A,B):
                if a != target and b != target: return float('inf')
                if b != target: b_rot += 1
                if a != target: a_rot += 1
            return min(a_rot, b_rot)
        min_rotations = min(rotations(A[0]), rotations(B[0]))
        return min_rotations if min_rotations != float('inf') else -1
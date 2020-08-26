class Solution:
    # 1 prereq to 0
    # [0,1]
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites: return True
        taken = set(range(numCourses))
        course_dict = defaultdict(list)
        for course, prereq in prerequisites:
            if course in taken: taken.remove(course)
            course_dict[course].append(prereq)
        def dfs(course_num, visited=set()):
            if course_num in taken: return True
            for prereq in course_dict[course_num]:
                if prereq in visited: return False # circular dependency
                visited.add(prereq)
                if not dfs(prereq, visited): return False
                visited.remove(prereq)
            taken.add(course_num)
            return True
        for num in course_dict.keys():
            if not dfs(num): return False
        return True
            
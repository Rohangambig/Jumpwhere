from collections import deque

def canFinish(numCourses, prerequisites):
    adj_list = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    completed_courses = 0

    while queue:
        course = queue.popleft()
        completed_courses += 1  
        
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1  
            if in_degree[neighbor] == 0:
                queue.append(neighbor)  
    
    return completed_courses == numCourses

#
print(canFinish(2, [[1,0]]))  
print(canFinish(2, [[1,0], [0,1]]))  

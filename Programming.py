from datetime import datetime
from bisect import bisect_left, bisect_right

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

submissions = []
user_max_points = {}
total_submissions = 0
error_submissions = 0
user_error_counts = {}
time_points = []

while True:
    line = input().strip()
    if line == '#':
        break
    UserID, ProblemID, TimePoint, Status, Point = line.split()
    Point = int(Point)
    submissions.append((UserID, ProblemID, TimePoint, Status, Point))
    time_points.append(TimePoint)
    
    total_submissions += 1
    
    if Status == "ERR":
        error_submissions += 1
        if UserID not in user_error_counts:
            user_error_counts[UserID] = 0
        user_error_counts[UserID] += 1
    else:
        if UserID not in user_max_points:
            user_max_points[UserID] = {}
        if ProblemID not in user_max_points[UserID]:
            user_max_points[UserID][ProblemID] = 0
        user_max_points[UserID][ProblemID] = max(user_max_points[UserID][ProblemID], Point)

submissions.sort(key=lambda x: x[2])
time_points.sort()

while True:
    query = input().strip()
    if query == '#':
        break

    if query == "?total_number_submissions":
        print(total_submissions)
    
    elif query == "?number_error_submision":
        print(error_submissions)
    
    elif query.startswith("?number_error_submision_of_user"):
        _, UserID = query.split()
        print(user_error_counts.get(UserID, 0))
    
    elif query.startswith("?total_point_of_user"):
        _, UserID = query.split()
        total_points = sum(user_max_points.get(UserID, {}).values())
        print(total_points)
    
    elif query.startswith("?number_submission_period"):
        _, from_time, to_time = query.split()
        from_seconds = time_to_seconds(from_time)
        to_seconds = time_to_seconds(to_time)
        
        from_index = bisect_left(time_points, from_time)
        to_index = bisect_right(time_points, to_time)
        
        count = to_index - from_index
        print(count)


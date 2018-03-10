def have_trains_crashed(speed_1, speed_2):
    if (dist - alter_course_waypoint) / speed_2 <= alter_course_waypoint / speed_1:
        return True
    else:
        return False


dist = 10
alter_course_waypoint = 4

print(have_trains_crashed(3, 6))



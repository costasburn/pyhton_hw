def have_trains_crashed(speed_1, speed_2):
    distance = 10
    alter_course_waypoint = 4
    if (distance - alter_course_waypoint) / speed_2 <= alter_course_waypoint / speed_1:
        return True
    else:
        return False


print(have_trains_crashed(3, 6))



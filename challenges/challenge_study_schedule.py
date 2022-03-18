def study_schedule(permanence_period, target_time):
    if not target_time or target_time < 0:
        return

    students_in_target_time = 0  # students counter
    for in_time, out_time in permanence_period:

        if not isinstance(in_time, int) or not isinstance(out_time, int):
            return
        # target_time between in_time and out_time
        elif in_time <= target_time <= out_time:
            students_in_target_time += 1  # add 1 in students counter
    return students_in_target_time

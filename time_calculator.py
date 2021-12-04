def add_time(module_x, module_y, module_z = False):
    x_1 = int(module_x.partition(':')[0])
    x_2 = int(module_x.partition(':')[2].split()[0])
    y_1 = int(module_y.partition(':')[0])
    y_2 = int(module_y.partition(':')[2])

    p_hour = 0
    minute = 0
    h_1 = x_1
    h_2 = x_2
    m_1 = y_1
    m_2 = y_2
    sum_min = h_2 + m_2
    if m_1 == 24 :
        m_1 = 0
    if sum_min >= 60:
        sum_min -= 60
        m_1 += 1
        minute += sum_min
    else:
        minute += sum_min
    sum_hour = h_1 + m_1
    if sum_hour >= 13 :
        p_hour = sum_hour % 12
    else:
        p_hour += sum_hour
        # print(str(p_hour))
        # print(str(minute).zfill(2))

    check_AMorPM = module_x.partition(':')[2].partition(' ')[2]
    filp_AP = {"AM": "PM", 'PM': 'AM'}
    flip_1 = x_1  # module flip Am or Pm
    flip_2 = y_1
    f_m1 = x_2
    f_m2 = y_2
    if f_m1 + f_m2 >= 60:
        flip_1 += 1
    count_flip = int(flip_1 + flip_2 ) / 12
    if int(count_flip) % 2 == 1 :
        check_AMorPM = filp_AP[check_AMorPM]
    else:
        pass

    module_a = str(p_hour) + ':' + str(minute).zfill(2) + ' ' + check_AMorPM
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: "Wednesday", 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    day_num = {'sunday': 0, 'monday': 1, 'tuesday': 2, "wednesday": 3, 'thursday': 4, 'friday': 5, 'saturday': 6}
    day_1 = x_1
    day_2 = y_1
    c_day = module_x.partition(':')[2].partition(' ')[2]
    sum_day = day_1 + day_2
    find_day = day_2 // 24
    if c_day == 'PM' and sum_day >= 12 :
        find_day += 1

    if module_z :
        module_z = module_z.lower()
        index_1 = int((day_num[module_z]) + find_day ) % 7
        new_day = day[index_1]
        module_a += ", "+str(new_day).rstrip()

    if find_day == 1 :
        return str(module_a)+" "+"(next day)"
    elif find_day > 1 :
        return  module_a+''" ("+str(find_day)+" days later)"
    return module_a


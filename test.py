day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: "Wednesday", 4: 'Thursday', 5: 'Friday', 6: 'Saturday',}
day_num = {'Sunday':0 , 'Monday': 1  , 'Tuesday': 2  , "Wednesday":3 , 'Thursday': 4  ,'Friday': 5 , 'Saturday': 6 }
print(day_num['tueSday'])
if m_1 >= 24:
    m_1 = 0
if h_2 + m_2 >= 60:  # module find Time
    minute = h_2 + m_2 - 60
    m_1 += 1
    # print(minute)
else:
    minute = h_2 + m_2
    # print(minute)
while h_1 >= 13:
    h_1 = h_1 - 12
if m_1 + h_1 >= 13:
    h3 = m_1 + h_1 - 12
else:
    h3 = m_1 + h_1  # module A # find time done
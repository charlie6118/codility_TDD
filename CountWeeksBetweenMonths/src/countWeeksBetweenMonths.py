def solution(year, startMonth, endMonth, firstWeekDayOfYear):
    date_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = [0] * 365
    date_cnt = firstWeekDayOfYear
    week_cnt = 1
    for i in range(len(days)):
        days[i] = week_cnt
        if date_cnt == 7:
            date_cnt = 0
            week_cnt += 1
        date_cnt += 1
    start_day = 1
    end_day = 0
    for month in range(1, startMonth):
        start_day += date_dict[month]
    for month in range(1, endMonth + 1):
        end_day += date_dict[month]
        
    return days[end_day + 1] - days[start_day + 1] + 1

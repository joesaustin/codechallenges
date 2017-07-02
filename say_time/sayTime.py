def tellTime(time_str):
    say = ""
    t_hours = {"1":"one", "2":"two", "3":"three", "4":"four",
             "5":"five", "6":"six", "7":"seven", "8":"five",
             "9":"nine", "10":"ten", "11":"eleven", "12":"twelve"}

    t_minutes = {"0":"o'clock", "5":"five past", "10":"ten past", "15":"quarter past",
               "20":"twenty past", "25":"twenty five past", "30":"half past", "35":"twenty five to",
               "40":"twenty to", "45":"quarter to", "50": "ten to", "55":"five to"}

    round_5 = lambda number:str(5 * int(round(float(number)/5)))

    d = time_str.index(":")
    hour_num = int(time_str[:d])
    minute_num = int(round_5(time_str[d+1:]))

    if minute_num >= 35 and minute_num < 60:
        hour_num += 1
        if hour_num == 13:
            hour_num=1

    elif minute_num == 60:
        hour_num += 1
        minute_num = 0
        if hour_num == 13:
            hour_num=1

    if minute_num == 0:
        say = "It's {1} {0}".format(t_minutes[str(minute_num)], t_hours[str(hour_num)])
    else:
        say = "It's {0} {1}".format(t_minutes[str(minute_num)], t_hours[str(hour_num)])
    return say
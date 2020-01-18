def time_converter(time):
    new_hours = 0

    if int(time[0:2]) >= 13:
        new_hours = int(time[0:2]) - 12
        result = str(new_hours) + time[2:] + " p.m."
    elif int(time[0:2]) == 12:
        result = time + " p.m."
    elif time == "00:00":
        result = str("12" + time[2:] + " a.m.")

    else:
        result = time + " a.m."

    if int(result[0]) == 0:
        result = result[1:]
    else:
        pass

    return result

#This code converts 24hr time format into 12hr AM/PM format

print(time_converter('13:00'))
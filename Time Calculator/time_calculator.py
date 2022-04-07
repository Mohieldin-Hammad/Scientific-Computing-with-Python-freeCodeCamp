def add_time(start, duration, day = None):
    # Create a list of week days if  day is exists
    if day is not None:
        # Make sure that the day letters are clear for example "tueSday" will be saved as "Tuesday"
        day = day.lower().capitalize()
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # 4:03 PM -> ["4:03", "PM"]
    temp = start.split()

    # Defining a dictionary that will be use in calculation
    # # The base start time is number "0"
    # if temp[1] == "PM":
    #     periods = {"0":"PM", "1":"AM"}
    # else:
    #     periods = {"0":"AM", "1":"PM"}
    
    if temp[1] == "PM":
        periods = ["PM", "AM"]
    else:
        periods = ["AM","PM"]

    hours = int(temp[0].split(":")[0])
    min = int(temp[0].split(":")[1])
    dur_h = int(duration.split(":")[0])
    dur_m = int(duration.split(":")[1])
    f_per = None

    # Calcute the final min that will be printed 
    f_min = min + dur_m
    if f_min >= 60:
        f_min %= 60
        # If the summation of min is > 60 that means one hour has been finished
        hours += 1    
    f_min = str(f_min).zfill(2)
    
    # Calculate the final hour that will be printed
    # The algorithm is work like after geting the summtion of "start" hours with "duration" hours including if the summaion of minuts > 60 so there is one plus hour
    # After geting the answer of the summation, answer mod 12 will equal the final hour 
    # Also make sure if the final hour == 0, this mean it's 12 hours
    f_hour = (hours + dur_h) % 12
    if f_hour == 0:
        f_hour = 12
    f_hour = str(f_hour)    

    # The calculation here will select from two choices "0", "1" 
    # If the answer is 0 that means the start period didn't change after the time summation
    # Otherwise if the answer is 1, then the period has been changed 
    f_per = periods[((hours + dur_h) // 12) % 2]

    count = None
    # Calculating the counts of days after time summation
    if periods[0] == "PM":
        count = round((hours + dur_h) / 24) 
    elif periods[0] == "AM":
        count = round((hours + dur_h) / 48)
    
    # geting the current week day after the time summation
    if day is not None:
        f_day = days[(count + days.index(day) ) % 7]
    
    if count == 1:
        if day is None:
            return f"{f_hour}:{f_min} {f_per} (next day)"    
        return f"{f_hour}:{f_min} {f_per}, {f_day} (next day)"
    
    if count == 0:
        if day is None:
            return f"{f_hour}:{f_min} {f_per}"
        return f"{f_hour}:{f_min} {f_per}, {f_day}"
    
    if count > 1:
        if day is None:
            return f"{f_hour}:{f_min} {f_per} ({count} days later)"
        return f"{f_hour}:{f_min} {f_per}, {f_day} ({count} days later)"
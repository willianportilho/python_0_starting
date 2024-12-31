import time

def get_epoch_time():
    epoch_time = 0

    gtm = time.gmtime(epoch_time)

    formated_epoch_time = time.strftime("%B %e, %Y", gtm)
    formated_epoch_time = formated_epoch_time.replace("  ", " ")

    return (formated_epoch_time)

def get_current_secs_time():
    current_secs_time = time.time()

    int_cur_time = int(current_secs_time)
    dec_cur_time = current_secs_time - int_cur_time

    int_cur_time = f"{int_cur_time}:,"

    dec_cur_time = round(dec_cur_time, 4)
    print(current_secs_time)
    print(dec_cur_time)
    dec_cur_time = str(dec_cur_time)
    dec_cur_time = dec_cur_time.replace("0.", "")

    formated_cur_secs_time = int_cur_time + dec_cur_time

    return(formated_cur_secs_time)

print("Seconds since", get_epoch_time(), ":", get_current_secs_time())

#print("cur = ", current_secs_time)
#print("new = ", formated_time)
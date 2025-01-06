import time


def epoch_time():
    epoch_time = 0

    gmt = time.gmtime(epoch_time)

    formated_epoch_date = time.strftime("%B %e, %Y", gmt)
    formated_epoch_date = formated_epoch_date.replace("  ", " ")

    return (formated_epoch_date)


def current_secs_time(cur_secs_time):
    str_cur_secs_time = str(cur_secs_time)
    cut_time = str_cur_secs_time[:15]

    int_part, dec_part = cut_time.split(".")
    int_part = f"{int(int_part):,}"

    formated_time = int_part + "." + dec_part

    return (formated_time)


def scientific_notation(cur_time):
    new_notation = f"{cur_time:.2e}"

    return (new_notation)


def current_date(cur_secs_time):
    gmt = time.gmtime(cur_secs_time)
    formated_cur_date = time.strftime("%b %e %Y", gmt)
    formated_cur_date = formated_cur_date.replace("  ", " ")

    return (formated_cur_date)


def main():
    cur_secs_time = time.time()
    print("Seconds since", epoch_time() + ":",
          current_secs_time(cur_secs_time),
          "or", scientific_notation(cur_secs_time),
          "in scientific notation")
    print(current_date(cur_secs_time))


if __name__ == "__main__":
    main()

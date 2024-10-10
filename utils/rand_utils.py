

def num_or_zero_if_empty(num_str):
    if num_str == " " or num_str == "":
        return 0
    else:
        return int(num_str)
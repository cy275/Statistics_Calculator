def median(a):
    a = sorted(a)
    list_length = len(a)
    num = list_length//2
    if list_length % 2 == 0:
        median_num = (a[num] + a[num + 1])/2
    else:
        median_num = a[num]
    return median_num

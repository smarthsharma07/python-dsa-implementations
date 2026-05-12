def quick_sort(lst):
    if len(lst)<=1:
        return lst[:]
    pivot=lst[-1]
    less=[]
    greater=[]
    equal=[]
    for x in lst:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)

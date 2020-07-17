from collections import Counter
from collections import OrderedDict
#ordered dict in sorted order(reverse) with frequency count
def SOCountR(mylist):
    return OrderedDict(sorted(Counter(mylist).items(),reverse=True))

def SOCount(mylist):
    return OrderedDict(sorted(Counter(mylist).items()))

#frequency Count
def freq_count(mylist):
    return Counter(mylist)

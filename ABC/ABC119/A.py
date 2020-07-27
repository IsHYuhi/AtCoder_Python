import datetime
date_str = "2019/04/30"
date_formatted = datetime.datetime.strptime(date_str, "%Y/%m/%d")
s = input()
s = datetime.datetime.strptime(s, "%Y/%m/%d")

if s <= date_formatted:
    print('Heisei')
else:
    print('TBD')
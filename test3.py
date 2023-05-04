# import re
# s = "http://github.com/carbonfive/raygun"
# res = re.findall("(^(http.?://))", s)
# print(res)
# test = re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', s).group('name')
# print(test)

def format_duration(seconds):
    words = ["year", "day", "hour", "minute", "second"]

    if not seconds:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]
    print(time)


seconds = 145151
format_duration(seconds)

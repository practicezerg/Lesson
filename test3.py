# import re
# s = "http://github.com/carbonfive/raygun"
# res = re.findall("(^(http.?://))", s)
# print(res)
# test = re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', s).group('name')
# print(test)

data = {'ID': 3195778, 'RegionCode': '36', 'Region': 'Воронежская', 'DistrictCode': '21B04D8B-D97C-4034-AD25-28F64CF387BD', 'District': 'город Воронеж', 'PlaceCode': '5BF5DDFF-6353-4A3D-80C4-6FB27F00C6C1', 'Place': 'г. Воронеж', 'StreetHome': 'ул. Калинина 22 а ', 'ScheduledTimeRemoval': '2023-05-05T17:50:00', 'ScaleShutdown': 'не знаю', 'StatusRequest': 'принято', 'Created': '2023-05-05T12:48:00', 'Modified': '2023-05-05T12:51:53.693', 'RejectionReasonTitle': ''}
print(type(data))
if isinstance(data, dict):
    print("YES")
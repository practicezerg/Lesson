# import keyboard
#
# while True:
#     event = keyboard.read_event()
#     if event.event_type == keyboard.KEY_DOWN:
#         key = event.name
#         print(f'Pressed: {key}')
#         if key == 'q':
#             break
#

def sum_dig_pow(a, b):
    l = []
    for i in range(a, b+1):
        n = 1
        sum = 0
        for x in str(i):
            res = int(x) ** n
            sum += res
            n += 1
        if sum == i:
            l.append(i)
    return l



a = 1
b = 100
res = sum_dig_pow(a, b)
print(res)

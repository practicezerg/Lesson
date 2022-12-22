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

def dig_pow(n, p):
    res = 0
    x = 0
    for i in str(n):
        res = res + int(i)**(p+x)
        x += 1
    print(res)
    print(res/n)
    k = res/n
    print(k)
    if int(res/n):
        return int(k)
    else:
        return -1


n = 3456789
p = 5
res = dig_pow(n, p)
print(res)

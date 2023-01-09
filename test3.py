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



def checkio(food):
    golyb = 1
    n = 2
    res = 0
    while food > golyb:
        food = food - golyb
        res += 1
        if food < golyb:
            return golyb
        golyb = golyb + n

        n +=1
    return res



food = 3
n = checkio(food)
print(n)
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

test = {
    0: ["151", "fdsdfsdf"],
    1: ["151", "fdsdfsdf"],
    2: ["15151", "fdsdfsdf"],
    3: ["231", "fdsdfsdf"],
    4: ["1231", "fdsdfsdf"],
    5: ["114501", "fdsdfsdf"]
}
print(test.keys([0:3]))
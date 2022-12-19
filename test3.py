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

l = ['\t+ CAM 044\tостановка "Улица Куцыгина"\t', '\t+ CAM 060\tостановка "Институт МЧС"\t', '\t+ CAM 077\tостановка "Поликлиника №11"\t', '\t+ CAM 111\tостановка "Улица Куцыгина"\t', '\t+ CAM 321\tостановка "Улица Куцыгина"\t']
for i in l:
    print(i)
import requests
from PIL import Image
import pytesseract

capcha_url = "https://***.store/captcha/_"

#функция для скачивания картинки
def download_captcha_image():
    response = requests.get(capcha_url)
    img_bytes = response.content  #файл в виде байтовой строки
    fname = "captcha.png"   #куда сохранять картинку
    with open(fname, "wb") as f:
        f.write(img_bytes)  #байты в картинку

#    читаем картинку на диске с помощью Pillow
    img = Image.open(fname)
    return img
img = download_captcha_image()


pixels = img.load()   # превращаем картинку в редактируемый массив пикселей
pixels[25.10]  # пиксель по этому адресу x=25 y = 10 (красный 0....255, зеленый 0....255, синий 0....255)
bad_colors = [(64,64,64), (0,0,255)]
for y in range(img.size[1]):   # перебираем все пиксели картинки
    for x in range(img.size[0]):
        if pixels[x,y] in bad_colors:   # если пиксель в списке на замену
            pixels[x,y] = (255,255,255)   # ставим белый цвет

pytesseract.image_to_string(img)
print(img)

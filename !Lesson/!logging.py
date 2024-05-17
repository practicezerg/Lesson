'''
Для  логирования используется библиотека import logging
перед всем кодом после библиотек прописываем 
logging.basicConfig(filename='parser.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
дальше в коде при необходимости пишем logging.info(текст сообщения) если хотим 
записать сообщение о каком то процессе
или logging.error(текст сообщения) если нужно записать что тут была ошибка
'''

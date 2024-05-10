заметки по Selenium
сылка на SeleniumBase
https://github.com/seleniumbase/SeleniumBase?tab=readme-ov-file

with Driver(headed=False) as driver:
			driver.maximize_window()
			# Устанавливаем максимальное время ожидания в 30 секунд для всех элементов
			driver.implicitly_wait(30)
			# создаем всю информацию котоаря нужна при регистрации


сделать скриншот, иногда помогает при отлове ошибки 
driver.save_screenshot("path_for_file/name_file.png")

выполнение скрипта
driver.execute_script(f"window.scrollBy(0, {pixels_to_scroll});")

передаем страничку в bs для парсинга
soup = BS(driver.page_source, features="html.parser")

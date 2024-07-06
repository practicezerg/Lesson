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





The provided code snippets are method calls in Python, likely part of a Selenium WebDriver script used for automating web browsers. These methods perform various actions on web pages such as navigating, interacting with elements, waiting for conditions, and verifying states. Here's a translation of these method names into Russian:

self.open(url) - Перейти в браузере на указанный URL.
self.type(selector, text) - Обновить поле текстом.
self.click(selector) - Нажать элемент с селектором.
self.click_link(link_text) - Нажать ссылку, содержащую текст.
self.go_back() - Вернуться к предыдущему URL.
self.select_option_by_text(dropdown_selector, option) - Выбрать опцию по тексту в выпадающем списке.
self.hover_and_click(hover_selector, click_selector) - Навести курсор и нажать элемент.
self.drag_and_drop(drag_selector, drop_selector) - Перетащить и отпустить элемент.
self.get_text(selector) - Получить текст элемента.
self.get_current_url() - Получить URL текущей страницы.
self.get_page_source() - Получить HTML текущей страницы.
self.get_attribute(selector, attribute) - Получить атрибут элемента.
self.get_title() - Получить заголовок текущей страницы.
self.switch_to_frame(frame) - Переключиться в контейнер iframe.
self.switch_to_default_content() - Выйти из контейнера iframe.
self.open_new_window() - Открыть новое окно в том же браузере.
self.switch_to_window(window) - Переключиться на окно браузера.
self.switch_to_default_window() - Переключиться на оригинальное окно.
self.get_new_driver(OPTIONS) - Открыть новый драйвер с параметрами OPTIONS.
self.switch_to_driver(driver) - Переключиться на драйвер браузера.
self.switch_to_default_driver() - Переключиться на оригинальный драйвер.
self.wait_for_element(selector) - Подождать, пока элемент станет видимым.
self.is_element_visible(selector) - Проверить видимость элемента.
self.is_text_visible(text, selector) - Проверить видимость текста.
self.sleep(seconds) - Задержка выполнения на заданное количество времени.
self.save_screenshot(name) - Сохранить скриншот в формате .png.
self.assert_element(selector) - Проверить видимость элемента.
self.assert_text(text, selector) - Проверить текст элемента.
self.assert_exact_text(text, selector) - Проверить точное совпадение текста.
self.assert_title(title) - Проверить заголовок веб-страницы.
self.assert_downloaded_file(file) - Проверить, был ли скачан файл.
self.assert_no_404_errors() - Проверить отсутствие разбитых ссылок (404 ошибок).
self.assert_no_js_errors() - Проверить отсутствие JavaScript ошибок.

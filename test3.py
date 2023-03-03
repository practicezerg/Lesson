import time
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
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


#
# def checkio(food):
#     golyb = 1
#     n = 2
#     res = 0
#     while food > golyb:
#         food = food - golyb
#         res += 1
#         if food < golyb:
#             return golyb
#         golyb = golyb + n
#
#         n +=1
#     return res
#
#
#
# food = 3
# n = checkio(food)
# print(n)


# l = ["<div class=\"highlight-count count-text\" data-reactid=\"138\"><strong data-reactid="139">3</strong><!-- react-text: 140 --> <!-- /react-text --><!-- react-text: 141 -->Items<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="144"><strong data-reactid="145">0</strong><!-- react-text: 146 --> <!-- /react-text --><!-- react-text: 147 -->Items on Wish List<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="157"><strong data-reactid="158">1</strong><!-- react-text: 159 --> <!-- /react-text --><!-- react-text: 160 -->Sent Trades<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="163"><strong data-reactid="164">0</strong><!-- react-text: 165 --> <!-- /react-text --><!-- react-text: 166 -->Trades Received<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="169"><strong data-reactid="170">0</strong><!-- react-text: 171 --> <!-- /react-text --><!-- react-text: 172 -->Trades To Rate<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="175"><strong data-reactid="176">0</strong><!-- react-text: 177 --> <!-- /react-text --><!-- react-text: 178 -->Items Locked<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="184"><strong data-reactid="185">2 324</strong><!-- react-text: 186 --> <!-- /react-text --><!-- react-text: 187 -->Available<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="190"><strong data-reactid="191">0</strong><!-- react-text: 192 --> <!-- /react-text --><!-- react-text: 193 -->Badges Earned<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="196"><strong data-reactid="197">0</strong><!-- react-text: 198 --> <!-- /react-text --><!-- react-text: 199 -->Quest Challenges<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="469"><strong data-reactid="470">3</strong><!-- react-text: 471 --> <!-- /react-text --><!-- react-text: 472 -->Items<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="475"><strong data-reactid="476">0</strong><!-- react-text: 477 --> <!-- /react-text --><!-- react-text: 478 -->Items on Wish List<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="488"><strong data-reactid="489">1</strong><!-- react-text: 490 --> <!-- /react-text --><!-- react-text: 491 -->Sent Trades<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="494"><strong data-reactid="495">0</strong><!-- react-text: 496 --> <!-- /react-text --><!-- react-text: 497 -->Trades Received<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="500"><strong data-reactid="501">0</strong><!-- react-text: 502 --> <!-- /react-text --><!-- react-text: 503 -->Trades To Rate<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="506"><strong data-reactid="507">0</strong><!-- react-text: 508 --> <!-- /react-text --><!-- react-text: 509 -->Items Locked<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="515"><strong data-reactid="516">2 324</strong><!-- react-text: 517 --> <!-- /react-text --><!-- react-text: 518 -->Available<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="521"><strong data-reactid="522">0</strong><!-- react-text: 523 --> <!-- /react-text --><!-- react-text: 524 -->Badges Earned<!-- /react-text --></div>, <div class="highlight-count count-text" data-reactid="527"><strong data-reactid="528">0</strong><!-- react-text: 529 --> <!-- /react-text --><!-- react-text: 530 -->Quest Challenges<!-- /react-text --></div>]






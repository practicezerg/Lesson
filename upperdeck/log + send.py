from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# login = "Brown35@gmail.com"
login = "LeonhartX2O7tetej@gmail.com"
# psw = "06Yiy3DJCfpw"
psw = "yzsBWUEV9oSun8K4Sc"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa")
elem1 = driver.find_element(By.XPATH, "//*[@id=\"login-email\"]").send_keys(login)
elem2 = driver.find_element(By.XPATH, "//*[@id=\"login-password\"]").send_keys(psw)
elem3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/form/div[3]/button").click()
time.sleep(5)
elem4 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
time.sleep(5)
elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i").click()
elem6 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/img").click()
time.sleep(5)
elem7 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
elem8 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"submit-trade\"]"))).click()
time.sleep(3)
elem9 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/div/div/div/div[3]/div/button[1]"))).click()
# elem9 = driver.find_element(By., "btn btn-ud-primary btn-confirmation-popup").click
# elem10 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-ud-primary btn-confirmation-popup"))).click

time.sleep(5000)

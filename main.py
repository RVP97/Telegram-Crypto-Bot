from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import re
import requests


CHROMEDRIVER = Service('C:\\Users\\52553\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(service=CHROMEDRIVER)
driver.get('https://ethermine.org/miners/7095ddad31693ea600fc1ac0599221c2ea45d19a/dashboard')
time.sleep(1)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
hash_rate_text = soup.select_one('div.hashrate')
# using regex find text that starts with 'Reported' and ends with '(MH/s)'
hash_rate = float(re.findall(r'(\d+\.\d+)', hash_rate_text.text)[-1])

# send telegram message
telegram_token = ''
chat_id = ''
telegram_endpoint = f'https://api.telegram.org/bot{telegram_token}/sendMessage'

telegram_data = {
    'chat_id': chat_id,
    'text': f'Hash rate: {hash_rate} MH/s'}

if hash_rate < 182:
    requests.post(telegram_endpoint, data=telegram_data)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from secrets import username, password

class FacebookBot():
    def __int__(self):
        options = ChromeOptions()
        # options.add_argument("--headless=new")
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)

    def login(self, username, password):
        url = 'https://www.facebook.com'
        self.driver.get(url)
        time.sleep(2)
        email = self.driver.find_element(By.NAME, "email")
        pswrd = self.driver.find_element(By.NAME, "pass")
        email.send_keys(username)
        time.sleep(1)
        pswrd.send_keys(password)
        time.sleep(3)
        email.submit()
        time.sleep(10)






# driver.get('https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=pfbid034iiCHto4jgYRr8QUakCmLWPSfsYAkccHgjfPBe3KKHpVEtjHJFFG64cnSbGgboVnl&av=100094998467661&eav=AfZBbaDzcpD4JpfZbst6Sv1xr85-4g8TVA-2mHj6ghhZSS3vaBe42E-CpQgC1jvXYXE&paipv=0&ext=1698241965&hash=AeSHVlVqFVFESdcKjt8')
#
# pageContent = driver.page_source
#
# soup = BeautifulSoup(pageContent, 'html.parser')
# # print(soup.prettify())
# names = soup.find_all('div', class_='_4mo')
# for name in names:
#     print(name.text)


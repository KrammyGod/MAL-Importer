'''
Import any amount of anime to myanimelist by giving the links to the anime

By: Mark Xue

Date: May 30, 2021

V1.0
'''

from selenium import webdriver
import time
from settings import LoginCredentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Variable setup
driver = 'driver/chromedriver.exe'
_options = webdriver.ChromeOptions()
# True for headless, False for actual browser
_options.headless = True
# Remove all logging clog
_options.add_argument('log-level=3')
driver = webdriver.Chrome(driver, options=_options)


# Function to click elements
def click(xpath):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()


settings = LoginCredentials()
USER = settings._username
PASS = settings._password

# Start timer
start = datetime.now()
# Login Screen
driver.get('https://myanimelist.net/login.php?from=%2F')

# Login Credentials
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loginUserName')))
element.send_keys(USER)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-password')))
element.send_keys(PASS)

# Login Button
login_btn = driver.find_element_by_xpath('//input[@class=\'inputButton btn-form-submit btn-recaptcha-submit\']')
driver.execute_script('arguments[0].scrollIntoView();', login_btn)
login_btn.click()
time.sleep(1)

total_modified = []
lines_read = 0

completed = True
# Navigate animes
try:
    with open('export.txt', 'r') as export_list:
        for line in export_list:
            text = line.strip()
            if text == '# watched':
                completed = True
                continue
            elif text == '# watching':
                completed = False
                continue
            elif text.startswith('#'):
                continue
            else:
                driver.get(text)
                lines_read += 1

            # Get title of anime, prioirtize english name
            try:
                # English title
                xpath = "//p[@class='title-english title-inherit']"
                element = driver.find_element_by_xpath(xpath)
                title = element.text
            except:
                pass
            try:
                # Default title
                xpath = "//h1[@class='title-name h1_bold_none']/strong"
                element = driver.find_element_by_xpath(xpath)
                title = element.text
            except:
                # Otherwise use link as title
                title = text
            
            try:
                # Try to add to list
                xpath = "//a[@class='btn-user-status-add-list js-form-user-status js-form-user-status-btn  myinfo_addtolist']"
                driver.find_element_by_xpath(xpath).click()
                total_modified.append(title)
            except:
                pass
            
            # Check if anime is already marked as completed
            try:
                xpath = "//div[@class='user-status-block js-user-status-block fn-grey6 clearfix al mt8 po-r']/select[@id='myinfo_status' and @data-class='completed']"
                driver.find_element_by_xpath(xpath).click()
                anime_done = True
            except:
                anime_done = False

            # Mark as completed only if header is '# watched' and not marked as completed
            if completed and not anime_done:
                xpath = "//div[@class='user-status-block js-user-status-block fn-grey6 clearfix al mt8 po-r']/select[@id='myinfo_status']"
                click(xpath)
                xpath += "/option[2]"
                click(xpath)
                if not (title in total_modified):
                    total_modified.append(title)
                time.sleep(1)
except IOError:
    print('Error opening file "export.txt". Please check the file and try again.')


# Close processes
driver.quit()
time_taken = datetime.now() - start
start = start.strftime('%H:%M:%S')
seconds = int(time_taken.total_seconds())
h = seconds // 3600
seconds -= 3600 * h
m = seconds // 60
seconds -= 60 * m
print(f'Process started on {start}, time taken: {h:02}:{m:02}:{seconds:02}.')
print(f'Modified {len(total_modified)}/{lines_read} anime:')
for i in range(len(total_modified)):
    print(f'{i+1}: {total_modified[i]}')

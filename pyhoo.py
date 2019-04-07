import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
import time
import argparse
#import getpass
parser = argparse.ArgumentParser()
parser.add_argument("-e","--email", help="Email id of user", type=str, required=True)
parser.add_argument("-n","--email_number", help="(Optional) Email iumber to begin with; default is 5000", type=int)
parser.add_argument("-i","--iteration", help="(Optional) Number of emails to parse in reverse order; default is 10", type=int)
args = parser.parse_args()
user = args.email
if args.email_number:
    email_number = args.email_number
else:
    email_number = 5000
if args.iteration:
    iteration = args.iteration
else:
    iteration = 10
#future-add cookie check and log to existing account
driver = webdriver.Firefox(executable_path = '/Users/p2730903/Documents/Personal/Python projects/geckodriver')
driver.get("https://login.yahoo.com/")
timeout = 20
#assert "YAHOO!" in driver.title
#add username
elem = driver.find_element_by_id("login-username")
elem.send_keys(user)
elem.send_keys(Keys.RETURN)
#add verification
random = raw_input("Added this to cause delay. Press Enter after you accept the notification on the App")
random = False #sanitizing in case user crafted a malicious input instead of Return key
#driver.close()
elem = driver.find_element_by_name("code")
elem.send_keys(raw_input("Enter Code: "))
elem.send_keys(Keys.RETURN)
#wait for page to load
try:
	WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, 'uh-mail-link')))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()
#click on 'Mail' from yahoo homepage
driver.find_element_by_id("uh-mail-link").click()
time.sleep(5) #waiting to load - is this needed?
#will need a loop here
for i in range(int(iteration)):
    email_number = email_number - 1
    #open tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # You can use (Keys.CONTROL + 't') on other OSs
    try:
        driver.get('https://mail.yahoo.com/d/folders/1/messages/'+str(email_number))
    # Make the tests...

        #driver.find_element_by_xpath("//a[contains(text(), 'Unsubscribe') or contains(text(), 'unsubscribe') or \
        #     contains(text() 'Stop') or contains(text(), 'stop') or contains(text(), 'Click here') or contains(text()\
        #        , 'Click Here') or contains(text(), 'click here') or contains(text(), \
        #        'click Here')]").send_keys(Keys.COMMAND + Keys.RETURN)

        if driver.find_element_by_partial_link_text('Unsubscribe').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "function_for_unsub"
        elif driver.find_element_by_partial_link_text('unsubscribe').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "function_for_unsub"
        elif driver.find_element_by_partial_link_text('Stop').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "func_for_unsub"
        elif driver.find_element_by_partial_link_text('stop').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "func_for_unsub"
        elif driver.find_element_by_partial_link_text('Click here').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "func_for_unsub"
        elif driver.find_element_by_partial_link_text('click here').send_keys(Keys.COMMAND + Keys.RETURN):
            action = "func_for_unsub"

        #try:
        #    driver.find_element_by_xpath()
        #except Exception as e:
        #    print("ERROR while handling subscription- the error is " + str(e))

        #ask if user wants to delete
        del_check = raw_input("Do you want to delete this message? yes/no [no] ")
        if del_check.lower() == "yes":
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Move'])[1]\
            /following::span[3]").click()
        #trying to parse deleted emails will result in issues
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    except Exception as e:
        print("ERROR while accessing email- the error is " + str(e))
    # close the tab
    # (Keys.CONTROL + 'w') on other OSs.
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

driver.close()

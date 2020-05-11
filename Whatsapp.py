"""Python code to send a whatsapp text (input) 
to a Contact (input) 
a certain amount of times (input)  """

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Tells the selenium driver which explorer will be handled
driver = webdriver.Chrome("chromedriver.exe") 

# Tells selenium which website to open. 
# It is in a "try" because driver.get() expects the explorer to output 
# a completion output to know when it has already loaded the website and 
# for some reason (might be version compatibilities) it never worked and 
# brought an error instead which exited the code.
try:
    driver.get("https://web.whatsapp.com/") 
except:
    pass
wait = WebDriverWait(driver, 600) 
  
# Asks user for input to know the destination name (only one), 
# the message to be sent, and the # of times to send it
name = input("Enter name of destination: ")
msg = input("Enter the messsage to be sent:")
count = int(input("How many times?"))

# Since whatsapp asks for a QR scan to open an account in the web browser, 
# the code pauses here for the user to do it and waits for the user to click enter to continue.
input("Enter anything after scanning QR code")    

# Searches for the destination in the contact search box and clicks it.  
buscador = driver.find_element_by_xpath("//div[@contenteditable='true'][@data-tab='3']")
buscador.send_keys(name)
time.sleep(.01)
buscador.send_keys(Keys.ENTER)

# The above code searches for contacts that don't appear in the screen. If the destination 
# can be seen in the screen, you can run the next two lines of code instead to make it faster.
#user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
#user.click()

# Writes in the message box the defined messsages and sends it the defined amount of times.
msg_box = driver.find_element_by_xpath("//div[@contenteditable='true'][@data-tab='1']")

for i in range(count):
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)
    
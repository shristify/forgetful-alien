from setup import *
from messenger import *
#driver=webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    
def assignments():
    pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract'
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--example-flag")
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=82defbda-2b2c-4dff-ae1c-97d41949fcbf&client-request-id=ad3a6952-c5d8-4800-97bb-c9c21c203e21&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=e0394e34-e410-46b3-b60a-0209ec830a26&domain_hint=&sso_reload=true")
    time.sleep(5)
    username = driver.find_element_by_name("loginfmt")
    username.clear()
    username.send_keys("*********") #login ID goes here
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(5)
    password = driver.find_element_by_name("passwd")
    password.clear()
    password.send_keys("******") #password goes here
    time.sleep(5)
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(5)
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(5)
    #driver.find_element_by_link_text("Use the web app instead").click()
    time.sleep(10)
    driver.find_element_by_id("app-bar-66aeee93-507d-479a-a3ef-8f494af43945").click()
    driver.find_element_by_id("app-bar-66aeee93-507d-479a-a3ef-8f494af43945").click()
    time.sleep(100)
    driver.get_screenshot_as_file("ss.png")
    img=cv2.imread('ss.png')
    t=pytesseract.image_to_string(img)
    x=t.index('ous')
    y=t.index('> Completed')
    x=x+3
    os.remove("ss.png")
    text=t[x:y].strip()
    print(text)
    send_mess(text)
    driver.close()
    
def german():    
    message = client.messages.create( 
                          from_=twi,  
                          to=me,
	          body=(one[random.randint(0,len(one)-1)])
                          )
    print(message.sid)
    
schedule.every().day.at('07:00').do(assignments)
schedule.every().day.at('07:15').do(german)


while True:
    schedule.run_pending()
    time.sleep(1)
    

#code snippets tested

#driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
#pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd='./.apt/usr/share/tesseract-ocr/4.00/tessdata'
#TESSDATA_PREFIX = ./.apt/usr/share/tesseract-ocr/4.00/tessdata
#all_spans = driver.find_elements_by_xpath("//div[@class='assignment-card-duedate__27g97']")
#for span in all_spans:
#   print(span,span.text)
#try:
#    driver.find_element_by_class_name("action-button").click()
#except NoSuchElementException:
#    print("hey")
#//div[@class="assignment-card-grid__22fij"]/span
#//span[@class="due-date-alignment__1BKzK"]/span[@class=""]

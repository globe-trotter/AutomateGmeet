import webbrowser
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
opts=Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9222')
driver= webdriver.Chrome(chrome_options=opts)

def openBrowser(start,end,link):
    curtime=time.strftime("%H:%M:%S")
    while(curtime!=start):
        print("wait")
        curtime=time.strftime("%H:%M:%S")
        time.sleep(1)
    if(curtime==start):
        driver.get(link)
        time.sleep(8)
        mute=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div")
        mute.click()
        video=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div")
        video.click()
        #join = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div")))
        join=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
        join.click()
        #/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div
    
    while(curtime!=end):
        curtime=time.strftime("%H:%M:%S")
        print("In meeting")
        time.sleep(1)
    try:
        endMeeting=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div")
        endMeeting.click()
    except:
        close=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div")
        close.click()
    finally:
        endMeeting=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div")
        endMeeting.click()



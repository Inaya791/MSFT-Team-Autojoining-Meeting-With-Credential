#code with using credentials of Teams 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver import ActionChains

# Configure Chrome options
chrome_options = Options()
# Uncomment this for headless mode if needed
# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.notifications": 2
})

# Initialize ChromeDriver service
service = Service(executable_path='./chromedriver.exe')  # Path to your chromedriver

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

def join_teams_meeting(meeting_link):
    try:

        #open Teams logination
        driver.get(Teams_login)
        sleep(3)
        # Enter Email ID to login with your credential
        try:
            Email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]'))
            )
            Email_input.clear()
            Email_input.send_keys("xyz@gmail.com") 
        except Exception as e:
            print("Failed to find or input Email ID. Error:", e)
        # Click on "Next" button
        try:
            next_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input'))
            )
            next_button.click()
        except Exception as e:
            print("Failed to find or click 'Next' button. Error:", e)
        # Enter password  to login with your credential
        try:
            Email_password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input'))
            )
            Email_password_input.clear()
            Email_password_input.send_keys("@@@@@")  
        except Exception as e:
            print("Failed to find or input password. Error:", e)
        # Click on "sign in" button
        try:
            sign_in_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input'))
            )
            sign_in_button.click()
        except Exception as e:
            print("Failed to find or click 'sign in' button. Error:", e)
        sleep(5)#authentication form will begin here 
        # Click on "Stay sign in form submission" button
        try:
            stay_sign_in_no_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input'))
            )
            stay_sign_in_no_button.click()
        except Exception as e:
            print("Failed to find or click ' stay sign in no ' button. Error:", e)
        sleep(10)#to navigate to diffrent tab to join meeting

        # Open the Teams meeting link
        driver.get(meeting_link)
        sleep(5)  # Wait for the page to load
        updated_meeting_link = driver.current_url
        print(f"Extracted updated meeting link")

        # Open the new meeting link in a new tab
        driver.execute_script("window.open('');")  # Open a new blank tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab

        # Load the extracted meeting link in the new tab
        driver.get(updated_meeting_link)
        print(f"Opening the extracted meeting link in a new tab")

        # Click on "Continue on this browser"
        try:
            continue_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/button[1]/div/h3'))
            )
            continue_button.click()
            print("Clicked 'Continue on this browser'")
        except Exception as e:
            print("Failed to find or click 'Continue on this browser' button. Error:", e)

        # Click on "Continue without audio or video" /html/body/div[6]/div/div[2]/div/div[1]/div/button #dialog-content-1 > div > button /html/body/div[7]/div/div[2]/div/div[1]/div/button
        try:
            no_audio_video_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div/button'))
            )
            no_audio_video_button.click()
            print("Clicked 'Continue without audio or video'")
        except Exception as e:
            print("Failed to find or click 'Continue without audio or video' button. Error:", e)
        
        # Click on "Join now" button /html/body/div[1]/div/div/div/div[6]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[2] #prejoin-join-button
        try:
            join_now_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[6]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[2]"))
            )
            join_now_button.click()
            print("Clicked 'Join Now button'")
        except Exception as e:
            print("Failed to find or click 'Join now' button. Error:", e)
        # Click on "Chat button" button  /html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div[1]/button
        try:
            chat_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div[1]/button'))
            )
            chat_button.click()
            print("Clicked 'Chat button'")
        except Exception as e:
            print("Failed to find or click 'Chat' button. Error:", e)
        #Chat Interface with welcome note by NAIRA /html/body/div[1]/div/div/div/div[5]/div/div/div/div/div[4]/div/div[3]/div[2]/div/div[2]/div/div/p
        try:
            type_a_message_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[7]/div/div/div/div/div[4]/div/div[3]/div[2]/div/div[2]/div/div'))
            )
            type_a_message_input.click()  # Focus on the input box
            type_a_message_input.send_keys("Hi! I'm N.AI.R.A,Your Intelligent Companion")
            print("Typed message 'Hi! I'm NAIRA,I will record and Transcribe this meeting.'")
        except Exception as e:
            print("Failed to find or type a message. Error:", e)
        
        #Click on the "Send" button /html/body/div[1]/div/div/div/div[5]/div/div/div/div/div[4]/div/div[3]/div[3]/div[3]/div[2]/button
        try:
            send_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[7]/div/div/div/div/div[4]/div/div[3]/div[3]/div[3]/div[2]/button'))
            )
            send_button.click()
            print("Message sent")
        except Exception as e:
            print("Failed to find or click 'Send' button. Error:", e)

        # Click on "three dots" button /html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div[8]/button
        try:
            three_dots_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div[8]/button'))
            )
            three_dots_button.click()
        except Exception as e:
            print("Failed to find or click 'three dots' button. Error:", e)
        sleep(1)
        # Click on "Recording and Transcription" button   /html/body/div[27]/div/div/div[1]/span[2]/span
        try:
            record_transcript_button = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='RecordingMenuControl-id']"))
            )
            print("Located 'Recording and Transcription' button.")
    
            # Hover or click on the "Recording and Transcription" button
            actions = ActionChains(driver)
            actions.move_to_element(record_transcript_button).perform()
            sleep(2)  # Allow the hover effect to take place
            # record_transcript_button.click()
            # print("Hovered over the 'Recording and Transcription' button.") 
        except Exception as e:
            print("Failed to find or click 'Recording and Transcription' button. Error:", e)
        # Click on "Start Recording" button /html/body/div[25]/div/div/div[1]
        try:
            start_record_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='recording-button']"))
            )
            start_record_button.click()
            print("Started recording  button.")
        except Exception as e:
            print("Failed to find or click 'Start Recording' button. Error:", e)
        sleep(40)
       
    except Exception as e:
        print("Error in the meeting process.")
        traceback.print_exc()

    finally:
        driver.quit()

if __name__ == '__main__':
    Teams_login="https://go.microsoft.com/fwlink/p/?linkid=873020"
    # Replace with your actual Teams meeting link
    meeting_link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting"
    join_teams_meeting(meeting_link)

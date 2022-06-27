#TS002 Testing Login page

#importing essential modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# main function this will be executed first
def main():
    #chrome driver object with driver manager for executable path
    driver = webdriver.Chrome(ChromeDriverManager().install())  
    # list of user and password every username is password    
    Testusers=["HELLO","HeLlO","hello","HarryPotter","1234","1234567","Hello123","hii12","IN@11","!@#$%","in@11"]
    c=1
    #loop for checking every username and password
    for i in Testusers:
        print(f"\nTest case {c}")
        TS002(driver,i,i)       # call to function TS001 for testing register page with given test case
        c=c+1

    check_session(driver,"hello","hello")           # check_session function called to check if session is saved or not in browser


    # capturing server resource failed pop up alert occurs after 120 seconds 
    try:
        print('''
        --------------------------------------------
          Waiting for server resource failed alert
                        120 seconds\n ''')
        driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/")
        WebDriverWait(driver=driver,timeout=122).until(EC.alert_is_present()," ")
        alert=driver.switch_to.alert                #switching to alert to handle it
        print(f"\nPop up message Server replied {alert.text} \n\n")
        alert.accept()
    except:
        pass




# function for testing login page with given username and password 
def TS002(driver,username,password):
    driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/")
    result_user=username_input_checker(driver,username)         # call to a function for checking Username field's response
    result_pwd=password_input_checker(driver,password)      # call to a function for checking Password field's response

    # checking if username and password is entered correctly or not
    if(result_user==True and result_pwd==True):
       
        create_btn=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
        create_btn.click()       #create button clicked
        time.sleep(5)
        try:
            #checking is any pop up alert is shown or not
            WebDriverWait(driver,5).until(EC.alert_is_present)
            alert=driver.switch_to.alert
            print("\nPop up message :- "+alert.text)
            alert.accept()
            print(f"\nTest case Failed\nServer replied {alert.text} \n\n")

        except:
            #confirming successfull login 
            c_url= driver.current_url
            if c_url=="https://testing-assessment-foh15kew9-edvora.vercel.app/s":
                print("Test case Success Account logged in successfully")
            else:
                # console output of unsuccessfull login
                print("\nuser is unable to login as Account was not created(doesn't exit) ")
                if((not username.islower()) and (not (username.isalnum() or password.isalnum()))):
                    print("because username contains uppercase characters and username and password contains non-alphanumeric characters")
                else:
                    # as we cannot create account with Uppercase characters in username 
                    if not username.islower():
                        print("because username contains uppercase characters")
                    # as we cannot create account with non-alphanumeric characters in username and password
                    if not (username.isalnum() or password.isalnum()):
                        print("because username and password contains non-alphanumeric characters")
        
    else:
        print("\nTest case Failed user not able to login with given username and password as account doesn't exist \n")
            
            


# function for checking Username field's response to a given value
# Evalue is expected value that is given by user
def username_input_checker(driver,Evalue):           
    print("\nChecking Username input Field for given value")
    usrnam_field=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input')
    usrnam_field.send_keys(Evalue)

     #Avalue (value of attribute "value" of input tag) is value which is found in input box after typing
    Avalue=usrnam_field.get_attribute("value")      
    #checking result
    if(Evalue==Avalue):
        print("\nTest case is success \n Value given is :- "+Evalue)
        return True
    else:
        print(f"\nTest case failed \n Expected Value is :- {Evalue} \n Value found in input box is :- {Avalue}")
        print("unable to write more than 5 characters in box")
        return False

# function for checking Password field's response to a given value
# Evalue is expected value that is given by user
def password_input_checker(driver,Evalue):            
    print("\nChecking Password input Field for given value")
    pass_field=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input')
    pass_field.send_keys(Evalue)

    #Avalue (value of attribute "value" of input tag) is value which is found in input box after typing
    Avalue=pass_field.get_attribute("value")   
    #checking and returning result  
    if(Evalue==Avalue):
        print(f"\nTest case is success \n Value given is :- {Evalue}")
        return True
    else:
        print(f"\nTest case failed \n Expected Value is :- {Evalue} \n Value found in input box is :- {Avalue}")
        print("unable to write more than 5 characters in box")
        return False

# checking if logged in session is saved or not in browser by refreshing the page 
def check_session(driver,username,password):
    print("\n\nChecking if session of logged user is saved or not\nlogging in with username : hello \n         password : hello")
    driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/")
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button').click()
    time.sleep(5)
    print("Account logged in Successfully")
    # checking session with username value as it is not editable on details page and unique for everyone
    try:
        current_user1=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/input').get_attribute("value")
        driver.refresh()
        current_user2=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/input').get_attribute("value")
        if(current_user2!=current_user1):
            print("\nSession is not saved credentials are reset to null after Refresh")
        else:
            print("\nSession is saved same user is logged in ")
    except:
        pass


# calling main function to start testing
if __name__ == "__main__":
    main()
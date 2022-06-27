#TS001 Testing register page

#importing essential modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
        TS001(driver,i,i)       # call to function TS001 for testing register page with given test case
        c=c+1

# function for testing username and password for registeration
def TS001(driver,user,password):
    # opening register page
    driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/r")
    result_user=username_input_checker(driver,user)         # call to a function for checking Username field's response
    result_pwd=password_input_checker(driver,password)      # call to a function for checking Password field's response

    # If there is no changement in value of username and password than create button is clicked
    if(result_user==True and result_pwd==True):
        create_btn=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
        create_btn.click()      #create button clicked
        time.sleep(5)

        # checking alert is present or not
        if EC.alert_is_present:
            alert=driver.switch_to.alert
            #confirming the alert's message
            if 'Account sucessfully created' in alert.text :
                print("\nPop up message :- "+alert.text)
                alert.accept()
                print(f"\nTest case success\nAccount created successfully with \nUsername:{user}\nPassword:{password}\n\n")
            else:
                print("\n\nPop up message :- "+alert.text)
                alert.accept()
                print("\nAccount creation test case failed!!\n")
    else:
        if result_user==False:
            print("\n Unable to Enter Username's Given Value")
        if result_pwd==False:
            print("\n Unable to Enter Password's Given Value")
        print("\nAccount creation test case failed!!\n")

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
        if(len(Evalue)>5):
            print("unable to type more than 5 character in input box")
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
        if(len(Evalue)>5):
            print("unable to type more than 5 character in input box")
        return False

# calling main function to start testing
if __name__ == "__main__":
    main()
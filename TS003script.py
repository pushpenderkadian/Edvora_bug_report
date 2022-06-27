#TS003 Testing Details page

#importing essential modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time,datetime
        

# main function this will be executed first
def main():
    #chrome driver object with driver manager for executable path
    driver = webdriver.Chrome(ChromeDriverManager().install()) 

    #setting browser's size and position according to current xpath for elements
    driver.set_window_position(0, 0)
    driver.set_window_size(400, 768)
    
    # user name and password for details
    user='hello'
    password='hello'
    #test case values for details
    names=['ABC XYZ','abcxyz','Abc','ABC123','Abc@123','!@@#$#@']
    mobiles=["1293823422","sdadwewdx","csddew12132","ABC1234","jdh@!1231","@#%#$%$"]
    dobs=['2020-02-11','2000-10-02','1999-01-01',"1923-12-28",'1800-11-01','2000-02-02']
    genders=['male','female','other','transgender','not want to disclose','none']
    addresses=['andhri east','h no. 123,sajd,ds','12/21,hcjds','!@sdsf@#','21324','099823']
    passwords=['hii','HoLa','ABCZTY','in@22','In@25','!@#$%&']

    # call to function TS003 for testing of updation of all info in profile page with given test case
    TS003(driver,user,password,names,mobiles,dobs,genders,addresses,passwords)


#function for testing profile page
def TS003(driver,user,password,names,mobiles,dobs,genders,addresses,passwords):
    pwd=password
    for i in range(0,len(names)):
        print(f"\n\nTest case {i+1}\n")
        print(f'''
-----------------------------------------------
Test Updating values in Personal Info Section
Full Name:{names[i]}
Mobile number:{mobiles[i]}
Date of Birth:{dobs[i]}
Gender:{genders[i]}
Address:{addresses[i]}
        ''')

        # calling function for testing personal info's updation on profile page 
        try:
            edit_profile(driver,user,pwd,names[i],mobiles[i],dobs[i],genders[i],addresses[i])
        except Exception as e:
            print(e)
        print(f'''
-----------------------------------------------
Test Changing password in Security section
Older Password:{pwd}
New Password:{passwords[i]}
        ''')

        # calling function for testing password updation on profile page
        try:
            edit_password(driver,user,pwd,passwords[i])
        except Exception as e:
            print(e)
        pwd=passwords[i]

# function for logging into account from homepage
def login(driver,username,password):
    driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/")
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button').click()
    time.sleep(8)
    
    #checking successfull login or not
    if(driver.current_url=="https://testing-assessment-foh15kew9-edvora.vercel.app/s"):
        print("\nLogin Success\n")
    else:
        print("\nLogin failed\n")


# function for testing profile updation
def edit_profile(driver,username,password,fname,mobile,db,gender,address):
    # login function called for logging into account to edit details
    login(driver,username,password)
    time.sleep(5)
    # clicking on edit button
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[2]/button').click()
    time.sleep(2)                        
    #chnging value for full name field
    Fname = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/input')
    for i in range(0,len(Fname.get_attribute("value"))):
        Fname.send_keys(Keys.BACKSPACE)
    Fname.send_keys(fname)

    #changing value for Mobile number field
    Mobile = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/input')
    for i in range(0,len(Mobile.get_attribute("value"))):
        Mobile.send_keys(Keys.BACKSPACE)
    Mobile.send_keys(mobile)

    # changing value for Date of Birth field
    Dob=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input')
    format = '%Y-%m-%d'
    dat = datetime.datetime.strptime(db, format).date()
    dob=str(dat).split('-')

    #configuration of date typing according to the field
    Dob.send_keys(int(dob[1]))
    if(int(dob[2])<10):  
        Dob.send_keys(int(dob[2]),Keys.ARROW_RIGHT)
    else:
        Dob.send_keys(int(dob[2]))
    Dob.send_keys(int(dob[0]))

    #changing value for gender field
    Gender=Select(driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/select'))
    try:
         Gender.select_by_value(gender)
    except:
        pass

    #changing value for Address Field
    Address=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/input')
    for i in range(0,len(Address.get_attribute("value"))):
        Address.send_keys(Keys.BACKSPACE)
    Address.send_keys(address)

    # clicking save button after all changements
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[2]/button[2]').click()

    time.sleep(5)

    #confirming success by redirection
    if( driver.current_url=="https://manike.com/"):
        print("\nValues Updated Successfully\n\n\nVerifing Details ")

    time.sleep(2)
    # calling login function for logging again into account for confirmation of values
    login(driver,username,password)
    time.sleep(7)

    #checking value of Full name field
    Fname = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/input')
    if(Fname.get_attribute("value")==fname):
        if(not Fname.get_attribute("value").isalpha()):
            print("(Error must be there on webpage as only alphabets are considered as Name)")
        print("\nFull name changed successfully\n")
    else:
        print("\nTest case failed for Full Name change is not saved in server's database correctly\n")
        

    #checking value of Mobile number field
    Mobile = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/input')
    if(Mobile.get_attribute("value")==mobile):
        if(not Mobile.get_attribute("value").isnumeric()):
            print("(Error must be there on webpage as only numeric values and +( for country code) should be there in Mobile number)")
        print("\nMobile number changed successfully\n")
    else:
        print("\nTest case failed Mobile number change is not saved in server's database correctly\n")

    #checking value of Date of birth field
    Dob=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input')
    if(Dob.get_attribute("value")==db):
        print("\nDate of birth changed successfully\n")
    else:
        print("\nTest case failed Date of birth change is not saved in server's database correctly\n")
    
    #checking value of gender field
    Gender=Select(driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/select'))
    if(Gender.first_selected_option.get_attribute("value")==gender):
        print("\nGender changed successfully\n")
    else:
        if(gender not in ["male","female","other"]):
            print("\nTest Case failed due to Wrong gender input \n Value is not changed")
        else:
            print("\nTest case failed Gender change is not saved in server's database correctly\n")
    

    # checking value of address field
    Address=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/input')
    if(Address.get_attribute("value")==address):
        print("\nAddress changed successfully\n")
    else:
        print("\nTest case failed Address change is not saved in server's database correctly\n")


#function for testing of Password field in Security section of profile page
def edit_password(driver,username,password,new_password):

    #logging into account 
    login(driver,username,password)
    time.sleep(2)
    #clicking on edit button
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div[2]/button').click()
    
    # passing new password into the field
    pwd=driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div[1]/div/div/div/div/input')
    pwd.send_keys(new_password)
    
    # clicking on save button
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div[2]/button[2]').click()
    time.sleep(5)

    # confirm saved success by checking url after redirection
    if( driver.current_url=="https://manike.com/"):
        print("Password changed successfully ")
    else:
        try:
            driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div[2]/button[2]')
            print("unable to save password")
        except:
            pass

    #logging into account using new password
    login(driver,username,new_password)
    time.sleep(3)
    if(driver.current_url=="https://testing-assessment-foh15kew9-edvora.vercel.app/s"):
        print("Password verified successfully\n\n")
    
    else:
        print("\nTest case failed Password change is not saved in server's database correctly\n\n")

    
# calling main function to start testing
if __name__ == "__main__":
    main()

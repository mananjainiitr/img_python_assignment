from typing import Text
import mysql.connector
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 

conn = mysql.connector.connect(user='manan', password='#Manan#2020#', host='localhost',database='user',auth_plugin = "mysql_native_password")

cursor = conn.cursor(buffered = True)
user = ""
def checkusername(username):
    mycursor = conn.cursor()
    query = "SELECT username FROM user WHERE username = '"+username+"'"
    
    mycursor.execute(query)
    result = mycursor.fetchall()
    if(result!=[]):
        
        check(username)
        return result[0]

    else:
        return "Error data not found"
def decoder(func,username):
    return func(username)
def check(username):
    mycursor = conn.cursor()
    query = "SELECT * FROM scrap WHERE userid = '"+username+"'"
    
    mycursor.execute(query)
    result = mycursor.fetchall()
    if(result!=[]):
        objuserid = result[0][0]
        objname = result[0][1]
        objcity = result[0][3]
        objwork = result[0][2]
        objfav = result[0][4]
        obj1 = Person(objname)
        obj1.show(objname,objcity,objwork,objfav)

    else:
        scrap(username)
class Person:
    name = ""
    work =[]
    city = ""
    favouraites = {}
    def __init__(self,name,work = [],city = "Roorkee"):
        self.name = name
        self.work = work
        self.city = city
    def show(self,name,city,work,favouraites):
        self.name = name
        self.work = work
        self.city = city
        self.favouraites = favouraites
        if self.city == "":
            self.city = "roorkee"
        
            
        if self.name == "" or self.work == []:
            print("Error insufficient data")
        else :
            if self.city == name:
                self.city = "Roorkee"
            print("my name is "+self.name)
            print("my work is ")
            print(self.work)
            print("my city is ")
            print(self.city)
            print("favouraites are ")
            print(self.favouraites)
work = []
name = ""
like = {}
city = ""

def scrap(username):
    usr=input("enter phone no.")
    pwd=input("password")
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://m.facebook.com/")
    print ("Opened facebook")
    sleep(1)
    # eng = driver.find_element_by_id('"locale-selector"]/div/div[1]/div[3]/span/a')
    # eng.click()
    # sleep(1)
    username_box = driver.find_element_by_id('m_login_email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(5)
    password_box = driver.find_element_by_id('m_login_password')
    password_box.send_keys(pwd)
    print ("Password entered")
    
    login_box = driver.find_element_by_id('login_password_step_element')
    print(login_box)
    login_box.click()
    print(login_box)

    sleep(10)
    con_box = driver.find_element_by_class_name('_2pii')
    print(login_box)
    con_box.click()
    
    driver.get("https://m.facebook.com/"+username+"/about/")

    sleep(10)
    name = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[3]/a').text
    city = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div/header/h4[1]').text
    
    
    print(name)
    print(city)
    sleep(5)
    
    i = 0
    x = 1
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    workcount = len(driver.find_elements(By.XPATH,'//*[@id="work"]/div/*'))
    print(work)
 
    while(x<=workcount):
        work.append(driver.find_element(By.XPATH,'//*[@id="work"]/div/div['+str(x)+']/div/div/div[1]/span').text)
        x = x+1


    print(str(work))
    print(1)
    sleep(3)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    print(workcount)
    sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(3)
    
    likecount = len(driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[12]/div/div/div/div/div/div/div/*'))
    print(likecount)
    y = 1
    while(y<=likecount):
        like[y] = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[12]/div/div/div/div/div/div/div/div['+str(y)+']/div/span').text
        y = y+1

    print(like)
    
    print ("Done")

    
    driver.quit()
    obj1 = Person(name)
    obj1.show(name,city,work,like)
    mycursor = conn.cursor()
    workstr = str(work)
    newwork = workstr.replace("'","")
    newwork = newwork.replace(",","  ")
    likestr = str(like)
    newlike = likestr.replace("'","")
    newlike = newlike.replace(",","  ")
    newlike = newlike.replace("{","")
    newlike = newlike.replace("}","")
    query = "INSERT INTO scrap (userid,name,work,city,favouraites) VALUES (\'"+username+"\',\'"+name+"\',\'"+newwork+"\',\'"+city+"\',\'"+newlike+"\');"
    # connn = mysql.connector.connect(user='manan', password='#Manan#2020#', host='localhost',database='user',auth_plugin = "mysql_native_password")
    # cursor = connn.cursor(buffered = True)
    mycursor = conn.cursor()
    mycursor.execute(query)
    conn.commit()
    print(query)
    print("Finished")
    
        

    

print(decoder(checkusername,"ritvik.jain.52206"))

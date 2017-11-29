import xlrd
import tkinter
from tkinter import *
from tkinter import ttk
import easygui
import random
root=tkinter.Tk() #生成root主窗口 
root.geometry("500x500")#指定主框体大小；
root.title("58挂靠网")
Label(root, text='自动发帖机', font=('Arial', 20)).grid()
frame=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame.grid(row=2,column=0,sticky=W)
frame1.grid(row=12,column=0,sticky=W)
frame2.grid(row=22,column=0,sticky=W)
v_user = StringVar()
v_password = StringVar()
row_index=0
stop=0
Label(frame,text='账号：',height=2).grid(row=row_index,column=0,sticky=W)

def show_msg(*args):  
    print(PhoneNumber.get())
name1 = StringVar()
PhoneNumber = ttk.Combobox(frame,width=14, textvariable=name1)  
PhoneNumber["values"] = ("17725152076",
                     "18575518096",
                     "18902846703",
                     "15338709591",
                     "13113647183",
                     "13022076564"
)  
PhoneNumber["state"] = "readonly"    
PhoneNumber.current(0)    
PhoneNumber.bind("<<ComboboxSelected>>", show_msg)    
PhoneNumber.grid(row=0,column=1,sticky=W)
row_index=row_index+1
Label(frame,text='密码：').grid(row=row_index,column=0,sticky=W)
Entry(frame,width=13,textvariable=v_password,validate='key').grid(row=row_index,column=1,sticky=W)
row_index=row_index+1
v_fre=IntVar()
start=IntVar()
v_fre.set(10)
start.set(1)
Label(frame1,text='发帖频率',fg = 'red',bg = 'white').grid(row=0,column=0,padx=1,sticky=W)
Entry(frame1,width=8,textvariable=v_fre,validate='key').grid(row=0,column=1,sticky=W)
Label(frame1,text='秒').grid(row=0,column=2,sticky=W)
Entry(frame1,width=8,textvariable=start,validate='key').grid(row=2,column=1,sticky=W)
def calc(): 
    from selenium import webdriver
    from time import sleep
    # 引入 Keys 模块
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.select import Select
    driver = webdriver.Chrome()
    driver.get("http://passport.58guakao.com/User/login")
    elem_user = driver.find_element_by_id("phone")
    #elem_user.send_keys("13322991484")
    elem_user.send_keys(PhoneNumber.get())
    elem_pwd = driver.find_element_by_id("User_pwd")
    elem_pwd.send_keys("ljx1234")
    #elem_pwd.send_keys("zhiyi.6688")
    elem_pwd.send_keys(Keys.RETURN)
    sleep(2)
    data=xlrd.open_workbook("58.xlsx")
    table=data.sheets()[0]
    nrows=table.nrows
    print(nrows)
	#sleep(2)
    for index in range(start.get()-1,nrows):
    	table.row_values(1)
    	x=table.row_values(index)
    	#pos=x[3].index('+')
    	print(x[3])
    	#x1=x[3][0:pos]
    	#x2=x[3][pos+1:]
    	driver.get("http://post.58guakao.com/index/subject?etype=5")
    	driver.find_element_by_link_text(x[3]).click()
    	sleep(1) 
    	driver.find_element_by_link_text(x[4]).click()  	
	
               
    	fa_item=driver.find_element_by_id("title");
    	fa_item.send_keys(x[0]);
    	s=Select(driver.find_element_by_id("province"))
    	s.select_by_visible_text(x[2])
        
    	driver.find_element_by_xpath('//input[@value="3"]').send_keys(Keys.SPACE)  # send space
    	sleep(1)
    	driver.find_element_by_xpath('//input[@value="3"]').click()  # click
   
    	fa_content=driver.find_element_by_name("content");
    	fa_content.send_keys(x[1]);#内容随机
    	driver.find_element_by_id("publishsubmit").click()
    	sleep(v_fre.get())
     
    driver.quit()
def stop_calc(): 
    stop=1
Button(root,text='发帖',command=calc).grid(row=23,column=0,pady =40)


root.mainloop() #进入消息循环（必需组件）
# -*- coding: cp1252 -*-
'''
Created on May 15, 2016

@author: RizDesktop
'''

import sys
import os
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import inspect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#Ver1.0
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utilities import CommonUtil
from selenium.webdriver.support import expected_conditions as EC

global WebDriver_Wait 
WebDriver_Wait = 20
global WebDriver_Wait_Short
WebDriver_Wait_Short = 10

#if local_run is True, no logging will be recorded to the web server.  Only local print will be displayed
local_run = True
#local_run = False

def BrowserSelection(browser):
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        sBrowser.close()
    except:
        True
    global sBrowser
    try:
        browser = browser.lower()
        if "chrome" in browser:
            sBrowser = webdriver.Chrome()
            sBrowser.implicitly_wait(WebDriver_Wait)
            sBrowser.maximize_window()
            CommonUtil.ExecLog(sModuleInfo, "Started Chrome Browser", 1, local_run)
            return "passed"
        elif browser == 'firefox':
            sBrowser = webdriver.Firefox()
            sBrowser.implicitly_wait(WebDriver_Wait)
            sBrowser.maximize_window()
            CommonUtil.ExecLog(sModuleInfo, "Started Firefox Browser", 1, local_run)
            return "passed"
        elif "ie" in browser:
            sBrowser = webdriver.Ie()
            sBrowser.implicitly_wait(WebDriver_Wait)
            sBrowser.maximize_window()
            CommonUtil.ExecLog(sModuleInfo, "Started Internet Explorer Browser", 1, local_run)
            return "passed"
        
        elif "safari" in browser:
            os.environ["SELENIUM_SERVER_JAR"] = os.sys.prefix + os.sep + "Scripts" + os.sep + "selenium-server-standalone-2.45.0.jar"
            sBrowser = webdriver.Safari()
            sBrowser.implicitly_wait(WebDriver_Wait)
            sBrowser.maximize_window()
            CommonUtil.ExecLog(sModuleInfo, "Started Safari Browser", 1, local_run)
            return "passed"
    
        else:
            CommonUtil.ExecLog(sModuleInfo, "You did not select a valid browser: %s" % browser, 3,local_run)
            return "failed"
        #time.sleep(3)
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to start WebDriver. %s"%Error_Detail, 3,local_run)
        return "failed"

def OpenLink(link, page_title=False):
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        sBrowser.get(link)
        sBrowser.implicitly_wait(WebDriver_Wait)
        CommonUtil.ExecLog(sModuleInfo, "Successfully opened your link: %s" % link, 1,local_run)
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        if page_title != False:
            assert page_title in sBrowser.title
        #time.sleep(3)
        return "passed"
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "failed to open your link: %s. Error:%s" %(link, Error_Detail), 3,local_run)
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        return "failed"

def Login(user_name,password,logged_name):
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        Click_Element_By_Name("Log in")
        Set_Text_Field_Value_By_ID("username",user_name)
        Set_Text_Field_Value_By_ID("password",password)
        Click_Element_By_ID ("loginbtn")
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Successfully logged in", 1, local_run)
        element_login = WebDriverWait(sBrowser, WebDriver_Wait).until(EC.presence_of_element_located((By.XPATH, "//*[@title='View profile']")))
        if (WebDriverWait(element_login, WebDriver_Wait).until(lambda driver : element_login.text)) == logged_name:
            CommonUtil.ExecLog(sModuleInfo, "Verified that logged in as: %s"%logged_name, 1,local_run)
            return "passed"
        else:
            CommonUtil.ExecLog(sModuleInfo, "Log in failed for user: %s"%logged_name, 3,local_run)
            return "failed"
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to login.  %s"%Error_Detail, 3,local_run)
        return "failed"

           
def Click_By_Parameter_And_Value(parameter,value, parent=False):
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Locating your element...", 1, local_run)
        if isinstance(parent, (bool)) == True:
            Element = WebDriverWait(sBrowser, WebDriver_Wait).until(EC.presence_of_element_located((By.XPATH, "//*[@%s='%s']"%(parameter,value))))
        else:
            Element = WebDriverWait(parent, WebDriver_Wait).until(EC.presence_of_element_located((By.XPATH, "//*[@%s='%s']"%(parameter,value))))
        CommonUtil.ExecLog(sModuleInfo, "Found element and clicking..", 1, local_run)
        Element.click()
        CommonUtil.ExecLog(sModuleInfo, "Successfully clicked by %s and %s"%(parameter,value), 1,local_run)
        return "passed" 
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to locate element to click.  Parameter: %s & Value: %s  Error: %s"%(parameter,value,Error_Detail), 3,local_run)
        return "failed"
    
def Click_Element_By_Name(_name,parent=False):
    '''
    Use this function only if you are sure that there wont be any conflicting Name.
    If possible use Click_Element_By_ID
    
    '''
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        #Find all elements containing the name
        CommonUtil.ExecLog(sModuleInfo, "Trying to find element by name: %s"%_name, 1,local_run)
        if isinstance(parent, (bool)) == True:
            allElements = WebDriverWait(sBrowser, WebDriver_Wait).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='%s']"%_name)))        
        else:
            allElements = WebDriverWait(parent, WebDriver_Wait).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='%s']"%_name)))
        if allElements == []:        
            CommonUtil.ExecLog(sModuleInfo, "Could not find your element by name: %s"%_name, 3,local_run)
            return "failed"
        else:
            if len(allElements) > 1:
                CommonUtil.ExecLog(sModuleInfo, "Found more than one element and will use the first one.  ** if fails, try providing parent element or try by ID** ", 2, local_run)
            for each in allElements:
                if (WebDriverWait(each, WebDriver_Wait).until(lambda driver : each.is_displayed())) == True:
                    Element = each
                    CommonUtil.ExecLog(sModuleInfo, "Found your element by name: %s.  Using the first element found to click"%_name, 1,local_run)
                    break   
        #Now we simply click it
        Element.click()
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Successfully clicked your element: %s"%_name, 1,local_run)
        return "passed"
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to expand menu: %s.   Error: %s"%(_name,Error_Detail), 3,local_run)
        return "failed"    
 
 

def Click_Element_By_ID(_id):    
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Trying to find element by ID: %s"%_id, 1,local_run)
        try:
            Element = WebDriverWait(sBrowser, WebDriver_Wait).until(EC.presence_of_element_located((By.ID, _id)))
        except:
            CommonUtil.ExecLog(sModuleInfo, "Could not find your element by name or ID: %s"%_id, 3,local_run)
            return "failed"
        #Now we simply click it
        Element.click()
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Successfully clicked your element: %s"%_id, 1,local_run)
        return "passed"
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to click element by ID: %s.  Error: %s"%(_id,Error_Detail), 3,local_run)
        return "failed"    

def Click_Element_By_Custome_Field_Value(field,value):
    sModuleInfo = inspect.stack()[0][3] + " : " + inspect.getmoduleinfo(__file__).name
    try:
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Trying to find element by field: %s and value: %s"%(field,value), 1,local_run)
        Element = WebDriverWait(sBrowser, WebDriver_Wait).until(EC.presence_of_element_located((By.XPATH, "//input[@%s='%s']"%(field,value))))
        #Now we simply click it
        Element.click()
        CommonUtil.TakeScreenShot(sModuleInfo, local_run)
        CommonUtil.ExecLog(sModuleInfo, "Successfully clicked your element by field: %s and value: %s"%(field,value), 1,local_run)
        return "passed"

    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()        
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Error_Detail = ((str(exc_type).replace("type ", "Error Type: ")) + ";" +  "Error Message: " + str(exc_obj) +";" + "File Name: " + fname + ";" + "Line: "+ str(exc_tb.tb_lineno))
        CommonUtil.ExecLog(sModuleInfo, "Unable to click your element by field: %s and value: %s.  Error: %s"%(field,value, Error_Detail), 3,local_run)
        return "failed"    

CommonUtil.TakeScreenShot("ding", True)
    
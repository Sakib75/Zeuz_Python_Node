'''
Created on July 4, 2016

@author: Riasat Rakin
'''
import sys
import os
import time
sys.path.append(os.path.dirname(os.getcwd()))
from Projects.Youtube_test import Youtube_Search as YTS


def Create_Site_Content():
    YTS.BuiltInFunctions.Open_Browser('firefox')
    Test_For_Get_Elements()
#    Test_For_Get_All_Elements()
##    Henry's Test Page:
#    YTS.BuiltInFunctions.Go_To_Link('http://www.henrys.com/Categories/67-Digital-Cameras-Compare-and-Buy.aspx?source=Cornerstone_Henry%27s+Canada&bypassredirect=true&gclid=CKLv3b3F380CFZY1aQod4jMI2w')
#    YTS.BuiltInFunctions.Get_Element('link_text','Lighting & Studio','id','header_lstCategories_category_4','parent')    

##    Quest Test Page:
#    YTS.BuiltInFunctions.Go_To_Link('https://uwaterloo.ca/quest/')
#    YTS.BuiltInFunctions.Get_Element('link_text','//uwaterloo.ca/')
#    YTS.BuiltInFunctions.Click_Element('class','leaf about-quest mid-453')
#    YTS.BuiltInFunctions.Get_Element('link_text','About Quest','class','leaf about-quest mid-453','parent')
#    YTS.BuiltInFunctions.Enter_Text_In_Text_Box('id', 'masthead-search-term','coldplay', 'placeholder', 'Search')

##    Youtube Test Page:
#'id', 'search-btn','class','yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button'
#    step_data_click =  [ [ ( 'id' , 'search-btn' , False , False ) , ( 'class' , 'yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button' , False , False ) ] ] 
#    step_data_wait = [ ( 'class' , 'num-results first-focus' , False , False ) ]  , [ ( 'timeout' , '30' , False , False ) ] 
#    step_data_text =[ [ ( 'id' , 'masthead-search-term' , False , False ) , ( 'placeholder' , 'Search' , False , False ) ]  , [ ( 'text_value' , 'coldplay' , False , False ) ] ]    
    #YTS.BuiltInFunctions.Go_To_Link('https://www.youtube.com/?hl=en&gl=CA')
#    YTS.BuiltInFunctions.Enter_Text_In_Text_Box('id', 'masthead-search-term','coldplay','placeholder', 'Search')
    #YTS.BuiltInFunctions.Enter_Text_In_Text_Box(step_data_text)
    #YTS.BuiltInFunctions.Click_Element(step_data_click)
#    YTS.BuiltInFunctions.Click_Element('id', 'search-btn','class','yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button')
    #YTS.BuiltInFunctions.Wait_For_New_Element(step_data_wait)
    
#    YTS.BuiltInFunctions.Go_To_Link('http://www.bestbuy.ca/en-CA/product/hewlett-packard-hp-officejet-pro-8710-wireless-colour-all-in-one-inkjet-printer-8710/10419576.aspx?path=1b43ebda1b346b9d5a595ee064882e90en02')
#    YTS.BuiltInFunctions.Go_To_Link('http://assetscience.automationsolutionz.com/Home/ManageTestCases/SearchEdit/') 
#    YTS.BuiltInFunctions.Go_To_Link('http://qa-factory.assetscience.com/totalanalysis/devicesearch/list')    
#    YTS.BuiltInFunctions.Login_To_Application('rrakin', 'password', 'username', 'password', 'submit')#'loginbtn')
#    time.sleep(10)
#    YTS.BuiltInFunctions.Get_Table_Elements('css_selector', 'ul.std-tablist', 'tag_name', 'li', 'tag_name', 'span')
#    YTS.BuiltInFunctions.Get_Table_Elements('tag_name', 'tbody', 'tag_name', 'tr', 'tag_name','td','class','table visible table-striped table-bordered table-hover','parent')
#    YTS.BuiltInFunctions.Get_Table_Elements('tag_name', 'tbody', 'tag_name', 'tr', 'tag_name', 'td')
    #for each_row in list_1:
    #    row_element = list_1[each_row]
    #    print row_element
    print "test complete"
#    YTS.Item_Search('webdriver')

def Test_For_Get_Elements():
    YTS.BuiltInFunctions.Go_To_Link('http://www.kijiji.ca/h-kitchener-waterloo/1700212')
#    YTS.BuiltInFunctions.Go_To_Link('http://www.henrys.com/Categories/67-Digital-Cameras-Compare-and-Buy.aspx?source=Cornerstone_Henry%27s+Canada&bypassredirect=true&gclid=CKLv3b3F380CFZY1aQod4jMI2w')
    #Case 1: ref_parent_or_child == false
    #Case 1.A: ref value and elem = false: single matching
    YTS.BuiltInFunctions.Get_Element('id','SearchInput')
    print "Case 1.A"
    #Case 1.B: ref value and elem != false: double matching
    YTS.BuiltInFunctions.Get_Element('id','SearchInput','name','keywords')
    print "Case 1.B"

    #Case 2: ref_parent_or_child == parent
    YTS.BuiltInFunctions.Get_Element('id','SearchInput','id','InputContainer','parent')
    print "Case 2"
    #Case 3: ref_parent_or_child == child (uses table cases - using Henry's website
    YTS.BuiltInFunctions.Get_Element('text','Accessories','id','header-menus','parent')
    print "end of parent"
    
#    YTS.BuiltInFunctions.Get_Element('text','Lighting & Studio','text','Studio Strobes','child')
#    print "end of child"

def Test_For_Get_All_Elements():
    #Case 1: Parent = False
    #Case 1.A: Param type = text
    YTS.BuiltInFunctions.Get_All_Elements('text', 'Search')
    print "end of text test case"
    #Case 1.B: Param type = tag name
    YTS.BuiltInFunctions.Get_All_Elements('tag_name', 'div')
    print "end of tag test case"
    #Case 1.C: Param type = link text
    YTS.BuiltInFunctions.Get_All_Elements('link_text', 'Lighting & Studio')
    print "end of link test case"
    #Case 1.D: Param type = css
    YTS.BuiltInFunctions.Get_All_Elements('css_selector', 'li.A')
    print "end of css case"
    #Case 1.E: Param type = others /by xpath
    YTS.BuiltInFunctions.Get_All_Elements('id', 'header_lstCategories_dropNav_4')
    print "end of xpath case"
        
Create_Site_Content()
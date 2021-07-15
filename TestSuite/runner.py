from TestSuite.Page.Base import base
from TestSuite.pageobjct.SearcH import Searchpage
from selenium.webdriver.common.by import By
#from TestSuite.Variablelayer.Variable import *
import time
import unittest
leave='成都'
leave_data="2021-07-20"
arrive='北京'
arrive_data='2021-07-30'
aa=Searchpage()
aa.search7(leave='成都',leave_data="2021-07-20",arrive='北京',arrive_data='2021-07-30')


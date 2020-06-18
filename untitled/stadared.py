import  os
import glob
import time
import django
from selenium import webdriver

driver = webdriver.chrome()
if driver:
    print('adss')


#
# print(time.time(),'!!!')
#
# t = time.asctime(time.localtime(time.time()))
# print(t)
# # print(os.getcwd())
# # print(glob.glob('*.py'))
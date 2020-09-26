import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as tm


class Sherwin():


    def __init__(self):

        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")

        self.driver = webdriver.Chrome(chrome_options= options)
        self.driver.get('https://www.sherwin-williams.com.br/cores')
        tm(4)

    def getColors(self):

        colorsinit = self.driver.find_elements_by_class_name('item')

        for color in colorsinit:

            color.click()

            tm(4)



tinta = Sherwin()
tinta.getColors()



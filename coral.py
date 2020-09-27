import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as tm


class Coral():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(chrome_options= options)
        self.driver.get('https://www.coral.com.br/pt/paletas-de-cor/h_white')
        tm(3)
        self.driver.find_element_by_xpath('/html/body/div[11]/section/div/article/div[3]/a[1]').click()
        
        tm(4)
    def getColors(self):

        namecolor = ''
        idcolor = ''
        hexcolor = ''
        text_final = '"ColorName","ColorId","ColorHex"\n'

        links = [
            'https://www.coral.com.br/pt/paletas-de-cor/h_white',
            'https://www.coral.com.br/pt/paletas-de-cor/h_red',
            'https://www.coral.com.br/pt/paletas-de-cor/h_orange',
            'https://www.coral.com.br/pt/paletas-de-cor/h_gold',
            'https://www.coral.com.br/pt/paletas-de-cor/h_yellow',
            'https://www.coral.com.br/pt/paletas-de-cor/h_lime',
            'https://www.coral.com.br/pt/paletas-de-cor/h_green',
            'https://www.coral.com.br/pt/paletas-de-cor/h_teal',
            'https://www.coral.com.br/pt/paletas-de-cor/h_blue',
            'https://www.coral.com.br/pt/paletas-de-cor/h_violet',
            'https://www.coral.com.br/pt/paletas-de-cor/h_cool%20neutral',
            'https://www.coral.com.br/pt/paletas-de-cor/h_warm%20neutral']

        index = 1
        for link in links:

            self.driver.get(link+'?tab=2')
            tm(4)

            while(True):
                try:
                    element = self.driver.find_element_by_xpath(f'/html/body/div[3]/div/div/section/div/section/section[2]/div/div[2]/div/section/div/div[{index}]/a')
                    namecolor = element.get_attribute('data-title')
                    idcolor = element.get_attribute('data-colorid')
                    hexcolor = '#'+str(element.get_attribute('data-id'))
                    text_final = text_final+f'"{namecolor}"'+','+f'"{idcolor}"'+','+f'"{hexcolor}"'+'\n'
                    print(namecolor)
                    index = index+1
                except:
                    index = 1
                    break                         
            groumps = 1
            controller = True
            while(True):

                self.driver.get(link+'?tab=1')
                tm(7)
                self.driver.find_element_by_class_name('content-closed ').click()
                                                  

                tm(2)
                try:
                    while(True):
                    
                        controller = element = self.driver.find_element_by_xpath(f'/html/body/div[3]/div/div/section/div/section/section[2]/div/div[2]/div[2]/div[{index}]/div[2]/div[1]/a')
                        
                        
                        try:
                            element = self.driver.find_element_by_xpath(f'/html/body/div[3]/div/div/section/div/section/section[2]/div/div[2]/div[2]/div[{index}]/div[2]/div[{groumps}]/a')
                            
                        except:
                            index = index+1
                            groumps = 1
                            break
                        namecolor = element.get_attribute('data-title')
                        idcolor = element.get_attribute('data-colorid')
                        hexcolor = '#'+str(element.get_attribute('data-id'))
                        text_final = text_final+f'"{namecolor}"'+','+f'"{idcolor}"'+','+f'"{hexcolor}"'+'\n'
                        groumps = groumps+1
                        print(namecolor)
                 
                except:

                    break
        
        open('data_coral.csv','w', -1, "utf-8").write(text_final)    
        read_file = pd.read_csv(open('data_coral.csv','rb'))
        read_file.to_excel('data_Coral.xlsx', index = None, header=True)
                                                              
                                                             

                

coral = Coral()
coral.getColors()
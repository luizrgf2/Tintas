import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as tm
from colormap import rgb2hex
from webdriver_manager.chrome import ChromeDriverManager


class Eucatex():

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(chrome_options= options,executable_path=ChromeDriverManager().install())
        self.driver.get('https://www.eucatex.com.br/tintas/e-colors')
        tm(4)
    def getColors(self):

        buttons = self.driver.find_elements_by_class_name('nav-link') #botões dos tons das cores do site

        
        namecolor = ''
        idcolor = ''
        hexcolor = ''
        text_final = '"ColorName","ColorId","ColorHex"\n'

        

        

        for button in buttons: #pegar as cores se baseando em cada botão
            
            button.click()
            tm(4)
            colors = self.driver.execute_script('return document.getElementsByClassName("btn btn-colors")') #cores separadas por cada tom 
            print(f'{len(colors)} cores detectadas!')


            for i in range(len(colors)): #pegando dados de cada cor
                try:
                    text = self.driver.find_element_by_xpath(f'/html/body/app-root/app-e-colors/div/div/main/div[2]/div/ul/li[{i+1}]/span/span[3]').text.split(' ')[1]#pegando texto dar cor rgb para ser convertido para hex
                    namecolor = self.driver.find_element_by_xpath(f'/html/body/app-root/app-e-colors/div/div/main/div[2]/div/ul/li[{i+1}]/span/span[1]').text
                    idcolor = self.driver.find_element_by_xpath(f'/html/body/app-root/app-e-colors/div/div/main/div[2]/div/ul/li[{i+1}]/span/span[2]').text
                    hexcolor = self.converColortohex(text)
                    text_final = text_final+f'"{namecolor}"'+','+f'"{idcolor}"'+','+f'"{hexcolor}"'+'\n' #pegando texto e dividindo para ser escrito em arquivo csv
                    print(namecolor+' '+idcolor+' '+hexcolor)
                except:
                    break


                  
        
        
        
        
        #escrevendo no arquivo csv e depois convertendo para excel
        open('data_eucatex.csv','w', -1, "utf-8").write(text_final)    
        read_file = pd.read_csv(open('data_eucatex.csv','rb'))
        read_file.to_excel('data_Eucatex.xlsx', index = None, header=True)
        #####


    def converColortohex(self,rgb):

        colorrgb = rgb.split(',')

        return rgb2hex(int(colorrgb[0]),int(colorrgb[1]),int(colorrgb[2]))                      

            


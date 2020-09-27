import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as tm
from colormap import rgb2hex


class Suvinil():

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(chrome_options= options)
        self.driver.get('https://www.suvinil.com.br/cores/todas-as-cores')
        tm(4)
    
    def getColors(self,numColor):

       
        namecolor = []
        idcolor = []
        hexcolor = []
        text_final = '"ColorName","ColorId","ColorHex"\n'

        #No site as cores são separadas em tons claros e escuros
        coresclaras = self.driver.execute_script('return document.getElementsByClassName("item item-color light");')
        coresescuras = self.driver.execute_script('return document.getElementsByClassName("item item-color dark");')
        ########

        for i in range(len(coresclaras)-1):#pegando dados dos tons claros




            
            namecolor.append(coresclaras[i].get_attribute('data-name'))
            idcolor.append(coresclaras[i].get_attribute('data-code'))
            hexcolor.append(self.converColortohex(coresclaras[i].get_attribute('data-rgb')))
            text_final = text_final+f'"{namecolor[i]}"'+','+f'"{idcolor[i]}"'+','+f'"{hexcolor[i]}"'+'\n'


        for i in range(len(coresescuras)):#pegando dados dos tons escuros




            
            namecolor.append(coresescuras[i].get_attribute('data-name'))
            idcolor.append(coresescuras[i].get_attribute('data-code'))
            hexcolor.append(self.converColortohex(coresescuras[i].get_attribute('data-rgb')))
            text_final = text_final+f'"{namecolor[i]}"'+','+f'"{idcolor[i]}"'+','+f'"{hexcolor[i]}"'+'\n'
           




        #escrevendo no arquivo csv e depois convertendo para excel   
        open('data_suvinil.csv','w', -1, "utf-8").write(text_final)    
        read_file = pd.read_csv(open('data_suvinil.csv','rb'))
        read_file.to_excel('data_Suvinil.xlsx', index = None, header=True)
        #####

    def converColortohex(self,rgb):

        colorrgb = rgb.split(',')

        return rgb2hex(int(colorrgb[0]),int(colorrgb[1]),int(colorrgb[2]))

        


        
                                          


Su = Suvinil()
Su.getColors(2000)


  


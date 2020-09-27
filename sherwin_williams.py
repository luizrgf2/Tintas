import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as tm


class Sherwin():


    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(chrome_options= options)
        self.driver.get('https://www.sherwin-williams.com.br/cores')

        tm(2)

    def getColors(self):

        namecolor = ''
        idcolor = ''
        hexcolor = ''
        text_final = '"ColorName","ColorId","ColorHex"\n'
        line = []
        links = [
            'https://www.sherwin-williams.com.br/cor_base/vermelhos-alaranjados/',
            'https://www.sherwin-williams.com.br/cor_base/amarelos-verdes/',
            'https://www.sherwin-williams.com.br/cor_base/azul-violetas/',
            'https://www.sherwin-williams.com.br/cor_base/neutros1/',
            'https://www.sherwin-williams.com.br/cor_base/neutros2/',
            'https://www.sherwin-williams.com.br/cor_base/brancos-pasteis/',
            'https://www.sherwin-williams.com.br/cor_base/colecao-atemporal/',
            'https://www.sherwin-williams.com.br/cor_base/cores-marcantes/'  ]
        num_site = 0

        index = 0
        
        self.driver.get(links[0])
        tm(3)
        while(True): # usando um laço infinito por nao ter como pegar os objetos previamente e saber o tamanho da lista

            index = index+1

            for i in range(1,8): #cada linha tem 8 posiçoes, pegando objetos de cada linha
                try:
                    element = self.driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div/div/ul[{index}]/li[{i}]/a')
                    namecolor = element.get_attribute('data-titulo')
                    idcolor = element.get_attribute('data-codigo')
                    hexcolor = '#'+element.get_attribute('data-cor')
                    text_final = text_final+f'"{namecolor}"'+','+f'"{idcolor}"'+','+f'"{hexcolor}"'+'\n'
                    print(namecolor)
                except:
                    num_site =num_site+1
                    try:
                        self.driver.get(links[num_site])
                    except:
                        open('data_sherwin.csv','w', -1, "utf-8").write(text_final)    
                        read_file = pd.read_csv(open('data_sherwin.csv','rb'))
                        read_file.to_excel('data_Sherwin.xlsx', index = None, header=True)
                        return
                    index = 0
                    tm(4)
                    break
        

                

                                                             



            

        
 
                
            
                    
                    
                                                           

                                             
            

        

tinta = Sherwin()
tinta.getColors()



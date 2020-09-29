from eucatex import Eucatex
from suvinil import Suvinil
from coral import Coral
from sherwin_williams import Sherwin
from time import sleep as tm
import zipapp


def main():


    print('uma vez executado, ele rodara ate que você encerre o script!\n')
    tm(3)
    try:
        time = int(input('Digite o tempo para a proxima atualização [em segundos]!'))
    except:

        print('Apenas números são permitidos, tente de novo!')
        return


    while(True):
        
        print('Buscando dados do site da Coral, isso pode demorar um pouco!\n\n')

        coral = Coral()
        coral.getColors()
        
        print('Buscando dados do site da Eucatex, isso pode demorar um pouco!\n\n')

        eucatex = Eucatex()
        eucatex.getColors()

        print('Buscando dados do site da Suvinil, isso pode demorar um pouco!\n\n')

        suvinil = Suvinil()
        suvinil.getColors()


        print('Buscando dados do site da Sherwin, isso pode demorar um pouco!\n\n')

        sherwin = Sherwin()
        sherwin.getColors()

        tm(time)


main()








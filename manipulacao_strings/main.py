from datetime import datetime
from time import sleep
import os

def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

""" Gerar data para renomear o arquivo """
def get_hours():
    date = datetime.now()
    day = date.strftime("%d_%m_%Y")

    return day

""" Funcao principal """
def main(frase):
    context = frase
    print("\033[0;33;44mVerifiando ou criando a Pasta!\033[m\n")
    sleep(1)
    paths = "./arquivos"
    os.makedirs(paths, exist_ok=True)

    name_file = get_hours()

    if context == 'exit':
        print(f"\033[0;32;42m| Conteudo do arquivo = {name_file}.txt |\033[m")

        with open(f"{paths}/{name_file}.txt", mode="r", encoding="utf-8") as file:
            text = file.readlines()

            for i, row in enumerate(text):
                print(f"{i}: {row}")
                sleep(.5)
        exit()

    else:
        print("\033[0;33;44mModificando...\033[m\n")
        sleep(1)

        """ Manipulando Strings """
        frase_modi = context.strip()
        fm = frase_modi.capitalize()

        print("\033[0;33;44mEscrevendo no arquivo!\033[m\n")
        sleep(1)

        try:
            with open(f"{paths}/{name_file}.txt", mode="a", encoding="utf-8") as file:
                sleep(1)
                file.write(f"{fm}\n")
                print("\033[0;32;42mConteudo escrito com sucesso!\033[m")
                sleep(3)
                clear_console()

        except Exception as err:
            print(f"\033[31mERROR => {err}\033[m")

if __name__ == "__main__":
    while True:
        frase = input("DIGITE: ")
        main(frase)
        if frase == 'exit':
            break
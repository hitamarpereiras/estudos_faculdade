from time import sleep
import os

alphabet = [
    ('a', '*'), ('b', '&'), ('c', '**'), ('d', '?'), ('e', '#*'),
    ('f', '++'), ('g', '*&'), ('h', '!'), ('i', '*%'), ('j', '$'),
    ('k', '*#'), ('l', '!*'), ('m', '&&'), ('n', '*$'), ('o', '$#'),
    ('p', '0*'), ('q', '-'), ('r', '+='), ('s', '@'), ('t', '+^'),
    ('u', '&^'), ('v', '^'), ('w', '$@'), ('x', '*^*'), ('y', '!!'),
    ('z', 'x^'), ('A', 'Z'), ('B', 'Y'), ('C', 'X'), ('D', 'W'),
    ('E', 'V'), ('F', 'U'), ('G', 'T'), ('H', 'S'), ('I', 'R'),
    ('J', 'Q'), ('K', 'P'), ('L', 'O'), ('M', 'N'), ('N', 'M'),
    ('O', 'L'), ('P', 'K'), ('Q', 'J'), ('R', 'I'), ('S', 'H'),
    ('T', 'G'), ('U', 'F'), ('V', 'E'), ('W', 'D'), ('X', 'C'),
    ('Y', 'B'), ('Z', 'A')
]

def coding(word):
    for w_old, w_new in alphabet:
        word = word.replace(w_old, w_new)
        
    return word

def decoding(word):
    for w_new, w_old in alphabet:
        word = word.replace(w_new, w_old)

    return word
   
def main():
    print('===== MENU =====')
    print('[0] Para SAIR.')
    print('[1] Para CODIFICAR.')
    print('[2] Para DECODIFICAR.')
    cmd = int(input(">> "))

    if cmd == 1:
        print('Pegando o Texto')
        sleep(.5)
        text = input('Text: ')

        words = text.split()

        print('Codificando...')
        sleep(.5)
        coding_words = [coding(word) for word in words]

        finish_text = " ".join(coding_words)

        print('Finalizado! \n')
        sleep(.5)
        print(f"Original: {text:10}")
        sleep(.5)
        print(f"Codificada: {finish_text:10}")
        input("Aperte enter pra continuar...")
        
    elif cmd == 2:
        print('Pegando o Texto')
        sleep(.5)
        text = input('Text: ')

        words = text.split()

        print('Codificando...')
        sleep(.5)
        coding_words = [decoding(word) for word in words]

        finish_text = " ".join(coding_words)

        print('Finalizado! \n')
        sleep(.5)
        print(f"Original: {text:10}")
        sleep(.5)
        print(f"Codificada: {finish_text:10}")
        input("Aperte enter pra continuar...")

    elif cmd == 0:
        print("Fim do Programa.")
        exit()

if __name__ == "__main__":
    while True:
        os.system(command='cls')
        main()
import sys
import re

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py nome_do_arquivo")
        sys.exit(1)

    texto = ler_arquivo(sys.argv[1])
    divisao = re.split(r"(on|off|=)", texto, flags=re.I)

    counter = 0
    i = 0
    state = True
    size = len(divisao)

    while i < size:
        if re.fullmatch(r"on", divisao[i], flags=re.I):
            state = True
        elif re.fullmatch(r"off", divisao[i], flags=re.I):
            state = False
        elif re.fullmatch(r"=", divisao[i]):
            print(counter)
        else:
            if state:
                counter += sum(map(int, re.findall(r"\d+", divisao[i])))
        i += 1

    print(f"A soma é: {counter}")

if __name__ == "__main__":
    main()

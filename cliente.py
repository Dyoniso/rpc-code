import Pyro4

SERVER_LINK = 'PYRO:obj_449f67588d4b40228215f00f0a5aeedd@localhost:52474'

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy(SERVER_LINK)  # Substitua 'obj_123456' pelo URI do servidor
    resultado = calculadora.somar(85, 3)
    print("A soma é:", resultado)

    resultado = calculadora.subtrair(10, 3)
    print("A subtração é:", resultado)

    resultado = calculadora.multplicar(40, 3)
    print("A multplicação é:", resultado)

if __name__ == "__main__":
    main()

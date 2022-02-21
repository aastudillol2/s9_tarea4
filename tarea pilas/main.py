from Pila_cola_lista import *
import os

c1 = True
while c1:
    opc = input('1.PILAS 2.COLAS. 3.LISTAS 4.SALIR: ')
    os.system('cls')
    if opc == '1':
        print('Bienvenido a pilas'.center(30,'-'))
        c = True
        while c:
            opc = input('\n1.PUSH 2.POP 3.LONGITUD 4.SHOW 5.BUSCAR 6.SALIR: ')
            if opc == '1':
                tamaño = int(input('\nIngrese el tamaño de la pila: '))
                pila = Stack(tamaño)
                pila.push()
            else:
                if opc == '2':
                    pila.pop()
                else:
                    if opc == '3':
                        pila.longitud()
                    else:
                        if opc == '4':
                            pila.show()
                        else:
                            if opc == '5':
                                pila.buscar()
                            else:
                                if opc == '6':
                                    c = False
                                    c1 = True
                                    os.system('cls')
    else:
        if opc == '2':
            print('Bienvenido a colas'.center(30,'-'))
            c = True
            while c:
                opc = input('\n1.PUSH 2.POP 3.LONGITUD 4.SHOW 5.BUSCAR 6.SALIR: ')
                if opc == '1':
                    tamaño = int(input('\nIngrese el tamaño de la cola: '))
                    cola = Cola(tamaño)
                    cola.push()
                else:
                    if opc == '2':
                        cola.pop()
                    else:
                        if opc == '3':
                            cola.longitud()
                        else:
                            if opc == '4':
                                cola.show()
                            else:
                                if opc == '5':
                                    cola.buscar()
                                else:
                                    if opc == '6':
                                        c = False
                                        c1 = True
                                        os.system('cls')
        else:

            if opc == '3':
                print('Bienvenido a listas'.center(30,'-'))
                
                c = True
                while c:
                    opc = input('\n1.PUSH 2.POP 3.SHOW 4.ELIMINAR ELEMENTO 5.INSERTAR ELEMENTO 6.BUSCAR 7.SALIR: ')
                    if opc == '1':
                        tamaño = int(input('\nIngrese el tamaño de la lista: '))
                        lista1 = Lista(tamaño)
                        lista1.push()
                    else:
                        if opc == '2':
                            lista1.pop()
                        else:
                            if opc == '3':
                                lista1.show()
                            else:
                                if opc == '4':
                                    lista1.eliminarElemento()
                                else:
                                    if opc == '5':
                                        lista1.insertarElemento()
                                    else:
                                        if opc == '6':
                                            lista1.buscar()
                                        else:
                                            if opc == '7':
                                                c = False
                                                c1 = True
                                                os.system('cls')
            else:
                if opc == '4':
                    print('Gracias por usar el programa')
                    c1 = False

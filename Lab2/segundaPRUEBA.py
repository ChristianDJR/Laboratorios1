import hashlib
import os
##---------------------------------------------------------------------
##---------------ROT(-12)--------------------------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------

def rotmenos12 (phrase):
   abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   desfrase = ""
   for char in phrase:
       desfrase += abc[(abc.find(char)- 12)%26]  
   return desfrase

print('''---------------------------------------------------------------------
                                 ROT (-12)                                                                     
---------------------------------------------------------------------''')
phrase = input("Ingrese su frase a descifrar -->")
phrase_upper = phrase.upper()

print("La frase descifrada es la siguiente -->", ((rotmenos12(phrase_upper))))

number = 1
for number in range(10):
    if number == 2:
        break    # break here

    print('Espera ' + str(number))
    
##---------------------------------------------------------------------
##---------------VIGENERE-FINISPASSWD----------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------
ABC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
'''
ABECEDARIO SIN LA LETRA Ñ, debido a generacion de error
Esto iniciara desde el 0 al 25, donde empieza como A como 0 y termina con Z como 25
'''
def main ():
   print('''

        Bienvenido a la encriptacion y descifrado de VIGENERE
        A continuacion siga los siguientes pasos:
        → Mensaje: (Mensaje que deseas descifrar)
        → Modo: SOLO PUEDES DESCIFRAR COLOCANDO "descifrar"
        → (Mensaje final)
        ''')
   mensaje =(rotmenos12(phrase_upper))
   llave= "FINISPASSWD" #Llave de seguridad
   opcion= input("Modo: ")
    
   if opcion== 'descifrar':
      traducido= descifrar_mensaje(llave, mensaje)
   print(traducido)

def descifrar_mensaje(clave, mensa):
   return traductor_mensaje(clave, mensa,'descifrar')
##---------------------------------------------------------------------
'''Mezcla entre el mensaje y la llave de seguridad'''
##---------------------------------------------------------------------
def traductor_mensaje(clave, mensa, opcion): #Recorrera el mensaje que se encriptara o descifrara
    traducido=[] #Se almacenan los caracteres de susticion
    indice_clave=0 #Recorrera la palabra clave e iniciara con 0
    clave=clave.upper() #Convierte en mayusculas las palabras

    for symbol in mensa:
        num= ABC.find(symbol.upper())

        if num!=-1:
                #find encuentra la aparicion del valor especificado devuelve -1 sino
                #encuentra el valor
            if opcion=='descifrar':
                num-=ABC.find(clave[indice_clave])
            num%=len(ABC)
##---------------------------------------------------------------------
            if symbol.isupper():
                traducido.append(ABC[num]) #Si el caracter es en mayuscula
                
            elif symbol.islower():
                traducido.append(ABC[num].lower()) # Si el caracter es en minuscula

            indice_clave +=1

            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido) #Toma todos los valores y los une en una sola cadena
if __name__== '__main__':
    main()
print('''---------------------------------------------------------------------
                           LEER ABAJO PARA CONTINUAR :=)                                                                   
---------------------------------------------------------------------''')

variable2 = input("Ingrese la encriptacion de viginere para la ultima permutacion a descifrar-->")
print('''
''')
print('''---------------------------------------------------------------------
                                 ROT (-8)                                                                     
---------------------------------------------------------------------''')

##---------------------------------------------------------------------
##---------------ROT(-8)--------------------------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------
def rotmenos8 (phrase):
   abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   desfrase = ""
   for char in phrase:
       desfrase += abc[(abc.find(char)- 8)%26]
   return desfrase

phrase = variable2
phrase_upper = phrase.upper()
final = rotmenos8(phrase_upper)
final2= final.lower()


# ---------------------------------------------------------------------
# ------------------------HASH-----------------------------------------
# ---------------------------------------------------------------------
'''SACO EL HASH DE LA PALABRA DESCIFRADA'''
salida1 = hashlib.sha256(final2.encode("utf-8")).hexdigest()
print(salida1)


'''COMPARO LOS HASH DEL MENSAJE INICIAL INGRESADO SIN HASH Y DEL FINAL DESCIFRADO'''

# ---------------------------------------------------------------------
# ------------------------ INTEGRIDAD DEL MENSAJE / HASH---------------
# ---------------------------------------------------------------------

archivo3= open('mensajeseguro.txt', 'r')
primeralinea= archivo3.readline()
segundalinea= archivo3.readline()
terceralinea= archivo3.readline()
archivo3.close()

#---------------------------------------------------------------------
#--------- INTEGRIDAD DEL MENSAJE COMPARACION DEL HASH---------------
#---------------------------------------------------------------------
if terceralinea == salida1:
   print("LOS HASH SON IGUALES, POR LO QUE LA INTEGRIDAD SIGUE INTACTA")
else:
   print("SON DIFERENTES, DAÑO EN LA INTEGRIDAD DEL MENSAJE")
   
#---------------------------------------------------------------------
#------------------ OBSERVACION DE LOS MENSAJES------------------------
#---------------------------------------------------------------------

archivo= open('mensajedeentrada.txt', 'r')
primeralinea2= archivo.readline()
archivo.close()

number3 = 1
for number3 in range(10):
    if number3 == 2:
        break    # break here

    print('Espera ' + str(number3))
    
print(''' ''')
print(''' ''')

if final2 != primeralinea2:
   print('''EL MENSAJE  HA SUFRIDO CAMBIOS''')          
else:
   print('''EL MENSAJE NO HA SUFRIDO CAMBIOS''')          
   print("→Mensaje Inicial:", final2)
   print("→Mensaje despues de descifrado:", primeralinea2)







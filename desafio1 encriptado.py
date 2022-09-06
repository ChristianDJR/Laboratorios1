##---------------------------------------------------------------------
##---------------ROT(8)--------------------------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------

def rot8 (phrase):
   abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   desfrase = ""
   for char in phrase:
       desfrase += abc[(abc.find(char)+ 8)%26]  
   return desfrase

print('''---------------------------------------------------------------------
                                 ROT (8)                                                                     
---------------------------------------------------------------------''')
phrase = input("Ingrese su frase a cifrar -->")
phrase_upper = phrase.upper()

print("La frase descifrada es la siguiente -->", ((rot8(phrase_upper))))

##---------------------------------------------------------------------
##---------------VIGENERE-heropassword--------------------------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------
ABC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
'''
ABECEDARIO SIN LA LETRA Ñ, debido a generacion de error
Esto iniciara desde el 0 al 25, donde empieza como A como 0 y termina con Z como 25
'''
def main ():
   print('''
''')
   print('''---------------------------------------------------------------------
                                 VIGENERE                                                                     
---------------------------------------------------------------------''')
   print('''

        Bienvenido a la encriptacion y descifrado de VIGENERE
        A continuacion siga los siguientes pasos:
        → Mensaje: (Mensaje que deseas encriptar o descifrar)
        → Modo: Las opciones son "encriptar" o "descifrar"
        → (Mensaje final)
        ''')
   mensaje =input("Mensaje:")
   llave= "HEROPASSWORD" #Llave de seguridad
   opcion= input("Modo: ")
    
   if opcion== 'encriptar':
      traducido= cifrar_mensaje(llave, mensaje)
   elif opcion== 'descifrar':
      traducido= descifrar_mensaje(llave, mensaje)
   print(traducido)

'''Retornara dependiendo la eleccion del usuario tanto si este sea encriptar o descifrar'''

def cifrar_mensaje(clave, mensa):
   return traductor_mensaje(clave, mensa,'encriptar')

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
            if opcion=='encriptar':
                num+=ABC.find(clave[indice_clave])
                #find encuentra la aparicion del valor especificado devuelve -1 sino
                #encuentra el valor
            elif opcion=='descifrar':
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
print('''
''')
print('''---------------------------------------------------------------------
                                 ROT (12)                                                                     
---------------------------------------------------------------------''')

##---------------------------------------------------------------------
##---------------ROT(12)--------------------------------------------------
##---------------------------------------------------------------------
##---------------------------------------------------------------------
def rot12 (phrase):
   abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   desfrase = ""
   for char in phrase:
       desfrase += abc[(abc.find(char)+ 12)%26]
   return desfrase

phrase = input("Ingrese su frase a cifrar -->")
phrase_upper = phrase.upper()

print("La frase descifrada es la siguiente -->", ((rot12(phrase_upper))))

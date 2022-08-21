import random

def run():
    available_chars=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V',
             'W','X','Y','Z' 'a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z','&','?','!','#')
    name=''
    usuario=''
    while name=='':


        name=input(' Escriba su Nombre:')
        if name=='':
            print('es obligatorio escribir el nombre')
            continue
        
        else:
            while usuario=='' or len(usuario)<5:
                    usuario=input('Escriba su usuario:')
                    if usuario=='' or len(usuario)<5:
                        print('Escriba un usuario de minimo 5 caracteres')
                        continue
                    else:
                        option=input('Desea que el sistema sugiera un password:')
                        if option=='s':
                            char=0
                            contra=''
                            for chararcter in range (1,11):
                                 char=random.randint(1,51)
                                 finalpword=available_chars[char]
                                 contra=contra+finalpword
            
                            print('su contrasena es:'+str(contra))

                        else:
                            finalpword=input('escriba un password:')
                            print(finalpword)

        
            

if __name__== '__main__':
    run()


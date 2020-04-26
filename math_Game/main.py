from game import game 

gm = game()

def menu():

    print('''
        Which level do you want to keep game (For Exit please Enter : -1) ?

        For Easy Press 1

        For Middle Press 2

        For Hard Press 3
        
        For Legendary Press 4
    
    ''')

    level = input(">> ")

    if level == 1 :
        pass
    elif level == 2 :
        pass
    elif level == 3 :
        pass
    elif level == 4 :
        pass
    else :
        print('QUITING.....')
        exit(0)




if __name__ == "__main__":
    
   print('-'*50,'\n')
   print('\t\t ...Welcome...') 
   print('-'*50,'\n')
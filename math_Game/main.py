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

    try :
        level = int(input(">>"))
    except ValueError:
        print('Oops! That was no valid number. Try Again...')


    if level == 1 :
        gm.gameBegin(1,6)
    elif level == 2 :
        gm.gameBegin(6,12)
        
    elif level == 3 :
        gm.gameBegin(12,25)
    elif level == 4 :
        gm.gameBegin(25,100)
    else :
        print('QUITING.....')
        exit(0)




if __name__ == "__main__":
    
   print('-'*50,'\n')
   print('\t\t ...Welcome...') 
   print('-'*50,'\n')
   menu()
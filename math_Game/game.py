# Created by Mert Demirezen 
# Copyright © 2019 Mert Demirezen. All rights reserved.


from random import randint as rnd

class game:
    def __init__(self,correctAnswer = 0, wrngAnsw = 0):
        
        self.crctAns = correctAnswer
        self.wrngAnsw = wrngAnsw
    def checkAnswer(self,nm1,nm2,ans):
        
        if ans == -1 :
            self.gameOver()
            
        else : 
            if (nm1*nm2 == ans):
                self.crctAns += 1
                print('\t\t','*'*5,' Correct! ','*'*5)
            else :
                self.wrngAnsw += 1
                print('\t\t !!! WRONG ANSWER !!!\n Correct answer is : {}'.format(nm1*nm2))






    def gameBegin(self,a,b):
        

        if a > 10 :  lenght = 10 
        else : lenght = 5
        
        for i in range (0,lenght): 
            for j in range (0,lenght):
                number1 = rnd(a,b)
                number2 = rnd(a,b)

                print('-'*50,'\n')
                print('\t{} x {} = ? Please Enter The Answer : (For Exit Press : -1)'.format(number1,number2))
                try :
                    user_answer = int(input(">> "))
                except ValueError:
                    print('Oops! That was no valid number. Try Again...')

                
                self.checkAnswer(number1,number2,user_answer) 
                if i == 4 and j == 4 :
                    self.gameOver()
                

    def gameOver(self):
        print('''
                 ***** GAME OVER *****

                 Correct Answers = {}
                 Wrong Answers = {}

                 *********************
        '''.format(self.crctAns,self.wrngAnsw))
        exit(0)
        
        

        


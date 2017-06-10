'''
Created on Jun 2, 2017

@author: tarun.walia
'''
from random import randint
import sys
class GuessNumber:
    
    # system is guessing below number
    def systemGeneratedNum(self):
        sys_num = randint(1, 43)
        print "sys_num-: ",sys_num
        return sys_num
        
    
    def userInputNum(self):
        input1 = input("Enter number: ")
        return input1
    
    
    def compareInputNum(self, sys_num):
        #sys_num = self.systemGeneratedNum()
        input = self.userInputNum()
        
        while input>0:
            if input > sys_num+10:
                print "Input num is greather than sys_num"
                self.compareInputNum(sys_num)
                
            elif input > sys_num+5:
                print "Input num is close to sys_num"
                self.compareInputNum(sys_num)
                
            elif input < sys_num:
                print "Input num is less than sys_num"
                self.compareInputNum(sys_num)
             
            elif input == sys_num:
                print "Input num is equal sys_num"
                sys.exit()
                    
            else: print "Input num is close to sys_num"       
            
                
if __name__ =='__main__':
    guessNum = GuessNumber()
    num = guessNum.systemGeneratedNum()
    guessNum.compareInputNum(num)
    
                
                     
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:46:19 2019

@author: Sanna

Pupose: procastination 

Different dice problems 

"""
import numpy as np
import matplotlib.pyplot  as plt

def goblin_dice(nbr_dice = 1,nbr_iter=20000):
    
    result = np.zeros((nbr_iter,107*nbr_dice))    
    summa = 0
    for ii in range(0,nbr_iter):            
        while (summa<100):
            for jj in range(0,nbr_dice):
                # roll dices and sum them
                tal = roll_dice(nbr_dice)                
            summa += tal

            result[ii,summa] = result[ii,summa] + 1
        summa = 0
        
    plt.figure()
    plt.title('%d dice'%nbr_dice)
    plt.plot((sum(result))        )
    plt.xlabel('number')
    plt.ylabel('nbr of times hit')

def goblin_coin(nbr_dice = 1,nbr_iter=20000):
    
    result = np.zeros((nbr_iter,10*nbr_dice))    
    summa = 0
    for ii in range(0,nbr_iter):            
        while (summa<4):
            for jj in range(0,nbr_dice):
                # roll dices and sum them
                tal = roll_coin(nbr_dice)                
            summa += tal

            result[ii,summa] = result[ii,summa] + 1
        summa = 0
        
    plt.figure()
    plt.title('%d coin'%nbr_dice)
    plt.plot(sum(result),'bo'        )
    plt.plot(sum(result)        )
    plt.xlabel('number')
    plt.ylabel('nbr of times hit')
    
        
    
    
def roll_dice(nbr_dice=1):
    summa = np.sum(np.random.randint(1,7,size=nbr_dice))    
    return summa

def roll_coin(nbr_dice=1):
    summa = np.sum(np.random.randint(1,3,size=nbr_dice))    
    return summa

# on average, how many times must a dice be roll until a 6 turns up?
def when_number(number,nbr_iter=100):
    rolls=0
    dice=0
    statistics=[]
    for ii in range(0,nbr_iter):
        while dice!=number:
            dice=roll_dice(nbr_dice=1)
            rolls +=1
        # save result
        statistics.append(rolls)
        # start over
        rolls=0
        dice=0
    print np.mean(statistics) 
    
# How many tims in a row must a dice be thrown for a 6 to come up 2 times in a row?
def when2times(nbr_iter =100):
    rolls = 0
    throw = 0 
    statistics = []
    for ii in range(0,nbr_iter):
        # throw 2 dice (one twice in a row)
        while throw!=12:
            throw = roll_dice(nbr_dice=2)
            rolls +=1
        # save result
        statistics.append(rolls)
        # start over
        rolls = 0
        throw = 0
    print np.mean(statistics)     
    
def prob_number(number=1,nbr_dice=3,nbr_iter=1000):
    # calculate the prbability to get any number, with any number of dices
    # by numerical    
    result = np.zeros((nbr_iter,6*nbr_dice+1))    
    for ii in range(0,nbr_iter):            
        # roll dices and sum them
        tal = roll_dice(nbr_dice)                
        result[ii,tal] += 1
    
    #return the probability
    return sum(result[:,number])/ len(result)

if __name__ == '__main__':
    
    #goblin_dice(nbr_dice = 5,nbr_iter=10000)
    
    goblin_coin(nbr_dice = 1,nbr_iter=10000)
    
    print 'Roll a die'
    print roll_dice(nbr_dice=2)
    
    print 'On average, how many times must a dice be roll until a 6 turns up?'
    print 'Answer: '
    when_number(6,10000)
    
    print '# How many tims in a row must a dice be thrown for a 6 to come up 2 times in a row?       '
    print 'Answer: '
    when2times(1000)
    
    num = 2
    nbr_dice = 3
    print 'What is the probability to get %d with %d dice?'%(num,nbr_dice)
    print prob_number(num,nbr_dice,nbr_iter=10000)
    
    

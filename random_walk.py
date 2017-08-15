#Simulate a random walk
#100 random steps to this random walk
#random steps add onto one another-up or down (use append)
#win if you make it to 60th floor.

#random step is defined by a die toss outcome and clumsiness
#roll 1 or 2 -take step down
#roll 3,4,5-take step up
#roll 6-roll again and take as many steps up as numbers shown on the die
#.001 chance of falling down to the first floor when taking any step 

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(134)

all_walks=[]

#500 random walk simulations
for i in range(500):

    #random walk-100 random steps
    rand_walk=[0]
    for x in range(100):
        step=rand_walk[-1]
        # random step
        die_roll=np.random.randint(1,7) 
        if die_roll<=2:
            step=max(0,step-1)
        elif die_roll<=5:
            step=step+1
        else:
            step=step+np.random.randint(1,7)
        #clumsiness
        if np.random.rand()<=.001:
            step=0
        rand_walk.append(step)
    all_walks.append(rand_walk) #stores all 100 steps for 500 simulations

np_all_walks=np.array(all_walks) #500x100
#creates an array where each subarray is a single 100 step random walk
#first column is the set of all first steps in the 500 random walks 
#second column is set of all second steps in the 500 random walks 
#...
#...
#one-hundreth column is the set of all final steps of in the 500 random walks 
np_all_walks_t=np.transpose(np_all_walks) #100x500
#first row corresponds to set of all  first steps in the 500 random walks
#...
#...
#one-hundreth row corresponds to the set of all final steps in the 500 random walks 

#get the distribution of final resulting level in the building(last row)
ends=np_all_walks_t[-1,:]
print(ends)

#Plot the 500 random walks
fig=plt.figure()
ax1 = fig.add_subplot(211)
ax1.set_title('Simulation of Ten Random Walks up the Empire State Building')
ax1.set_xlabel('Random Step Number')
ax1.set_ylabel('Building Floor Number')
ax1.plot(np_all_walks_t)

#add a histogram of 500 walks endpoint distribution
ax2=fig.add_subplot(212)
ax2.set_title("Histogram of Random Walk Ending Positions")
ax2.set_xlabel("Ending Step Value")
ax2.set_ylabel("Frequency")
ax2.hist(ends)
plt.tight_layout()
plt.show()

#Find the probability of winning the bet based on 500 walk endpoints:

prob_win=len(ends[ends>=60])/float(len(ends))
print(prob_win)

#78% chance of winning the bet!

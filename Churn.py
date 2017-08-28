#Stochastic model for customer population
#time n is in months
                                #p_{n}=p_{n-1}+A_{n}-L_{n}
#p_{n} is the population at tie time n
#p_{n-1} is the population at time n-1

#A_{n} ~Brownian Motion(m_a,sigma_a)  (customer acquisition)
#L_{n}|C_{n}~Beta(C_{n}p_{n-1},p_{n-1}-C_{n}*p_{n-1})  (customer loss)
    #C_{n} ~Brownian Motion (m_churn,sigma_churn)    (customer churn)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)

#construct A_{n}-acquisition random process
#observed acquisition in the last month
mu_a=.05  #estimates from data on acquisions over past several months
sig_a=5

cn=[.10] #observed churn over the last month
mu_c=.001 #estimates from data on churn rates over past several months
sig_c=.001

all_walks=[]

for i in range(10): #500 different company paths
    pop_walk=[100] #starting population of customers for company
    for i in range(120):
        pop_step=pop_walk[-1]
        a_step=np.random.normal(loc=mu_a,scale=sig_a) #generates a_{n} value
        c_step=np.random.normal(loc=mu_c,scale=sig_c) #generates c_{n} value
        L=np.random.beta(a=max(c_step*pop_step,.001), b=max(pop_step-(c_step*pop_step),.001))
        pop_step=pop_step+a_step-L
        pop_walk.append(pop_step)

    all_walks.append(pop_walk)

np_all_walks=np.array(all_walks)

np_all_walks_t=np.transpose(np_all_walks)

#calculate the probability you end with more customers than you begin with under these particular parameter selections
ends = np_all_walks_t[ -1 ,:]
prob_gain_customers=len(ends[ends>=100])/ float (len(ends))
print(prob_gain_customers)

#plot trajectories of ten different companies, each starting with 100 customers
plt.plot(np_all_walks_t)
plt.title('Stochastic Time Series of Customer Retention')
plt.xlabel('Time (months)')
plt.ylabel('customer population')
plt.show()

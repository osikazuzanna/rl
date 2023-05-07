# Stationary bandit problem


#Import libraries
import random
import numpy as np
import matplotlib.pyplot as plt





#function for stationary problem

def bandit(N_p = 2000, N = 1000, k = 10, epsilon = 0.1):

    #number of iterations
    N = N
    # number of problems
    N_p = N_p
    #list for all the rewards for N_p problems
    all_R =[]
    # number of arms
    k = k
    # epsilon
    epsilon = epsilon

    for j in range(N_p):
    #Rewards - means of rewards
        means = [np.random.normal(loc=1.0, scale=1.0, size=None) for i in range(k)]
        
        #Initial action values
        Qa = [0.0] * k
        #Times action chosen
        Na = [0] * k
        
        Rewards = [0.0] * N

        for i in range(N):
            print('Iteration ' + str(i))
            #with prob of eps we choose a random action
            if random.random() <= epsilon:
                print('Random')
                A = int(random.randint(0, 9))
                print(A)
                Ra = np.random.normal(loc = means[A], scale = 1.0, size = None)
                print(Ra)
                Na[A] += 1
                print(Na[A])
                #update the value function of the action
                Qa[A] = Qa[A] + 1 / Na[A] * (Ra - Qa[A])
                print(Qa)
            else:
                #with prob 1-eps we choose the action with the highest value
                print('Max')
                A = Qa.index(max(Qa))
                print(A)
                Ra = np.random.normal(loc = means[A], scale = 1.0, size = None)
                print(Ra)
                Na[A] += 1
                print(Na[A])
                Qa[A] = Qa[A] + 1 / Na[A] * (Ra - Qa[A])
                print(Qa)
            #add the rewards to the list
            Rewards[i] = Ra
        #for each problem setting, append the reward list to all the reward lists
        all_R.append(Rewards)
    #calculate the average reward per iteratoin, for 2k different problems
    avg_r = [0.0] * N
    for i in range(N):
        a = 0
        for j in range(N_p):
            a = a + all_R[j][i]
        avg_r[i] = a / N_p
    return(avg_r)



    
problems = 2000
iterations = 1000
eps_01 = bandit(N_p = problems, N = iterations, k = 10, epsilon = 0.1)
eps_001 = bandit(N_p = problems, N = iterations, k = 10, epsilon = 0.01)
eps_0 = bandit(N_p = problems, N = iterations, k = 10, epsilon = 0)

plt.plot(eps_01, color = 'blue', label = 'eps01')
plt.plot(eps_0, color = 'red', label = 'eps001')
plt.plot(eps_001, color = 'green', label = 'eps0')
plt.show()
 
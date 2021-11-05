# Simulates 10K game of Hi Ho! Cherry-O 
# Setup _very_ simple timing. 

import time 
start_time = time.time() 
import multiprocessing
from statistics import mean
import random 
numGames = 10000

def cherryO(game): # This is a new function to be used for multiprocessing
    spinnerChoices = [-1, -2, -3, -4, 2, 2, 10] # everything is now indented
    turns = 0
    # totalTurns = 0
    # games = 0
# while games < 10001:  this is commented out with the new cherryO function
    # Take a turn as long as you have more than 0 cherries 
    cherriesOnTree = 10
    turns = 0
    while cherriesOnTree > 0:
        # Spin the spinner 
        spinIndex = random.randrange(0, 7)
        spinResult = spinnerChoices[spinIndex]
        # Print the spin result     
        #print ("You spun " + str(spinResult) + ".")
        # Add or remove cherries based on the result 
        cherriesOnTree += spinResult     
        # Make sure the number of cherries is between 0 and 10    
        if cherriesOnTree > 10: 
            cherriesOnTree = 10
        elif cherriesOnTree < 0: 
            cherriesOnTree = 0   
        # Print the number of cherries on the tree        
        #print ("You have " + str(cherriesOnTree) + " cherries on your tree.")     
        turns += 1
    # Print the number of turns it took to win the game 
    # print ("It took you " + str(turns) + " turns to win the game.") 
    # games += 1
    # totalTurns += turns 
    # print ("totalTurns " + str(float(totalTurns)/games)) 
    # Return the number of turns it took to win the game (new)
    return(turns)

def mp_handler(): # sets up our pool of processors and maps each of our tasks onto a worker/processor
    with multiprocessing.Pool(multiprocessing.cpu_count()) as myPool: # with ... as ... statement creates an object of the Pool class defined in the multiprocessing module and assigns it to variable myPool
                           # ^ this returns the actual number of processors on the machine i.e. transferable 
# OR (above is preferable)
# myPool = multiprocessing.Pool(multiprocessing.cpu_count())
    # code for setting up the pool of jobs
# myPool.close() # done adding jobs
# myPool.join() # clean up sub-processes to free up resources
        ## The Map function part of the MapReduce is on the right of the = and the Reduce part on the left where we are aggregating the results to a list.
        turns = myPool.map(cherryO, range(numGames)) # adds tasks/jobs to pool (of resources = workers/processors) ... list of results = map function
#     Uncomment this line to print out the list of total turns (but note this will slow down your code's execution 
#    print(turns) 
    # Use the statistics library function mean() to calculate the mean of turns 
    print(mean(turns)) 
if __name__ == '__main__': 
    mp_handler() 
    # Output how long the process took.
    print ("--- %s seconds ---" % (time.time() - start_time))
    
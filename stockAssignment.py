import random
from deap import base, creator, tools, algorithms

def genetic_algorithm_optimization_integer(func, num_variables, bounds, stock,memLen,population_size=100, generations=50):
    """
    Performs genetic algorithm optimization to minimize a given function with integer variables.

    Parameters:
    - func: The function to be minimized, which accepts up to 8 integer variables.
    - num_variables: The number of variables (up to 8) the function takes.
    - bounds: A list of tuples specifying the lower and upper bounds for each variable.
    - population_size: The size of the population (default is 100).
    - generations: Number of generations to run the algorithm (default is 50).

    Returns:
    - The best individual found by the algorithm and its fitness value.
    """
    
    # Ensure that the number of variables does not exceed 8
    # if num_variables > 8:
    #     raise ValueError("The function can have up to 8 variables only.")
    
    # Create a minimization problem
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    # Register toolbox functions
    toolbox = base.Toolbox()

    # Attribute generator: Random integer within given bounds for each variable
    toolbox.register("attr_int", random.randint, bounds[0][0], bounds[0][1])

    # Structure initializers: Define individual and population
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_int, n=num_variables)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    # Evaluation function (minimizing the given function)
    def eval_function(individual):
        
        return (func(individual, stock,memLen,),)
    
    toolbox.register("evaluate", eval_function)
    
    # Mating function: Use two-point crossover
    toolbox.register("mate", tools.cxTwoPoint)
    
    # Mutation function: Mutate by replacing a gene with a random integer within bounds
    def mut_integer(individual):
        for i in range(len(individual)):
            if random.random() < 0.2:  # Mutation probability of 20%
                individual[i] = random.randint(bounds[i][0], bounds[i][1])
        return individual,
    
    toolbox.register("mutate", mut_integer)
    
    # Selection function: Tournament selection
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Create the initial population
    pop = toolbox.population(n=population_size)

    # Genetic Algorithm parameters
    cxpb = 0.5  # Probability of crossover
    mutpb = 0.2  # Probability of mutation

    # Apply the genetic algorithm with selection, crossover, and mutation
    algorithms.eaSimple(pop, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=generations, 
                        stats=None, halloffame=None, verbose=False)
    
    # Get the best individual from the population
    best_ind = tools.selBest(pop, 1)[0]
    
    return best_ind, eval_function(best_ind)[0]

# Example usage:
# Define a sample function (for instance, a simple sum of squares function to minimize)
def example_function(assign,stock,memLen):
    # assign = [x1, x2, x3]
    # stock = [2,5,3,4,1.5]
    # memLen = [.57,.5,4.2]
    assignments = {}
    for i, a in enumerate(assign):
        el = memLen[i]
        # print(a not in assignments.keys())
        # print(assignments)
        if a not in assignments:
            assignments[a] = {
                "len":stock[a],
                "assigned":[memLen[i]]
            }
        else:
            assignments[a]['assigned'].append(memLen[i])
    # print(assignments)    
    wastedVol = 0
    
    for k,v in assignments.items():
        curWaste = v['len']-sum(v['assigned'])
        
        if curWaste<0:
            wastedVol = 10000000
        else:
            wastedVol += curWaste
    
    return wastedVol   
        
    

# stock = [2,5,3,4,1.5]
# memLen = [1,.5,4.2,6,5]
# Number of variables in the function
def memOpt(stock,memLen):
    num_vars = len(memLen)

    # Bounds for each variable (in this case, -10 to 10 for each variable)
    if num_vars ==1:
        best_solution, best_fitness = singleAssign(memLen[0],stock)
    else:
        bounds = [(0, len(stock)-1)] * num_vars
    # Perform the optimization
    # Perform the optimization
        best_solution, best_fitness = genetic_algorithm_optimization_integer(example_function, num_vars, bounds,stock,memLen)

    print("Best solution:", best_solution)
    print("Best fitness:", best_fitness)
    print('--------------------------------------')
    return best_solution, best_fitness


def assignPrep(memData,stockLib):
    stockOrder = {}
    for elem, data in memData.items():
        if data['r'] not in stockOrder:
            
            stockOrder[data['r']] = {'memLen':[data['length']],
                                     'assign':[]}
        else:
            
            stockOrder[data['r']]['memLen'].append(data['length'])
            
    for r, elemLen in stockOrder.items():
        
        stockLen = stockLib[r]['members']
        best_solution, best_fitness = memOpt(stockLen,elemLen['memLen'])
        stockOrder[r]['assign'] = best_solution
        stockOrder[r]['wasteVol'] = best_fitness
        stockOrder[r]['stockOptions'] = stockLen
        
    return stockOrder
def singleAssign(el,stock):
    wasteMin = 10000000
    matchInd = False
    for i,s in enumerate(stock):
        wasteCur = s-el
        if wasteCur<wasteMin and wasteCur>=0:
            wasteMin = wasteCur
            matchInd = i
            
    return matchInd, wasteMin
        
        
            

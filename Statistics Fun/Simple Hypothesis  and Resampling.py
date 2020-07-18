'''BACKGROUND PROBLEM form Introductory Statistics and Analytics A Resampling Perspective by Peter C. Bruce

In the fall of 2009, the Canadian Broadcasting Corporation (CBC) aired a radio news reporton a study at a hospital in Quebec. The goal of the study was to reduce medical errors.The hospital instituted a new program in which staff members were encouraged to reportany errors they made or saw being made. To accomplish that, the hospital agreed not topunish those who made errors. The news report was very enthusiastic and claimed thatmedical errors were less than half as common after the new program was begun. An almostparenthetical note at the end of the report mentioned that total errors had not changed much,but major errors had dropped from seven, the year before the plan was begun, to three, theyear after (Table 1.1)
This seems impressive, but a statistician recalling the vitamin E case might wonder if thechange is real or if it could just be a fluke of chance. '''

''' Result year one 7 major mistakes
           year two 3 major mistakes,
    Question was this due to chance, or was this due to the new policy that was put in place?
    
Head= first year, Tails= second year

Perform a test where we can check if 7 heads is indeed a plausible event or weather this is a very unlikely event.'''
import numpy as np 

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success, a.k.a HEADS
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number<p:
            n_success +=1

    return n_success
    
# Seed random number generator
np.random.seed(43)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(12)

# Compute the number of defaults
for i in range(12):
    n_defaults[i] = perform_bernoulli_trials(10,0.5)
    

event_of_7_heads = sum(n_defaults>=7)
    
#probability
probability= event_of_7_heads/12

#The probability of seeing a result as extreme as the observed value (the famous p-value)
print(probability)
    
#Alpha is 0.05
if(probability>0.05):
    print('Such result appears to not be statistically signifincant. Hence, the variation could not be explained by the alternative method (new policy)')
    
    
    
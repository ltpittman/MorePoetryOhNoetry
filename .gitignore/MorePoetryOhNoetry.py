#Imports for More Poetry? Oh Noetry!
from textblob import TextBlob
import random
import pycorpora

#My poem:
poem = """
   Within a day in November, 
   There is much snow in the sky. 
   The {0} gathers food and such,
   While the snow that fell was soft to the touch. 
   As the {1} watch from near. 
   The snow soon began to clear.
   The {2} grows in its winter fur,
   In order to keep warm from the wind's blur. 
   The {3} is in her cave to stay warm,
   To sleep all throughout the storm. 
    
 """
#Random animal choices for poem. 
animal_1 = random.choice(pycorpora.animals.common["animals"])
animal_2 = random.choice(pycorpora.animals.common["animals"])
animal_3 = random.choice(pycorpora.animals.common["animals"])
animal_4 = random.choice(pycorpora.animals.common["animals"])

#How it will be arranged in the poem:
arranged = poem.format(animal_1,animal_2,animal_3,animal_4)


print(arranged)

random.choice(pycorpora.animals.common["animals"])

pycorpora.animals.common["animals"]


!pip install pronouncing
#Keep this

import pronouncing 
pronouncing.rhymes("fur")

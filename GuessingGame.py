import random
import os


# create list
fruit = [
  "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]

vegetable = ["artichoke","asparagus","beets","broccoli","cabbage","carrot","cauliflower","celery","corn","cucumber","eggplant","garlic","greenbeans","kale","leek","lettuce","mushrooms","okra","onion","peas","peppers","potatoes","pumpkin","radishes","spinach","squash","sweetpotato","tomatoes","zucchini"]

actter = ["aamir", "amitabh", "shah rukh", "salman", "priyanka", "deepika", "kareena", "alia", "ranbir", "akshay", "ajay", "katrina", "ranveer", "varun", "tiger", "disha", "shraddha", "bhumi", "vicky", "sidharth", "kiara", "kriti", "janhvi", "sara", "ayushmann", "rajkummar", "manoj", "anil"]

country= [
  "afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda", "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "india", "botswana", "brazil", "brunei", "bulgaria", "burkinafaso", "burundi", "cambodia", "cameroon"]

objects = ['table','cheir','pen','book','car','leptop','moon','bucket','tseart','appel','school','toys','pencil','jar','banch','blackbord','mobile','wallet','bicycle']

flower = ["rose", "sunflower", "lily", "lotus", "tulip", "jasmine", "daisy", "lavender", "hibiscus", "marigold", "poppy", "carnation", "chrysanthemum", "daffodil", "orchid", "peony", "violet", "dandelion", "azalea", "camellia", "gerbera", "iris", "petunia", "zinnia", "anemone", "columbine", "freesia", "hyacinth", "narcissus", "pansy"]

plant = ["fern", "ivy", "cactus", "bamboo", "succulent", "moss", "palm", "aloe", "orchid", "bonsai", "rosemary", "lavender", "eucalyptus", "jasmine", "thyme",    "sage", "basil", "mint", "chamomile", "dandelion", "sunflower", "tulip", "daisy", "marigold", "violet", "petunia", "zinnia", "carnation", "hibiscus", "azalea"]

animal = ["ant", "bat", "cat", "dog", "elephant", "fox", "goat", "hamster", "iguana", "jaguar", "koala", "lemur", "meerkat", "newt", "otter", "panda", "quokka", "abbit", "sheep", "tiger", "unicorn", "vulture", "walrus", "x-raytetra", "yak", "zebra", "armadillo", "bison", "chameleon", "dolphin"]

bird = ["sparrow", "owl", "plover", "frigatebird", "robin", "magpie", "shrike", "harrier", "bluejay", "kingfisher", "myna", "anhinga", "finch", "mockingbird", "skylark", "gannet", "dove", "crane", "quail", "shelduck", "pigeon", "vulture", "starling", "goshawk", "crow", "cormorant", "jay", "tanager", "hawk", "toucan"]

electronic = ["resistor", "capacitor", "diode", "transistor", "inductor", "sensor", "opamp", "led", "relay", "transformer", "oscillator", "ic", "regulator","breadboard", "switch", "fuse", "connector", "motor", "encoder", "thermistor", "antenna", "speaker","microphon","mobile","Printer","camera"]

# store all list names in a list
stoke = ['electronic','bird','animal','plant','flower','objects','country','actter','vegetable','fruit']
#create a global score for storeing players store
score = 0

# store player name
name = input('Enter Your Name : ')
print(f'Welcome To Guessing Game {name} \n\t Good Luck!\n')
#chose a list randomly
lst = random.choice(stoke)
  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# difayne all logic in a function
def game():
  global lst
  #choce a word randomly
  word = random.choice(eval(lst))
  print(f'HINT : The word is {lst} Name and it has {len(word)} letters')
  print(' ----- Guess the word -----\n')
  guesses = ''
  chences = len(word)*2
  while chences > 0:
    faild = 0 
    point = 0
    for char in word: # match all letter in word from guesses
      if char in guesses:
        print(char,end=' ') #if letter match from word then print the letter
        point+=1
      else:
        print('_',end=' ') # or print '_'
        faild += 1

    if faild == 0: # if all letter match then exsecute this section
      global score
      score += (point*2) + (chences *2) # store point in score
      print(f'\n\tCongratulations! {name} You Win The Game Youre Score is {(point * 2) + (chences * 2)}')
      qs = input(f'\n\tDo You Want To Play Next Label {name} (y/n) : ')
      if qs.lower() == 'y':
        lst = random.choice(stoke)
        cls() # clear screen
        game()
      else:
        print('\n\t-------Thank You For Playing---------')
        print(f'\t-------{name} You Final Score is : {score} ---------')

        ex = input('\nQ to exit : ')
        if ex.lower() == 'q':
          quit() # exit the game
      break
      
    guess = input('\n\nGuess a character : ')
    # check some condition
    if len(guess) > 1: 
      print('\tPlease Enter Only One Character')
      continue
    elif guess in guesses: 
      print('\tYou have already guessed this character! Chose Another Letter')
      continue
    elif not guess.isalpha():
      print('\tPlease Enter Only Alphabets!')
      continue
    else:
      guesses+= guess.lower() # store all letter in a variable

    if guess not in word: # if letter not match then  print this stetment
      chences -= 1
      print('\tWrong Guess')
      print(f'You Have {chences} More Guesses To Win!')

    if chences == 0:        
      print(f'\n\t{name} You Lose The Game Your Point is {point*2}')
      print('The word is:',word)
      qs = input(f'\n\tDo You Want To Play Again {name} (y/n) : ')
      if qs.lower() == 'y':
        cls() # clear screen
        game()
      else:
        print('\n\t-------Thank You For Playing---------')
        score+=(point*2)
        print(f'\t-------{name} You Final Score is : {score} ---------')
        
        ex = input('\nQ to exit : ')
        if ex.lower() == 'q':
          quit() # exit the game
      break
      

if __name__ == "__main__":
  game()
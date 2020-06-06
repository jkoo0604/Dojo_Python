Dict = { 
    5 : 'Welcome', 
    6 : 'To', 
    7 : 'Geeks', 
    'A' : {
        1 : 'Geeks', 
        2 : 'For', 
        3 : 'Geeks'
    }, 
    'B' : {
        1 : 'Geeks', 
        2 : 'Life'
    }
} 

# Find a way to iterate through this dictionary and print the following:
# 1. Welcome to Geeks For Geeks
# 2. Welcome Geeks For Life
# 3. Geeks Welcome Geeks To Geeks For Geeks

def PrintSentence(string):
    strlist = string.split(" ")
    # print(strlist)
    type(strlist)

PrintSentence('Welcome to Geeks For Geeks')

#How to check if a value is a list or a dictionary?
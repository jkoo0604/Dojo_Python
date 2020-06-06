#<1>
x = [ [5,2,3], [10,8,9]]
students = [
    {
        'first_name': 'Michael',
        'last_name': 'Jordan'
    },
    {
        'first_name': 'John',
        'last_name': 'Rosales'
    }
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [
    {
        'x': 10,
        'y': 20
    }
]

#1 Change 10 in x to 15
x[1][0]=15
print(x)

#2 Change last_name of first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
print(students)

#3 Change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)

#4 Change 20 in z to 30
z[0]['y']=30
print(z)


#<2>
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

# def iterateDictionary(listname):
#     for i in range(len(listname)):
#         for j in listname[i]:
#             print(f"{j} - {listname[i][j]}")

# iterateDictionary(students)

def iterateDictionarynew(listname):
    for i in range(len(listname)):
        returnstr = ''
        for j in listname[i]:
            returnstr+=f"{j} - {listname[i][j]}, "
        returnstr=returnstr[:-2]
        print(returnstr)

iterateDictionarynew(students)


#<3>
#Create a function iterateDictionary2(key_name, some_list). iterateDictionary2('first_name',students) would print out Michael, John, Mark, KB.

def iterateDictionary2(key,listname):
    for i in range(len(listname)): # add if key in listname[i] then print (for edge cases)
        print(listname[i][key])

iterateDictionary2('first_name',students)

#<4>
#Create function printInfo(some_dict) that prints name of each key with the size of the list, followed by the values.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictname):
    for key in dictname:
        print(f"{len(dictname[key])} {key.upper()}")
        for item in range(len(dictname[key])):
            print(dictname[key][item])


printInfo(dojo)

#This would print out 7 LOCATIONS \n San Jose, Seattle, ... \n 8 INSTRUCTORS \n Michael, Amy, ...
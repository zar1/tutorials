## Non naive Python, torn from all over the web including: (https://www.youtube.com/watch?v=u2KZJzoz-qI) 

list_one = ['a','b','c','d']
list_four = [1,3,6,10]

#union
print "1:"
print set(list_one) | set(list_four)

#intersection
print "2:"
print set(list_one) & set(list_four)

#set difference
print "3:"
print set(list_one) - set(list_four)

#set xor
print "4:"
print set(list_one) ^ set(list_four) 

#cartesian product
from itertools import product
print "5:"
print(list(product(list_one, list_four)))

# list comprehension
print "6:"
print [x*2 for x in list_four]

#make a dict from two lists
print "7:"
print dict(zip(list_one,list_four))

# dict comprehension
print "8:"
print {k: v*2 for (k, v) in dict(zip(list_one,list_four)).iteritems()}

#lambda function
print "9:"
f =(lambda x: x*x)
print [ f(x) for x in list_four]

#lambda function
print "10:"
print [ (lambda x: x*x*2)(x) for x in list_four]

#enumerate
print "11:"
print [[idx,val ] for idx,val in enumerate(list_one)]
print [[idx,val ] for idx,val in enumerate(list_one, 100)]

#print dic keys,values, or touples
print "12:"
print dict(zip(list_one,list_four)).keys()
print dict(zip(list_one,list_four)).values()
print dict(zip(list_one,list_four)).items()

#zip
print "13:"
print zip("this","that")
print [''.join(x) for x in zip("this","that")]

#filter
print "14:"
print filter(lambda x: x % 2 == 0, list_four)

#any, all
print "15:"
print any([True, False])
print all([True, False])

#map
print "16:"
print map(lambda x: x * x, list_four)

# reduce
print "17:"
print reduce(lambda x,y: x * y, list_four)

#sum
print "18:"
print sum(list_four)

#Closure (more general)
print "19:"
def mult_by(x):
    def mult(y):
       return x * y
    return mult
mult_by_three = mult_by(3)
print mult_by_three(10)

#decorate  
print "20:"
def a(aFunc):
    def b(aString):
        return "Inner {0} Inner".format(aFunc(aString))
    return b
@a
def c(aString):
    return "outer {0} outer".format(aString)
print c("RunString")


#generators
print "21:"
def step(start=0, step=1):
    _start = start
    while True:
        yield _start  #yeild is entry and exit for generator
        _start += step        
stepper = step(10,2)
print stepper.next()
print stepper.next()

#generator expression
print "22:"
# sum([x*x for x in range(10)])
# this is the old way and less memeory effiecent
print sum(x*x for x in range(10))

#chain
print "23:"
from itertools import chain
print list(chain(list_one, list_four))
#this means that there is no list until list so you can work on long seperate lists!

#Combinaitons
print "24:"
from itertools import combinations
print list(combinations(list_one, 3))

#permutations
print "25:"
from itertools import permutations
print list(permutations(list_one, 3))

#compress
print "26:"
from itertools import compress
print (list(compress("list_one", [1,0,1,0,1,0,1,0])))
#array of 0,1's can be a function

#count
print "27:"
from itertools import count
counter = count(1,5)
print counter.next()
print counter.next()

#cycle
print "28:"
from itertools import cycle
aString = cycle("abc")
print [aString.next() for x in range(0,6)]


#groupby
print "29:"
from itertools import groupby
aString = "aaaaaaaabbbccccccc"
#print(list(groupby(aString)))  Note that return is a key and generator
print {k:list(v)for k, v in groupby(aString)}

#Fully worked example of Groupby
my_list = [
    {'id':1, 'name': "a"},
    {'id':1, 'email': "b"},
    {'id':2, 'name': "c"},
    {'id':2, 'email': "d"},
]

z= [dict(reduce(lambda y, z: y+z, 
             map(lambda x: x.items(),v)))
    for k,v in groupby(my_list,key=lambda x: x['id'])]
print z

#product
print "30:"
from itertools import product
print list(product(list_one,list_four))

#imap, ifitler, izip
#Getaddr, hasatter, setatter
print "31:"
class Bird:
    def __init__(self, airspeed, color):
        self.airspeed = airspeed
        self.color = color
aBird = Bird(25, 'black')

print getattr(aBird, 'color')
print hasattr(aBird, 'tail')

setattr(aBird, 'color', 'white')
setattr(aBird, 'nose', 'brown')
print getattr(aBird, 'color')

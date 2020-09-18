"""
For Algorithms_Questions.md/Algorithm_Answers.md
Used for working out the complexity solution.
"""
"""
* Exercise I(a)
"""
a = 0

while (a < 2 * 2 * 2): #1
    a = a + 2 * 2 #2

#ONE
#1 =>  0 < 8
#2 =>  a = 0 + 4

#TWO
#1 =>  4 < 8
#2 =>  a = 4 + 4

#1 =>  8 !< 8
## STOP

a = 0

while (a < 4 * 4 * 4):  #1
    a = a + 4 * 4       #2

#ONE
#1 =>  0 < 64
#2 =>  a = 0 + 16

#TWO
#1 => 16 < 64
#2 =>  a = 16 + 16

#THREE
#1 =>  32 < 64
#2 =>  a = 32 + 16

#FOUR
#1 =>  48 < 64
#2 => a = 48 + 16

#1 => 64 !< 64
## STOP

"""
* Exercise I(c)
"""
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)

bunnyEars(5)

####
bunnies = 5
if => pass
return 2 + bunnies(4)  #2

bunnies = 4
if => pass
return 2 + bunnyEars(3)  #4

bunnies = 3
if => pass
return 2 + bunnyEars(2) #6

bunnies = 2
if => pass
return 2 + bunnyEars(1) #8

bunnies = 1
if => pass
return 2 + bunnyEars(0) # 10

bunnies = 0
if => True
return 0 # 10


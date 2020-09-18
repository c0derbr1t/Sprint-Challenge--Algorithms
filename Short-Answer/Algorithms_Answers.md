#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This one is 𝑂(𝑛). The amount it will loop will depend on the input size 𝑛, and will grow at the same rate as 𝑛. For example: If 𝑛 = 2, then the expression will read like:
    while (a < 2 * 2 * 2):              
        a = 0 + 2 * 2 
        
    # 0 < 8 
    # a = 0 + 4

    # 4 < 8
    # a = 4 + 4

    # 8 !< 8
    # stop

And if 𝑛 = 4, then the expression will read like:
    while (a < 4 * 4 * 4):
        a = 0 + 4 * 4

    # 0 < 64
    # a = 0 + 16

    # 16 < 64
    # a = 16 + 16

    # 32 < 64
    # a = 32 + 16

    # 48 < 64
    # a = 48 + 16

    # 64 !< 64
    # stop

In each case, the amount of times the loop ran was the same as 𝑛, therefore runtime/space grew at the same rate - 𝑂(𝑛)

b) This one would be O(n^2) because there is a loop inside of a loop. It has the for loop that sets j to start at 1, and then as the range increases, increases both j (by multiplication) and sum (by addition).

    
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1



c) I believe this one is also 𝑂(𝑛). It recursively runs one time for each 𝑛 - 𝐛𝐮𝐧𝐧𝐢𝐞𝐬 is passed. 

If you call `bunnyEars(5)`, then it will run at the same rate, running 5 times while exiting on the 6th (and due to some Python 𝑀𝐴𝐺𝐼𝐶) will return the number of ears all nicely added up for you (10... who knew that 5 bunnies would usually have 10 ears? 🤷🏻‍♀️). 

If you were to call `bunnyEars(2)`, then it will run 2 times and exit on the 3rd...letting you know those 2 bunnies have 4 ears. 

If you call `bunnyEars(100)`, then it's going to do the exact same operations. It will run 100 times and exit on the 101st, and tell you that 100 bunnies have 200 ears between them.

## Exercise II

- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

-----

def broken_egg_floor(n, f):
    let the building be an array with the length being the number of stories in the building
    index 0 is the ground floor -> set it to the variable start
    index len(building) - 1 is the top floor -> set it to the variable for end
    let variable smashed_egg equal 0
    let variable whole_egg equal 0

    if start <= end
        then middle equals (start + end) // 2

        if building[middle] equals f
            whole_egg += 1
            return f"whole eggs: {whole_egg}; smashed eggs: {smashed_egg}"

        if building[middle] is less than f
            whole_egg += 1
            return recursive call to broken_egg_floor(new number of floors, f)

        else if building[middle] is greater than f
            smashed_egg += 1
            return recursive call to broken_egg_floor(new number of floors, f)

    return the top of the building if it is not found, meaning that f is higher than the top of the building.


    This is O(n) as it doesn't make any *new* lists, and really only loops once at a time.




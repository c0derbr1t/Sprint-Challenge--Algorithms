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

In each case, the amount of times the loop ran was the same as 𝑛, therefore runtime/space grew at the same rate - 𝑂(𝑛)!!!

b) ...


c) I believe this one is also 𝑂(𝑛). It recursively runs one time for each 𝑛 - 𝐛𝐮𝐧𝐧𝐢𝐞𝐬 is passed. 

If you call `bunnyEars(5)`, then it will run at the same rate, running 5 times while exiting on the 6th (and due to some Python 𝑀𝐴𝐺𝐼𝐶) will return the number of ears all nicely added up for you (10... who knew that 5 bunnies would usually have 10 ears? 🤷🏻‍♀️). 

If you were to call `bunnyEars(2)`, then it will run 2 times and exit on the 3rd...letting you know those 2 bunnies have 4 ears. 

If you call `bunnyEars(100)`, then it's going to do the exact same operations. It will run 100 times and exit on the 101st, and tell you that 100 bunnies have 200 ears between them.

## Exercise II



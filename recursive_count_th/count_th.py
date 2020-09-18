'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# time and space -> O(n)?
def count_th(word):
    # If the length of the word is less than 2, "th" cannot exist
    if (len(word) < 2):
        return 0

    # check if the first two letters of the word are "th"
        # return a recursive call of the word minus the first letter plus 1 (for the number of times "th is found") Python magic keeps track of it
    if (word[0:2] == "th"):
        return count_th(word[1:]) + 1

    # move forward one letter in the word and recursively call the function on it
    return count_th(word[1:])

a = ""
b = "abcthxyz"
c = "abcthefthghith"
d = "thhtthht"
e = "THtHThth"

print(count_th(a)) # 0
print(count_th(b)) # 1
print(count_th(c)) # 3
print(count_th(d)) # 2 
print(count_th(e)) # 1
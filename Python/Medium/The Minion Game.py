# https://www.hackerrank.com/challenges/the-minion-game/problem

"""
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
A player gets +1 point for each occurrence of the substring in the string S.
The game ends when both players have made all possible substrings.
"""

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i
    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
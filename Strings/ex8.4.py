# Strings
# Find Function modifed

import cmd2 as cmd
import twython

c = cmd.Cmd()

c.do_history()

def find(word, letter, index=0):
    while( index < len(word) ):
       if( word[index] == letter):
           return index

    return -1


print(find("Thomason", 'o', 1))



#write a function that converts quality value symbols into error rates
    #between ASCII value and Phred score
    
#ord() returns the ASCII values of the letter
#chr() returns a ASCII value into a letter

#quality value Q = -10 * math.log10(e); aka Phred quality Score; the probabilty of a based call corresponding to the based in question
# phred quality score 0 to 93, ASCII 33-126
#error rate ( end goal or starting point), score (intermediate), ASCII value(Letter and number value)
#(1)what's a phred score, (2)what are the symbols used and (3)what is the relationship
# error rate to score

# p = 10^-(q/10) 

import math
def prob_to_char(prob): # prob into ASCII
    q = - 10 * math.log10(prob) # error rate into a score
    q = int(q // 1)
    return chr(q + 33) # turns the ASCII value into a letter

def char_to_prob(char): #turns ASCII to prob
    q = ord(char) - 33
    prob = 10**-(q/10)
    return prob
print(prob_to_char(0.001))
print(char_to_prob('A'))

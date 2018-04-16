```
Yixiong Ding, <yixiongd@student.unimelb.edu.au>
4 September, 2018
The University of Melbourne 
```

import ngram
import sys

token_file = open("labelled-tokens.txt",'r')
def main():
    final_result= [0,0,0]
    temp = [0,0,0]
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    for line in token_file:
        line = line.split("\t")
        token = line[0]
        kind = line[1]
        if(len(token)== 1):
            one+=1
        if(len(token)== 2):
            two+=1
        if(len(token)== 3):
            three+=1
        if(len(token)== 4):
            four+=1
        if(len(token)== 5):
            five+=1
        if(len(token)== 6):
            six+=1
        if(len(token)== 7):
            seven+=1
        if(len(token)== 8):
            eight+=1

    print(one,two,three,four,five,six,seven,eight)

if __name__ == "__main__":
    main()
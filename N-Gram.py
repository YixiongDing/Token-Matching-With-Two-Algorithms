```
Yixiong Ding, <yixiongd@student.unimelb.edu.au>
4 September, 2018
The University of Melbourne 
```

import ngram
import sys

token_file = open("labelled-tokens.txt",'r')

def check(token, o_token):

    dict_file = open("dict.txt",'r')
    best_val = sys.maxint
    best_str = " "
    result = [0,0,0]
    result[0] += 1

    for dict_line in dict_file:
        val = ngram.NGram.compare(token, dict_line.strip(),N=2)
        if val > best_val:
            best_val = val
            best_str = dict_line.strip()
        if best_val == 1.0:
            break

    if best_str == o_token:
        #print(token,o_to>en,best_str)
        result[1] += 1
    else:
        #print(token,o_token,best_str, val, best_val)
        result[2] += 1
    return result

def main():
    final_result= [0,0,0]
    temp = [0,0,0]
    for line in token_file:
        line = line.split("\t")
        token = line[0]
        kind = line[1]
        o_token = line[2].strip("\n")
        if(kind == "OOV"):
            temp = check(token,o_token)
        final_result[0] += temp[0]
        final_result[1] += temp[1]
        final_result[2] += temp[2]

    print('\nTotal: %d\nCorrect matches: %d\nIncorrect matches: %d\nAccuracy: %.2f%%\n' %(final_result[0],final_result[1],final_result[2],final_result[1]*100.0/final_result[0]));

if __name__ == "__main__":
    main()
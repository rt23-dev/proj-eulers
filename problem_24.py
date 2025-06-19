# Lexicographic Permutations

# For digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9: total permutations: 10!
# 10! = 3628800
# We need to find the millionth. In the permutations, each digit starts 1/10th of the total. That is, 362880. 
# 362880*2 = 725760 AND 362880*3 = 1088640. This implies that the millionth lex perm must start with 2. 

# For the second digit, we have 9! = 362880 choices. Each digit comes in second place 40320 times.
# 725760+(40320*6) = 967680 AND 725760+(40320*7) = 1008000. This implies that the mill lex perm starts with 27.

# For the third digit, we have 8! = 40320 choices. Each digit comes in third place 5040 times. 
# 967680 + (5040*6) = 997920 AND 967680 + (5040*7) = 1002960. This imples that the mill lex perm starts with 278.

# For the fourth digit, we have 7! = 5040 choices. Each digit comes in fourth place 720 times. 
# 997920+(720*2) = 999360 AND 997920+(720*3) = 1000080. This implies that the mill lex perm starts with 2783.

# For the fifth digit, we have 6! = 720 choices. Each digit comes in fifth place 120 times. 
# 999360 + (120*5) = 999960 AND 999360 + (120*6) = 1000080. This implies that the mill lex perm starts with 27839.

# For the sixth digit, we have 5! = 120 choices. Each digit comes in sixth place 24 times. 
# 999960+(24*1) = 999984 AND 999960+(24*2) = 1000008. This implies that the mill lex perm starts with 278391.

# For the seventh digit, we have 4! = 24 choices. Each digit comes in seventh place 6 times. 
# 999984+(6*2) = 999996 AND 999984+(6*3) = 1000002. This implies that the mill lex perm starts with 2783915.

# For the eighth digit, we have 3! = 6 choices. Each digit comes in eighth place 2 times. 
# 999996+(2*2) = 1000000. 
# 
# Therefore, the mill lex perm is 2783915460.





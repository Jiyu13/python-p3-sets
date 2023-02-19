 # 1.
 my_list = [1, 2, 1, 3, 2]
 set(my_list)   # {1, 2, 3}

# 2.
my_string = "the big red cat ate the fat rat"
set(my_string)  # {'t', 'b', 'r', 'e', 'c', 'h', 'd', 'i', 'a', 'f', ' ', 'g'}


# 3. 
set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])   # True


# 4. use & operator to see what two sets have in common
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 & set_2  # 3

set_1 - set_2   # {1, 2}
set_2 - set_1   # {4, 5}

set_1 &= set_2
set_2 -= set_1

from typing import List


def compute_list_sum(nums : List[int]):
    """
     this fuction for calculute sum of list just numbers pairs

     parameter is list 

     return int (sum of numbers pairs)

         Exemples:
           compute_list_sum([1, 2, 3, 4, 5, 6])
         12

    
    """
    return sum(x for x in nums if x % 2 == 0)


print(compute_list_sum([1, 2, 3, 4, 5]))

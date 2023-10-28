# assignment-03

# no other imports needed
import collections

import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_match_iterative(mylist):
    def update_func(acc, char):
      return parens_update(acc, char)

    result = iterate(update_func, 0, mylist)

    return result == 0

def parens_update(current_output, next_input):
    if next_input == '(':
      return current_output + 1
    elif next_input == ')':
      return current_output - 1
    return current_output


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
    paren_values = list(map(paren_map, mylist))
    cumulative_sum, final_sum = scan(lambda x, y: x + y, 0, paren_values)
    return final_sum == 0 and all(min_f(cumulative_sum[i], 0) >= 0 for i in range(len(mylist)))

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
  """
    Recursive, divide and conquer solution to the parens match problem.
    
  Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
  """
  left_stack = []
  right_stack = []

  for char in mylist:
      if char == '(':
          left_stack.append(char)
      elif char == ')':
          if left_stack:
              left_stack.pop()
          else:
              right_stack.append(char)

  return (len(right_stack), len(left_stack))
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False

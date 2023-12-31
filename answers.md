# CMPS 2200 Assignment 3
## Answers

**Name:** Jacob Hornung


Place all written answers from `assignment-03.md` here for easier grading.


- **b.**

Because the function is iteratie work and span recurrence relations are the same and they are both W(N) = W(n-1) + O(1) (replace W with S for span respectively). This recurrence relation has a big O notation of O(n), meaning that both work and span are linear.


- **d.**

If we look at the version of scan that was provided in class (it's in the notes), then we have a work recurrence relation of W(N) = W(n/2) + n, which (in big O notation) is O(n). Likewise, the recurrence relation for span is S(n) = S(n/2) + O(1) which is equal to O(log n)


- **f.**

The work recurrence relation is W(n) = W(n/2) + O(n) because the function divides into two parts recursively, and the work at each level is O(n). Therefore, the big O notation would be W(n) = O(n log n). Because each character in the input list is processed once and individually, the span recurrence formula is S(n) = S(n-1) + O(1) which in Big O is O(n).
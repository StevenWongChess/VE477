The key in this problem is that the constrain of hc. You can do up to two homework and should follow the hc limitation. I spend a lot of time before accepting the fact that it takes 0 nanoseconds for the clever student to finish the homework.

I basically run two for loops from line 41. Brute force all the possibility of website being done by my friends. For each case, I calculate the union of several intevals. Finally, based on the result union, I use a for loop to check the gap between different intervals is enough for me to finish the calculation, since the calculation can be splited. To calculate the union, I first do the sorting, and traverse the sorted intervals to get the final union. 

Correctness

Since I can only give one or two website to my friend. I brute force all the possibilities(if some possibility break hc, I just skip it) and take the minimum for each computation. So I would not break hc and by taking minimun I can get the earliest possible finish time. After I give one or two websites to my friend, I can get the remaining websites for me to finish. Since multiple websites can be run at the same time, I only need to calculate the union of all the intervals for websites called result in my code. The bubble sort(or quick sort) is obviously correct, then a traverse all the intervals and use an easy if clause to union them one by one. The computation is decreased by the free time between two intervals accordingly. Once free time is enough, we get the finishing time and jump out. 

Time Complexity

P is the number of websites. k is the number of computations

The two for loop in line 40 takes, $O(P^2)$ In the loop, we need to set the choose array, which takes $O(P)$, then the bubble sort takes $O(P^2)$(because the test case is small, for larger test cases, we need to switch to quick sort or merge sort that only cost $O(P\log P))$. To union the sorted data, just traverse and $O(P)$. Since there can be k computations and for each of them, I need to traverse the result array, this step takes $O(k\times P)$ Thus the total complexity would be $O(P^3\times (P+k))$ for my algorithm. But for large test cases, it can be easily improved to $O(P^3\times (\log P+k))$ using merge sort or quick sort.


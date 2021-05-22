VE477 Lab 7 report

Wang Yichao

517370910011

1. RandomSearch

   (b) i. $n\log n$

   ii. n times

   iii. assume m repetition, then $\frac{n}{m}$ times needed

2. LinearSearch

   (b) i. average n times, worst n times

   ii. average $\frac{n}{2}$ times, worst n times

   iii. assume m repetition, average $\frac{n}{m}$ times, worst n-m times

3. ScrambleSearch

   (b) same as linear search

4. From the previous comparison, LinearSearch and ScrambleSearch are better (ScrambleSearch even better when the original input is not random). RandomSearch is bad because of the worst case can be infinite time(we can add a threshold so that the program is killed after 100 seconds to avoid infinite time).

5. Linear performs best. Since in our lab, the input is random, we will waste time on shuffling. For random search, the performance sucks.

   ![螢幕截圖 2020-11-17 下午9.54.02](/Users/stevenwong/Library/Application Support/typora-user-images/螢幕截圖 2020-11-17 下午9.54.02.png)
Riddler Classic - June 8, 2018

From Ben Gundry via Eric Emmet, find and replace with a twist:

Riddler Nation has been enlisted by the Pentagon to perform crucial (and arithmetical) intelligence gathering. Our mission: decode two equations. In each of them, every different letter stands for a different digit. But there is a minor problem in both equations.


## PROBLEM 1


In the first equation, letters accidentally were smudged on their clandestine journey to a safe room within Riddler Headquarters and are now unreadable. (These are represented with dashes below.) But we know that all 10 digits, 0 through 9, appear in the equation.

Given:
```
    E  X  M  R  E  E  K
+   E  H  K  R  E  K  K
 ______________________
 -  K  -  H  -  X  -  E
```

Riddle:
What digits belong to what letters, and what are the dashes?

Fortunately, we are given some information:
Each letter is a distinct digit from any other letter.
All 10 digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) appear in the equation.


Solution/Reasoning:

Immediately, knowing the sum of two digits with carryover is bounded in the range [1, 19], we can conclude that the leftmost '-' is a 1 (assuming the Riddler is not a monster who uses leading zeroes)

Starting with the right most sum, E must be even, as 2 * any number (K + K = 2K) is even. This limits E to one of (0, 2, 4, 6, 8)
Furthermore, since E + E is the leftmost pair, and yields a sum in the 10's of millions, E + E must be greater than 10 to yield that carry-over. This further limits E to one of (6, 8)
Since all letters must be digits, this narrows the possible values of K down to (3, 4)

Looking at the possible values, we have two scenarios for E and K:
1. K = 4, E = 8
	This certainly works for the ones digits (4 + 4 = 8), but we run into problems with the sum in the millions digits.
	Specifically, 8 + 8 = 16, which has a 6 in the ones place (the K value in the sum)
	Regardless of whether or not X + H has a carryover, if K is 4, 4 != 6 and 4 != 7
	Thus, K = 3, E = 6 must be true. See below:
2. K = 3, E = 6
	Again, the ones digits work (3 + 3 = 6)
	In the millions place, 6 + 6 = 12, returning a 2, which is a problem, as 2 != 3
	However, if X + H does have a carryover bit, then E + E + 1 = 6 + 6 + 1 = 13. This is possible, and everything so far has been legal.

So far, we know the following:
 * The ten millions place in the sum = 1
 * K = 3
 * E = 6
 * Our remaining digits to use are (0, 2, 4, 5, 7, 8, 9)
 * Our remaining varaibles are 	(X H M R - - -)


We can rewrite the problem as follows:
```
       (1)
        6  X  M  R  6  6  3
+       6  H  3  R  6  3  3
 __________________________
     1  3  -  H  -  X  -  6
```

At this point, we can evalueate a little bit more and figure out a few more things!

In the tens place, 6 + 3 = 9, meaning the tens '-' = 9
With no carryover from the tens place, the sum in the hundreds place is 6 + 6. This equals 12, returning a 2 in the sum in the hundreds place for X, and carrying over a 1 in the thousands place sum.


Rewriting again:
```
       (1)      (1)
        6  2  M  R  6  6  3
+       6  H  3  R  6  3  3
 __________________________
     1  3  -  H  -  2  9  6
```

At this point, we know the follwing:
 * The ten millions place in the sum = 1
 * K = 3
 * E = 6
 * The tens place in the sum = 9
 * X = 2
 * Our remaining digits to use are (0, 4, 5, 7, 8)
 * Our remaining variables are	(H M R - -)


Back to the millions place.
Since we know we need a carryover bit from the hunred-thousands from earlier, and we know that X = 2, then H must be one of (8, 9)
Furthermore, since we need to use each digit at least once, with 5 digits left to use, and 5 variables left to fill, there is no room for an extra 9.
This means that H = 8, which means the hundred thousands '-' = 0

Now, we have:
```
       (1)      (1)
        6  2  M  R  6  6  3
+       6  8  3  R  6  3  3
 __________________________
     1  3  0  8  -  2  9  6
```

We know the following:
 * The ten millions place in the sum = 1
 * K = 3
 * E = 6
 * The tens place in the sum = 9
 * X = 2
 * H = 8
 * The hundred thousands place in the sum = 0
 * Our remaining digits to use are (4, 5, 7)
 * Our remaining variables are	(M R -)


We are in the home stretch!

Looking at the remaining parts of the equation, we can see that either M + 3 = 8, or 1 + M + 3 = 8. Thus, M must be one of (4, 5)
1. M = 5
	This works in the ten thousands place (5 + 3 = 8)
	However, in the thousands place, we are left with placing 4 and 7 in a way that works.
	if R = 4, then we have 1 + 4 + 4 = 9, and 9 != 7
	if R = 7, then we have 1 + 7 + 7 = 15. There are 2 problems here: 5 != 4, and now we have a carryover into the ten thousands place, and 1 + 5 + 3 = 9, and 9 != 8
	Fortunately, the other scenario, M = 4, works
2. M = 4
	This works in the tens thousands place, with carryover (1 + 4 + 3 = 8)
	To get that carryover, R can be either of its remaining options (5, 7), but only R = 7 works.
	If R = 5, the equation in the thousands place would be 1 + 5 + 5 = 11, and 1 != 7
	If R = 7, the equation in the thousands place would be 1 + 7 + 7 = 15, and 5 = 5


With all of this information, we end up with:
```
        6  2  4  7  6  6  3
+       6  8  3  7  6  3  3
 __________________________
     1  3  0  8  5  2  9  6
```

Finally, we have filled out our equation!

We know the following:
 * The ten millions '-' = 1
 * K = 3
 * E = 6
 * The tens '-' = 9
 * X = 2
 * H = 8
 * The hundred thousands '-' = 0
 * M = 4
 * R = 7
 * The thousands '-' = 5


At last, we have 'erased' any fear of smudged numbers!


## PROBLEM 2


Riddle:
In the second equation, our mathematical spies have said that one of the letters in the equation is wrong. But they can’t remember which one. Which is it?

Given:
```
        Y  T  B  B  E  D  M  K  D
+       Y  H  D  B  T  Y  Y  D  D
 ________________________________
     E  D  Y  T  E  R  T  P  T  Y
```

Again, we are given some information:
Each letter is a distinct digit from any other letter.
With 10 letters and 10 possible digits, exactly one instance of 1 letter is wrong.

Our distinct letters are (Y, T, B, E, D, M, K, H, R, P)

Solution/Reasoning:

Here we go again! This equation starts off almost identically to the first, allowing us to use a few shortcuts from work above.
With D + D = Y in the ones place, and Y + Y = D in the hundred millions place, we can immediately notice that D = 3 and Y = 6.
Additionally, we know E must be 1, as we've established the sum of two digits can only yield a carryover of 1 (if any at all)

We can rewrite the problem already:
```
       (1)
        6  T  B  B  1  3  M  K  3
+       6  H  3  B  T  6  6  3  3
 ________________________________
     1  3  6  T  1  R  T  P  T  6
```

At this point, we know the following:
 * Y = 6
 * D = 3
 * E = 1
 * Our remaining digits to use are (0, 2, 4, 5, 7, 8, 9)
 * Our remaining varaibles are	(T B M K H R P)

Looking at the hundred thousands place, we can see B + B = 1.
B + B = 1 is only possible with a carryover, as twice the sum of any number must be an even number and 1 is not even.
Thus, B must be in the set (0, 5), and that T must be 9 to yield a carryover (1 + 9 = 10)
If T = 9, H = 7, as in the ten millions place, the sum must end in a 6
If T = 9, R = 0, as in the ten thousands place, the sum must end in a 0

Rewriting the equation with this information:
```
       (1)(1)
        6  9  B  B  1  3  M  K  3
+       6  7  3  B  9  6  6  3  3
 ________________________________
     1  3  6  9  1  0  9  P  9  6
```

At this point, we know the following:
 * Y = 6
 * D = 3
 * E = 1
 * T = 9
 * H = 7
 * R = 0
 * Our remaining digits to use are (2, 4, 5, 8)
 * Our remaining variables are	(B M K P)


From here, we can see that between the two options for B, B must be 5, as 0 + 0 = 1, and 0 + 3 != 9
We can also see that M + 6 = P must yield no carryover, as in the thousands place, 3 + 6 = 9 needs no additional 1
Using this knowledge, we can figure out the hundreds place.
With our remaining digits (2, 4, 8), the only pair that differs by 6 that is legal is (2, 8)
While 8 + 6 = 14 yields a 4 in the ones place, that forces a carryover into the thousands place, which would break the work we've done so far.
Thus, M = 2 and P = 8

We can rewrite once more:
```
       (1)(1)   (1)
        6  9  5  5  1  3  2  K  3
+       6  7  3  5  9  6  6  3  3
 ________________________________
     1  3  6  9  1  0  9  8  9  6
```

We know:
 * Y = 6
 * D = 3
 * E = 1
 * T = 9
 * H = 7
 * R = 0
 * B = 5
 * M = 2
 * P = 8
 * Our remaining digit is 		(4)
 * Our remaining variable is 	(K)


Immediately, we can see that if K = 4, 4 + 3 = 7 != 9 in the tens place. Thus the K is incorrect, and must be replaced with a Y

```
    6  9  5  5  1  3  2  6  3
+   6  7  3  5  9  6  6  3  3
 ____________________________
 1  3  6  9  1  0  9  8  9  6
```


Now, we have solved both equations. VictorK!

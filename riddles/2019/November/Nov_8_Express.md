# Riddler Express - November 8, 2019

Suppose I asked you to generate the biggest number you could using exactly three nines. Specifically, you can add, subtract, multiply, divide, exponentiate or write them side-by-side. Given this challenge, 9×9×9 is a pretty good start — it equals 729. Better yet is just writing the nines side-by-side, giving you 999. The biggest number is 9<sup>9<sup>9</sup></sup>, which equals 9387420489. If you were to write one digit of that number every second, it would take you more than a decade to write the whole thing.

Now let’s up the challenge: What’s the biggest number you can generate using exactly four threes?

## Reframing

Note: For the rest of this explanation, I will refer to writing numbers side-by-side as concatenation.

Lets break this question up into 3 different questions:

1. What's the largest number you can create with the above rules and two 3's?
2. Using that number, what's the largest number you can create with the above rules and another 3?
3. Using that number, what's the largest number you can create with the above rules and the last 3?

## Answer

1. This is pretty straightforward. To be exhaustive, we can try each operation:
    * Addition: 3 + 3 = 6
    * Subtraction: 3 - 3 = 0
    * Multiplication: 3 * 3 = 9
    * Division: 3 / 3 = 1
    * Exponentiation: 3 ** 3 = 9
    * Concatenation: 3 || 3 = 33

With just two 3's, concatenation is the operation that yields the largest number.

2. Bringing the 33 from step 1 with us, we can try the same methods again. For non-commutative operations, we will have to perform them twice, since 33 and 3 are distinct numbers:
    * Addition: 33 + 3 = 36
    * Subtraction(a): 33 - 3 = 30
    * Subtraction(b): 3 - 33 = -30
    * Multiplication: 33 * 3 = 99
    * Division(a): 33 / 3 = 11
    * Division(b): 3 / 33 = 1/11 [.09090909090909...]
    * Exponentiation(a): 33 ** 3 = 35937
    * Exponentiation(b): 3 ** 33 = 5559060566555523
    * Concatenation: 33 || 3 = 333

Bringing another 3 into the picture changes some things up. Most notably, we begin to see how exponentiation is the best operation for exploding the magnitude of numbers. More importantly, we observe that using the smaller number as the base, and larger number as the exponent, yields a much larger output than the other way around. Also, technically concatenation is not commutative, but since all of the digits in the inputs for this step are the same number (3), concatenation in either order yields the same value: 33 || 3 = 333 = 3 || 33.

3. We will repeat the process one last time, with the 5559060566555523 from step 2:
    * Addition: 5559060566555523 + 3 = 5559060566555526
    * Subtraction(a): 5559060566555523 - 3 = 5559060566555520
    * Subtraction(b): 3 - 5559060566555523 = -5559060566555520
    * Multiplication: 5559060566555523 * 3 = 16677181699666569
    * Division(a): 5559060566555523 / 3 = 1853020188851841
    * Division(b): 3 / 5559060566555523 = 1/1853020188851841 [5.39659527735429e-16]
    * Exponentiation(a): 5559060566555523 ** 3 = 171792506910670443678820376588540424234035840667 [1.717925e48]
    * Exponentiation(b): 3 ** 5559060566555523 = **undefined**
    * Concatenation(a): 5559060566555523 || 3 = 55590605665555233
    * Concatenation(b): 3 || 5559060566555523 = 35559060566555523

With the last 3, the same patterns hold true. However, the largest number was too large for my (admittedly low) efforts to evaluate to a decimal representation. We can write it as 3<sup>3<sup>33</sup></sup> or 3<sup>5559060566555523</sup>. However, I can tell you it has 2652345952577569 (about 2.65 quadrillion) digits. If you were to write one digit of that number every second, a decade wouldn't quite cut it.

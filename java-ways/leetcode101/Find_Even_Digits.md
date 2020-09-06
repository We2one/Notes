# Find even Digits

> [source](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237)

## Find Numbers with Even Number of Digits

QUESTION:

-  Given an array `nums` of integers, return how many of thme contain an __even number__ of digits

EXAMPLE 1:

```shell
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

EXAMPLE 2:

```shel
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
```

Constraints:

- `1 <= nums.length <= 500`

- `1 <= nums[i] <= 10^5`



Solutions:(Only Java for now)

```java
class Solution {
    public int counter=1;
    public int findNumbers(int[] nums) {
        int times = 0;
        for(int num:nums){
            if((getDigit(num))%2==0)
            {
                times++;
                counter=1;
            }
        }
        return times;
    }
    public int getDigit(int num) {
        if (num < 10)
            return counter;
        else {
            counter++;
            return getDigit(num / 10);
        }
    }
}
```

- There are many solutions ,the chosen solution is using `recursion`.Just for mind practice and deep inside.As God saying,”—“.
- Not best.

> One line solution using `stream`
>
> `return (int)Arrays.stream(nums).filter(i -> Integer.toString(i).length()%2==0).count();`


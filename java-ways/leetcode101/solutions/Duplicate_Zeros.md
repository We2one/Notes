```yaml
   Author: Gentleman.Hu
   Create Time: 2020-09-26 19:31:19
   Modified by: Gentleman.Hu
   Modified time: 2020-09-26 20:31:54
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Duplicate_Zeros 
> [ref](https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/)

## question:
Given a fixed length array `arr` of integers, duplicate each occurrence of zero,shifting the remaining elements to the right.

Note that elements beyond the lenght of the original array are not weitten.

Do the above modifications to the input array `in place`,do not return anything from your function.

Example 1:
```yaml
Input: []Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

Example 2:
```yaml
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
```

`Note`:

1. `1<= arr.length <= 10000`
2. `0<=arr[i] <=9`


### Solution

```java
class Solution {
    public void duplicateZeros(int[] arr) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i=0;i<arr.length;i++){
            result.add(arr[i]);
            if(arr[i]==0){
                result.add(arr[i]);
            }
        }      
        arr=result.stream().limit(arr.length).mapToInt(Integer::intValue).toArray();
    }
    
}
```

> this solution above won't accept by judge.Don't know why.

```java
class Solution {
    public void duplicateZeros(int[] arr) {
		for (int i = 0; i < arr.length - 1; i++) { //if we are on the last element it doesn't matter if it is non-zero or not
        	if (arr[i] == 0) { //if we get a zero we shift everything from the back to the right by one
        		for (int j = arr.length - 1; j > i; j--) {
        			arr[j] = arr[j - 1]; 
        		}
                i++; //if we get a zero we need to shift 'i' twice to avoid running into the zero we just duplicated
        	}
        }
    }
}
```



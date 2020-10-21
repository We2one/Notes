```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-21 08:56:42
   Modified by: Gentleman.Hu
   Modified time: 2020-10-21 09:56:15
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: #70 Climbing Stairs
 ```


## 动态规划三要素

- 最优子结构
- 边界
- 转台转移函数
  
## Climbing Stairs

> [source](https://leetcode.com/problems/climbing-stairs/)

## Question

You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb t the top?

- Example

- 1.

```yaml
Input: 2;
Output: 2
Explanation: 
- 1 step + 1 step
- 2 steps
```

- 2.

```yaml
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
- 1 step + 1 step + 1 step
- 1 step + 2 steps
- 2 steps + 1 step
```

- Constrains

> `1<=n<=45`

## Solution

### Java

- Recursive

Every time we can go `1` or `2` steps. So last step we go to top will be `1` or `2`. So `N` steps' solution stairs equals to `f(N-1)+f(N-2)`.

```java
class Solution{
	public int climbStairs(int n){
		if(n==1)
			return 1;
		if(n==2)
			return 2;
		return climbStairs(n-1)+climbStairs(n-2);
	}
}
```

- DP

```java
class Solution{
	public int climbStairs(int n){ 
		if(n==1||n==2){
			return n;
		}
		int a = 1;
		int b = 2;
		int temp = 0;
		for(int i=3;i<n+1;i++){
			temp = a + b;
			a = b;
			b = temp;
		}
		return temp;
	}
}
```

```java
class Solution {
	public int climbStairs(int n){
		if(n==1||n==2)
			return n;
		int tt[] = new int[n];

		tt[0] = 0;
		tt[1] = 1;
		tt[2] = 2;
		
		for(int i = 3;i<n;i++){
			tt[i]=tt[i-2]+tt[i-1];
		}
		return tt[n];
	}
}
```
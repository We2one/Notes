```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-14 20:05:13
   Modified by: Gentleman.Hu
   Modified time: 2020-10-14 21:11:43
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Reverse_List
 ```
## Reverse_List

> [source](https://leetcode.com/problems/reverse-linked-list/)

## Question:

Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by change the list by changing the links between node.

- Examples:

```c++
Input: Head of following linked list
1->2->3->4->NULL

Output: Linked list should be changed to,
4->3->2->1->NULL

Input: Head of following linked list
1->2->3->4->5->NULL

Output: Linked list should be changed to,
5->4->3->2->1->NULL

Input: NULL
Output: NULL

Input: 1
Output: 1
```

## One C++ Solution


- Steps
  - Initialize three pointers prev as NULL,curr as head and next as NULL.
  - Iterate through the linked list. In loop do following.
    - next = curr->next // Before changing next of current, store next node firstly.
    - curr->next = prev // Now change next of current(reverse happens here)
    - prev = curr // now prev point to current
    - curr = next // `next_current` point to `current->next` (which we store in first step)
  
- core function version

```c++
ListNode reverseList(ListNode* head){
	if(head==NULL)
		return NULL;
	if(head->next==NULL)
		return *head;
	
	ListNode* current = head;
	ListNode* prev = NULL;
	ListNode* next = NULL;
	
	while(curr!=NULL){
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;	
	}
	head = prev;

	return *head;
}

```

- full version

```c++
#include <iostream>

using namespace std;

struct ListNode{
    int val;
    struct ListNode *next;
    ListNode(int x):
            val(x),next(NULL) {
            }
};

class Solution {
    public:
        ListNode* ReverseList(ListNode* pHead){
            if(pHead==NULL) return NULL;// robustness
            ListNode* pCurrent=pHead; // current pointer
            ListNode* pPrev=NULL; // current Pointer's previous Node
            ListNode* pNext=NULL;

            while(pCurrent!=NULL){
                pNext = pCurrent->next;

                pCurrent->next = pPrev;

                pPrev = pCurrent;
                pCurrent = pNext;
            }

            pHead = pPrev;
            return pHead;
        };

        void printList(ListNode* pHead){
            for(ListNode* i=pHead;i!=NULL;i=i->next)
            {
                cout<<i->val<<","<<endl;
            }
        }
};

int main(){
    Solution* solution = new Solution();
    ListNode* l1 = new ListNode(123);
    l1->next = new ListNode(222);
    l1->next->next=new ListNode(333);

    solution->printList(l1);

    cout<<"reversed:"<<endl;

    solution->printList(solution->ReverseList(l1));
}
```

- Test output

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201014205234.png)

## One Java Recursive Solution

```java
ListNode reverseList(ListNode node,ListNode prevNode){
	if(node == null){
		return prevNode;
	}

	ListNode prevNextNode = node.next;
	node.next = prevNode;
	
	return reverseList(prevNextNode,node);
}
```

## Java Full Solution

```java
public class Main{
    public static void main(String ... args){
        System.out.println("nice world!");
        ListNode list = new ListNode(111);
        list.next = new ListNode(222);
        list.next.next = new ListNode(333);
        System.out.println("before:");
        list.printAll();
        System.out.println("after:");
        reverseList(list).printAll();
    }


    public static ListNode reverseList(ListNode head){
        if(head == null)
            return null;
        if(head.next==null)
            return head;

        ListNode current=head,next=null,prev=null;

        while(current!=null){
            next = current.next;

            current.next = prev;
            prev = current;
            current = next;
        }
        // if current is null, then last store all list is prev;
        return prev;
    }
}

class ListNode{
    int data;
    ListNode next;

    public ListNode(int data){
        this.data = data;
    }

    public void printAll(){
        for(ListNode i=this;i!=null;i=i.next)
            System.out.println(i.data+",");
    }
}
```
Output:

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201014211134.png)

## Resources

- [reverse-a-linked-list](geeksforgeeks.org/reverse-a-linked-list/)
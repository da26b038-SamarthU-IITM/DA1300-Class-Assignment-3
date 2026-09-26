# Class Assignment 3

THIS IS A REMOTE REPOSITORY CONTAINING SOLUTIONS TO THE CLASS ASSIGNMENT-3 DA1300  
SMAIL: da26b038@smail.iitm.ac.in            
ROLL NUMBER-    DA26B038   
NAME-    SAMARTH UMASHANKAR

            
This git repository contains solutions py file with functions for each question that you will be implementing, along with a public test cases evaluation script in test.py. You will have to clone this repository to your own private repo, create a fresh branch for each question as answers/q1 answers/q2 and so on, implement the solution, commit it, and merge it back into main branch. We will be evaluating on completion of git workflow tasks as well, and no marks will be given if files are directly edited online instead of following above flow.

Clone this into a private repository and add 'da26s200-byte' as a collaborator. Edit the identity.txt file with your smail and student id, and then proceed with above given instructions

## Problem 1

A shared office printer serves documents fairly rather than finishing one before
starting the next. Documents wait in a single queue, numbered `0, 1, 2, …` in the
order they were submitted. Document `i` has `pages[i]` pages.

The printer repeats this until the queue is empty:

1. Take the document at the **front** of the queue.
2. Print exactly **one page** of it.
3. If that document still has pages left, send it to the **back** of the queue.
   Otherwise it is finished and leaves the queue.

Return the document numbers in the order they **finish printing**.

Input format:
list called pages where pages[i] is the number of pages in the ith document   
Output: list giving order in which documents finished printing
eg [1,1,1] becomes [0,1,2] one page each, so submission order is preserved

## Problem 2

You are given an array `ships` representing a row of spaceships traveling along a single lane in space.
 
For each ship:
 
- `abs(ships[i])` represents its **engine power**.
- The **sign** represents its **direction**: positive means moving right, negative means moving left.
All ships travel at the same speed. When two ships moving toward each other **meet**, they collide:
 
- The ship with **lower engine power** is destroyed.
- If both ships have **equal engine power**, both are destroyed.
- Ships moving in the **same direction** never collide (they stay in formation, always maintaining spacing).
- Two ships moving in *opposite* directions only collide if the left one moves right (`+`) and the right one moves left (`−`) — i.e., they're heading toward each other.
Return the array of engine powers (with sign, preserving direction) of the ships that remain after all collisions are resolved.
 

### Example 1
```
Input:  ships = [6, 3, -5]
Output: [6]
```
**Explanation:** Ship `3` and ship `-5` collide; `-5` wins (since `5 > 3`).
Then `6` and `-5` collide; `6` wins (since `6 > 5`).
 
### Example 2
```
Input:  ships = [8, -8]
Output: []
```
**Explanation:** Equal power — both destroyed.

## Problem 3

A company's org chart is structured as a **binary tree** of employees. Each node represents an employee, and has at most two direct reports (a left report and a right report).

Each employee has a `salary` value.

For any employee `e`, define the **team average** of `e` as the average salary of `e` **and every employee in `e`'s reporting chain below them** (i.e., the entire subtree rooted at `e`), using **integer (floor) division**.

An employee is called a **fair manager** if their own salary is exactly equal to their team average.

Given the `root` of the org chart, return the **number of fair managers** in the company.

### Example 1
```
            4
          /   \
         8     5
        / \     \
       0   1     6
```
 
**Explanation:** For every employee except '8', the team average equals their own salary.

### Example 2
```
Input:  root = [1]
Output: 1
```
**Explanation:** A single employee is trivially their own fair manager: team average = 1 = salary.

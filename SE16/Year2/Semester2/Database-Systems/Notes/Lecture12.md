# Lecture 12

## SQL Statement

### Valid SQL statement

```sql
Select <column_name> | * | <built_in_functions>
From <table_name> | <view_name>
[Where <row_conditions>]
[Group By <column_list>]
[Having <group_conditions>]
[Order By <column_list>]
```

## SQL Logical Execution Sequence

1. `From`: to load table into the working buffer
2. `Where`: to check the row(s) which satisfy the query statement
3. ... (Will talk about it in the next lecture)
4. Built-in Functions

> [!NOTE]  
> At a point in time, the column name in the `Where` clause has only
> one value. It is the value of the column of the row which is being
> checked It check with the condition(s) whether to keep the row for
> result or leave it.

## SQL Built-in Functions

5 main Built-in Functions:

- Based on Columns
    - Numeric only values
        - `AVG`
        - `SUM`
    - Any values
        - `MIN`
        - `MAX`
- Based on Rows
    - `COUNT`

## Mathematical Calculation in SQL

- `+`
- `-`
- `*`
- `/`

## Key takeaway
- Sometimes SQL result may be against the Relational DB Theory. But we
can use other keyword to workaround for it. 
    - For example: 
        - `Select All`
        will provided every row and may contain duplicate rows, we can
        replace `All` with `Distinct`. (In `EX3`) 
        - `Like` and `Not Like` break the atomic principle of Relational
        DB.


## Final Leak
- None today...

## Appendix

### EX0 (Knowing how SQL statement look like)

`Student` Table:

| ID# (PK) | NAME | SCHOOL | DEPT |
| :------: | :--: | :----: | :--: |

We can convert this statement below

```
List DEPT of the Engineering school
which have at least 500 students in total
sorted by the total in descending order.
```

,to valid SQL statement below

```sql
Select DEPT, Count(*)
From Student
Where SCHOOL = 'Engineering'
Group By DEPT
Having count(*) >= 500
Order By Count(*) Desc
```

## EX1 (Republican Presidents)

Task:

```
List states in which have at least 2 Republican presidents born
```

Result SQL Statement:

```sql
Select state_born, Count(*)
From president
Where party = 'Republican'
Group By state_born
Having count(*) >= 2
Order By Count(*) Desc
```

, or

```sql
Select state_born, Count(*)
From president
Where party = 'Republican'
Group By state_born
Having Count(*) >= 2
Order By 2 Desc
```

, where 2 is a column position.

## EX2 (Recent Presidents View)

Task:

```
Drop the recent_presidents view and create it again.
```

Result SQL Statement:

```sql
Drop recent_presidents

Create View recent_presidents
As Select *
From presidents
Where birth_yr > 1880
```

### EX3 (ALL and DISTINCT IBM Chapter 5 Question 5.06 and 5.07)

#### EX3.1 (ALL Chapter 5 Question 5.06)

Task:

```
List all states where a recent president was born. Order by state
(Ascending oeder)
```

Problem: We find `Texus` twice and it violates the principle of
Relational DB where there is no duplicate rows.

#### EX3.2 (DISTINCT Chapter 5 Question 5.07)

Task:

```
List all states where a recent president was born, and eliminate
duplicates. Order by state
```

Result SQL Statement:

```sql
Select Distinct state_born
From recent_presidents
Order By state_born
```

Result SQL Statement:

### EX4 (Carter J E IBM Chapter 06 Question 6.01)

Task:

```
We want to get information of President Carter J E from the presidents
table
```

Result SQL Statement:

```sql
Select *
From presidents
Where pres_name = 'Carter J E'
```

### EX5 (AND IBM Chapter 6 Question 6.05)

Task:

```
List all facts available in the view recent_presidents about all presidents
who served more than 4 years
```

Result SQL Statement:

```
Select *
From recent_presidents
Where party = 'Republican' And state_born = 'Texus'
```

### EX6 (Republican and Democratic Presidents)

Task:

```
List rows of Republican and Democratic presidents
```

Result SQL Statement:

```sql
Select *
From recent_presidents
Where party = 'Republican' Or party = 'Democratic'
Order By party
```

> [!WARNING]  
> Common mistake:
> ```sql
> Select *
> From recent_presidents
> Where party = 'Republican' or 'Democratic'
> Order by party
> ```

### EX7 (IN (Origin: Ajarn Suphamit))

Task:

```
List all available in the view named recent_presidents that are in either
Republican or Democratic party
```

Result SQL Statement:

```sql
Select *
from presidents
Where party In ('Republican', 'Democratic')
Order By party
```

> [!NOTE]  
> Since `And`, `Or` and `In` are logical. $\therefore$ we cannot compare
> the performance as we talked in very first lectures.

### EX8 (BETWEEN IBM Chapter 6 Question 6.10)

Task:

```
List all facts available in the view named recent_presidents about all
presidents who died at an age 60 and 70 years
```

Result SQL Statement:

```sql
Select *
From recent_presidents
Where death_age >= 60 Abd death_age <= 70
```

, or

```sql
Select *
From presidents
Where _ Between 60 And 70
```

### EX9 (LIKE IBM Chapter 6 Question 6.11)

Task:

```
List all facts available in the view recent_presidents about all the
presidents whose name has the letter 'e' in the second position.
```

Result SQL Statement:

```sql
Select *
From recent_presidents
Where pres_name Like '_e%'
```

### EX10 (NOT LIKE IBM Chapter 6 Question 6.12)

Task:

```
List all facts in the view recent_presidents about all presidents whose
name has the letter 'e' in the second position, and not the letter 'R'
in the first position.
```

Result SQL Statement:

```sql
Select *
From recent_presidents
Where pres_name Like '_e%' And pres_name Not Like 'R%'
```

### EX11 (AVG IBM Chapter 7 Question 7.01)

Task:

```
Show the average age at death of the decreased presidents.
```

Result SQL Statement:

```sql
Select Avg(death_age)
From presidents
```

### EX12

Task:

```
Show the name of the president with the minimum death age with his death
age.
```


Mistaken SQL Statement:

```sql
Select pres_name, Min(death_age)
From presidents
```

This SQL statement gives syntax error.

> [!NOTE]  
> `column_name` cannot be together with `built_in_functions` in the same
> `Select` clause.

Why?

Answer:

| pres_name | Min(death_age) |
| :-------: | :------------: |
| Washington | 46 |
| ... |  |
| ... |  |
| ... |  |
| Raegan |  |

This is not a relation at all.

> [!IMPORTANT]  
> Set of values output cannot be together with single value output
> because the result is not the relation.

### EX13 (COUNT DISTINCT IBM CH01-07 P38)

Task:

```
How many individual presidents were there?
```

Result SQL Statement:

```sql
Select Count(Distinct pres_name)
From pre_marriage
```

Question: Can we

```sql
Select Count(party)
From presidents
```

Answer: Yes, but you will get the duplicate counting of parties. We can
solve by using below SQL statement instead.

```sql
Select Count(Distinct party)
From presidents
```

,so it is safer to use `Count(*)`

### EX14

Mistaken SQL Statement:

```sql
Select party, Count(*)
From presidents
Where party = 'Republican'
```

This SQL statement gives an syntax error where the DBMS believes that
`party` in `Select` clause is a `column_name`.  
We can avoid by changing `party` into a Built-in Function by `Min(party)`
or `Max(party)`.

### EX15 (Average Death Age The Harsh Way IBM CH08-12 P)

```sql
Select
```

Problems:
- `int / int` must return `int`.


```sql
Select
From presidents
Where death_age Is Not NULL
```

### EX16

Task:

```
List pres_name of presidents who served as president more than 10% of
their lives. (Consider only those who already passed away)
```

Mistaken SQL Statement:

```sql
Select pres_name
From presidents
Where (100 * yrs_serv / death_age) > 10 And death_age Is Not NULL
```

This might not be precise and give less than correct one due to IBM DBMS
use `int`.


Correct SQL Statement:

```sql
Select pres_name
From presidents
Where (100.0 * yrs_serv / death_age) > 10.0 And death_age Is Not NULL
```

,or we also can do

```sql
Select pres_name
From presidents
Where yrs_serv > 0.1 * death_age And death_age Is Not NULL
```

,in modern DBMS.

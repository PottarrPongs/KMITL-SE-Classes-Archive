# Lecture 1


## Parts

- Database $\rightarrow$ Data and relation
- Database Management System (DBMS) $\rightarrow$ Software to manage database
    - Use to present the users the logical perception of the DB
    - Mostly support only 1 type of DB Model

## Categories of DB

- Categorized by the way of arrangement (Many years ago)
    - Relational DB Model (Many to Many: Better due to the characteristic of normal data)
    - Hierarchical DB Model (One to Many: Better in some field like Banking  
    Top $\rightarrow$ Bottom: User $\rightarrow$ Accounts $\rightarrow$ Transaction History)
- Categorized by the way of arrangement (Modern)
    - SQL DB
    - No-SQL DB
- Categorized by Logical VS Physical (It depends on who we are talking to too.)
    - Logical DB $\rightarrow$ The DB we work with normally, mostly
    summarized by the DBMS.
    - Physical DB $\rightarrow$ The DB in the system.

## Why Table scan is faster than Index scan?

Answer: For DB Block Index search require more block than the table
scan $\therefore$ it is more convenience to use table scan rather than
using index scan.  
In old `Oracle DB Version`, you need to know whether to use table or
index scan to make most proficiency in querying. But the modern versions
automatically decide for you.

#### DB Admin POV:
Database Block $\rightarrow$ Logical Block
OS Block $\rightarrow$ Physical Block
#### OS Admin POV:
OS Block $\rightarrow$ Logical Block
Disk Block $\rightarrow$ Physical Block

> [!NOTE]  
>  As you can see, it depends on your role to see a Block whether it
>  is a Logical Block or Physical Block.

> [!IMPORTANT]  
> For Index scan, it is better to use integer as index rather than the
> string because integers take less space in main memory therefore more
> compatible. E.g. if you use characters (string) we have higher degree
> B-Tree to search which leads to slower querying. We need shallow B-Tree
> to be efficient. On the other hand, number of occurrence from the query
> also important. If the integer give use very high number and the string
> give us a few, it is considered that using string will be more efficient.

### 3 Factors that affect Querying

- DB Block Size
- Index Size $\rightarrow$ From choosing first index of querying
- Number of occurrence

## Query Optimizer

This is a part of the DBMS which determine the physical access root to
the result when you make query.
- Rule Based Optimizer $\rightarrow$ Use DB statistic (Parameters of the DB) to optimize.


### Database Statistic
- Size of table
- Size of row
- Availability of the table
- Availability of the access root
- The number od row return for each search condition

## Since the DB Optimizer needs to know the best access path for the query. How does the DB Optimizer know the DB Statistic?

Answer: It needs to be pre-collected by the Admin or the DBMS. Might
happen when the query traffic is low.

Example SQL:

```sql
SELECT * FROM S WHERE city='Paris' AND status=30
```

## Key Takeaway

- Never compare DB Model by performance and speed because they should
be compare in more physical level. Instead compare development
productivity and ease of use. - Not the database is not the only part that make the software run faster.
It has many other factors.
- In principle, we cannot tell the speed and performance difference
between 2 SQL prompts with different index order.
- The challenge of modern day DB performance is not from how we write
query prompt, it is from how we keep the DB Statistic.
- In SQL request, if you refer multiple tables, use cost based optimizer, 
and collect the DB statistic badly, the DBMS collects the DB Statistic
on the fly slowing down the response.

> [!NOTE]  
>  Look up for `IMS/VS`  
>  Look up for `DL/I` language  

## Database Architecture

Application and users need to see only the part of the DB relevant to
their needs

### DB Levels

3 levels of DB abstraction

- External Level (Individual user views)
- Conceptual Level (Community user views)
- Internal Level (Storage views)

#### Reasons of having multiple levels

- Privacy
- Maintenance cost
- Data Independence $\rightarrow$ Changes made in the lower level of
abstraction has nearly none or no effect on the higher level of
abstraction
    - Physical Data Independence
    - Logical Data Independence

### Why choosing DB, why not the programming language directly edit the file?

Answer: Data Independence, Productivity and Ease of Maintenance.

> [!NOTE]  
>  Levels might be different in POV of each roles.


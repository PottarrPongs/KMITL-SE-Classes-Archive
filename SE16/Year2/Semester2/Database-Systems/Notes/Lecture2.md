# Lecture 2

## From previous lecture

Back in the past, Conceptual Level of DB was the conceptual level DB.
Physical and Logical levels are not the same.  
Why do we need 3 levels?  
Data Privacy, Better Maintenance and Data Independence

## Conceptual Level of Data

Back in old days, the DB tabular and tree view were very high level at
that time but now, we now have the Entities Relation Diagram (ER Diagram)

## Conceptual Schema

There are 2 types of Conceptual Schema
- High level for better understanding in human communication (ER Diagram)
- Low Level for doing jobs in DBMS (AKA Logical Schema in current era,
to avoid being miscommunication)

## DSL

DSL stands for Data Sub Language (AKA Database Language, in current era).  
E.g. of DSL: SQL

## Conceptual View

### Conceptual Schema VS Conceptual View

Schema is Structure of the DB  
View is Data in the DB

## Internal/Physical DB

### Internal/Physical Schema

Index and files

## External Schema

Applications work with the external view

First, we have:

| X | Y | Z | W |
| :-: | :-:  | :-: | :-: |
| asdf | London | gh | True |
| asdf | Paaris | asas | True |
| haha | Bangkok | jk | False |
| llll | London | hehe | True |

To create a very simple view:
```sql
CREATE VIEW V1 (A, B, C) AS SELECT , Y, Z FROM T1 WHICH Z > 500
```

Will get like:

| A | B | C |
| :-: | :-:  | :-: |
| asdf | London | gh |
| asdf | Paris | asas |
| haha | Bangkok | jk |
| llll | London | hehe |

Then if an application want to use `A` and `C`:

```sql
SELECT A, C FROM V1 WHERE B = "London"
```

Will get like:

| A | C |
| :-: | :-: |
| asdf | gh |
| llll | hehe |

Normally the DBMS won't allocate memory for V1 but instead, it will keep
in the `System Catalog`.

### Conceptual Mapping

Query Process between layers

- External Conceptual Mapping: The query processing from View to Table
- Internal Conceptual Mapping: The query processing from Table to Files

## Materialize View

A type of view which keeps its static copy of data.  
Mostly used with data analyst.

## DB Model

What is a DB Model?  
Answer: DB Model presents data objects, relationship among them,
integrity constraints and languages for application development  

### Data Structure: What DB can see while developing
- Domain (atomic values)
- n-ary relations (attributes, tuples)

### Data Integrity: The rules to enforce correctness for the DB
- For Tables
    - Primary Key values must not be NULL
    - Foreign Key values are not match Primary key value (or be NULL)
- For Trees
    - The node of the tree can only have 1 Parent

### Data Manipulation: The languages that work on the Data Structure
- Relational Algebra (ot relational calculus equivalents):
    - Union
    - Intersection
    - Difference
    - Product
    - Select
    - Project
    - Join
    - Divide
- Relational Assignment

> [NOTE]  
> Since these SQL and NoSQL are Logical term, we cannot compare perfomance,
> like we've talked last lecture. But we can still compare on the platform
> it is running on.


## Key Takeaway

- Most Applications work with the view without directly access the Schema.
- View is the external table that Applications can use and can interact
with the table.
- If you writing a program to directly access the table, it will be
against Privacy and Data Independence which is a bad scenario for the
big enterprise organization, even though it is far more efficient.
- Most DBMS has the cache for the query whether it was once here in the
buffer before so that it will not need to be translated again.
(Query Optimization)
- The DBMS choose interpreter approach rather than compiler to use more
benefit from Data Independence and to let the DBMS to still be reusable
after some table/index were dropped but they might not affect the current
part AKA no recompiling.

> [!IMPORTANT]
> When you refer to the materials outside this class, they never talk
> about the Conceptual Schema that it is not only the ERD. So, be aware.

## Midterm Leak

- Explain the tree level architecture and demonstrate the tree level
architecture
- What is a relation?
    1. Table Structure without the data
    2. Data Rows excluding the structures ...
    3. Relationship between Tables
    4. Relationship between Entities
    - Why?
        - Answer: From the Term of Relation in Mathematics: `A relation
        in a subset of the Cartesian product of Domains`
        (Subset, in this part, is the tuples which are true.)
        (Cartesian product of Domains is the concatenation or combination
        of all domains values)  

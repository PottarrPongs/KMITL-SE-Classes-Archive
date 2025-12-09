# Lecture 3

## From previous lecture

Relations in the DB are just subset of all tuples consist of values
which are true in the given universe where the universe is the Cartesian
product of n domains where each domain is the data


## Heading Attributes (Relational Schema)

With the heading attributes we can reorder the data in the tuple but
can still make it work as normal.

(Schema means Structure)

| S |
| :-: |
| r1(S) |
| r2(S) |
| r3(S) |
| r4(S) |

We have Schema (`S`) and Relation n based on Schema S (`rn(S)`)

You may have and example of another format to represent the data in the
DB instead of table format,
e.g. we have X,Y,Z axes are schema which have P(x,y,z)
point as a tuple which is a data in the DB.

We can use cube to represent a DB
- Roll up
- Drill down

We can use different type of schema to design our DB
- Snowflake Schema
- Star Schema

## OLAP (Online Analytical Processing)

Used in Data Warehouse to show user dimensions in 3D, easier to see

## ROLAP (Relational OLAP)

OLAP on the Relational representation (for higher than 3D)

## MOLAP (Multi-Dimensional OLAP) 

OLAP on the Multi-Dimensional representation (for higher than 3D)


## Incorrect approach of SQL table

### Domain

| S# | ColumnName | Value |
| :-:| :--------: | :---: |
| S1 | SNAME | Smith |
| S1 | SSTATUS | 20 |
| S1 | CITY | London |
| ... | ... | ... |

What is wrong?
Answer: 
- It is not a relation and SQL language only works on relation
- The column must be in only 1 domain which this table has a `Value`
column with value from all the domain (this is not a relation anymore).

### Atomic value

| E# | Data | Telephone |
| :-:| :--: | :-------: |
| 1 | Data1 | 123, 234, 345 |
| 2 | Data2 | 456, 567 |

What is wrong?
Answer: From theory, we cannot obtain multiple value from
the Cartesian product of domain.

How to solve?
- Answer: 2 solutions
    - Added n column for Telephone number (drawback: fixed amount of
    numbers)
    - Create a separate table for that

#### Solution 1

| E# | Data | Telephone1 | Telephone2 | Telephone3 |
| :-:| :--: | :--------: | :--------: | :--------: |
| 1 | Data1 | 123 | 234 | 345 |
| 2 | Data2 | 456 | 678 | NULL |

#### Solution 2

| E# | Data |
| :-:| :--: |
| 1 | Data1 |
| 2 | Data2 |

| E# | Telephone |
| :-:| :-------: |
| 1 | 123 |
| 1 | 234 |
| 1 | 345 |
| 2 | 456 |
| 2 | 678 |


## Key Takeaway
- A table which represents a relation (a relational DB table) must have
the following properties:
    - An attribute belongs to only 1 domain
        - Why?
            - Answer: In 1980, KMTL used `GENDER` and `DEGREE` in the same
            column as `SEX` column. After that in 1981, they initialize
            Doctoral degree, it made the system very hard to maintain.
            Finally, in the end, they separate into 2 column. It was not
            their false because back in those days, we have limit column
            80 columns.
    - Attribute value must be atomic
        - What does atomic mean?
            - Answer: No applications access a subset of the data item
        -  Why?
            - Answer: From theory, we cannot obtain multiple value from
            the Cartesian product of domain.
    - No 2 rows are the same
        - It is set so, that all.
        - A primary key is required.
    - Rows has no order
        - Threrefore, `INSERT` command in SQL is placing new data somewhere
        in the DB. It could be anywhere in the table.
- Why Object DB cannot be used with SQL language?
    - Answer: Well it can, but you need the class attribute to be all public
    therefore, SQL can query.
- What is Object Relational DB?
    - Answer: OOP style DB

## Midterm Leak

- How can we show the data from the schema to the normal user with no
knowledge of DB system?
    - Answer: You can show table or cube or more.
- What is an SQL Table in Relational DB theory?
    - Answer: It is a variable whose values should be a relation (AKA 
    relational variable (relvar)

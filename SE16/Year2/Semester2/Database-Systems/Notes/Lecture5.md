# Lecture 5


## From previous lecture

Addition from previous lecture,

`EMP` Table:

| E#(1) | MGR#(1) | D#(2) |
| :-: | :-: | :-: |
| E10 | E1 |  D10 |

| D#(2) | ... |
| :-: | :-: |
| D10 | ... |


The `(1)` is the Relational/Foreign Key Relation within the same relation.  
The `(2)` is the Relational/Foreign Key Relation across 2 relations.

## Data Manipulation


What type of language (We tell the language what we want.)
Relational Calculus is a Non-Procedural Language which can tell the
result we want.
How type of language (We tell them step by step what we do to get the result.)
Relational Algebra is a Procedural Language which can tell how do we
do step by step to get the result.

### Relational Calculus

- Domain Relational Calculus
    - Query By Example (QBE) (created by IBM) is based on this.
- Tuple Relational Calculus
    - Structured English Query Language (SEQUEL) (created by IBM) is
    based on this. (Later changed to SQL (Structured Query Language))
    - QUEL (created by UCB) which was ran on Ingres later to be ancestor
    of Postgres.

> [!IMPORTANT]  
> For a DBMS to be called as a relational DB, they must:
> - Support Relation as Data Structure
> - Support Primary Key and Foreign Key
> - Support Relational Algebra and Relational Calculus (AKA SQL)

> [!NOTE]  
> A relational complete language is a language at least
> `as powerful (equivelent) as` the Relational Algebra or the 
> Relational Calculus.

## Database Analysis (Normalization)

Using technique called `Normalization` to check whether your DB is good
enough for the work (AKA QC standard for Relational DB Tables).

### Normal Forms

- Universe of relations 0NF (Normalized and Non-Normalized)
- 1NF relations (has all 4 basic properties)
- 2NF relations (has better `INSERT` and `DELETE`)
- 3NF relations (will be mentioned later)
- BCNF relations (will be mentioned later)
- 4NF relations (will be mentioned later)
- PJ/NF 5NF relations (no more redundancy)

#### 1st Normal Form (1NF)

- Must include 4 properties
    - An attribute belongs to only 1 domain
    - Attribute value must be atomic
    - No 2 rows are the same
    - Rows has no order

Benefits:
- No query problem

Drawbacks:
- May still have `INSERT` and `DELETE` problems

> [!NOTE]  
> We are going to talk about 2NF to 5NF in 2 upcoming classes

### Normalization Process

#### Given:
All attributes and all dependencies between related attributes.

#### Output:
Relational DB Schema (Table Structures) which guarantee minimum
or no redundancies.

#### Process:
1. Group related attributes to perform 1st draft tables. (1st Normal
Form Tables AKA 1NF)
2. For each table, check it against a higher Normal Form definition.
    - It agrees?
        - Yes, then do nothing.
        - No, then split the split it (the table).
3. Repeat step 2 until all tables agree with the 5th Normal Form (5NF).


## Key Takeaway
- Why we still use Relational DB?
    - It is still productive **`IF YOUR TABLE IS A RELATION`**.
- Problem of having redundancy in the relational DB table.
    - Insertion problem
        - Conflict fact can be inserted.
        - Some fact cannot be inserted because of Primary Key constraint
        violation.
        - The removal of a fact using delete operation may lead to the
        removal of other facts unintentionally.
- Why we worry more about `INSERTION` than `JOIN TABLE`?
    - We should care about problem that powerful hardware cannot solve
    first, then solve the hardware issues later. `INSERTION` can give
    the problem in long term in the DB.
- Why Relational DB is very high productive?
    - Answer:
        - Simple data Structures (Need certain rules)
        - Simple and powerful query language
- Normalization definition is not to split the table. It is not to split
when your tables are already agree with the current nNF.

## Midterm Leak
- Describe a DB Model (Last year 2024)
    - Answer: We need to support:
        - Support Relation as Data Structure
        - Support Primary Key and Foreign Key
        - Support Relational Algebra and Relational Calculus (AKA SQL)
- What will be a problem here in:
    - Given:
        - Query: `Q1`
        - Table: `SP'1`
    - Answer:
        - See all the `SP'1.1`, `SP'1.2` and `SP'1.3`.

## Appendix:

Table `S`:

| S# | SNAME | STATUS | CITY |
| :-: | :--: | :----: | :--: |
| S1 | Smith | 20 | London |
| S2 | Jones | 10 | Paris |

Table `P`:

| S# | PNAME | COLOR | WEIGHT | CITY |
| :-: | :--: | :----: | :----: | :--: |
| P1 | Nut | Red | 12 | London |
| P2 | Bolt | Green | 17 | Paris |
| P3 | Screw | Blue | 17 | Rome |


Table `SP`:

| S# | P# | QTY |
| :-: | :-: |:-: |
| S1 | P1 | 300 |
| S1 | P2 | 200 |
| S1 | P3 | 400 |
| S2 | P1 | 300 |

Query `Q1`:

```sql
LIST SNAME of 'London' SUPPLIER WHO supply 'Red' parts
```

Table `SP'DEFAULT` (`SP'1`):

| S#(PK) | SNAME | CITY | STATUS | P#(PK) | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | Smith | London | 20 | P2 | Bolt | Green | 200 |
| S1 | Smith | London | 20 | P3 | Screw | Blue | 400 |
| S2 | Jones | Paris | 10 | P1 | Nut | Red | 300 |

Table `SP'1.1` (INSERT INVALID DATA):

| S#(PK) | SNAME | CITY | STATUS | P#(PK) | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | Smith | London | 20 | P2 | Bolt | Green | 200 |
| S1 | Smith | London | 20 | P3 | Screw | Blue | 400 |
| S2 | Jones | Paris | 10 | P1 | Nut | Red | 300 |
| S1 | David(1) | Rome(1) | 40(1) | P4 | Screw | Red | 300 |
| S3 | Jeffrey | NewYork | 20 | P1 | Hammer(2) | Blue(2) | 100(2) |

- (1)
    - Valid insertion, due to:
        - `S1P1` $\neq$ `S1P4`
    - Problem:
        - Causation:
            - (1): `S1` was already Smith and we insert David (same to
            other attributes).
        - Consequence:
            - We might be confused later after a while.
- (2)
    - Valid insertion, due to:
        - `S1P1` $\neq$ `S3P1`
    - Problem:
        - Causation:
            - (2): `P1` was already Nut and we insert Hammer (same to
            other attributes).
        - Consequence:
            - We might be confused later after a while.

Table `SP'1.2` (NULL IN PK):

| S#(PK) | SNAME | CITY | STATUS | P#(PK) | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | Smith | London | 20 | P2 | Bolt | Green | 200 |
| S1 | Smith | London | 20 | P3 | Screw | Blue | 400 |
| S2 | Jones | Paris | 10 | NULL | NULL | NULL | NULL |

Problem:
- Invalid, due to Primary Key cannot be NULL.

Table `SP'REMOVED_PK` (`SP'2`):

| S# | SNAME | CITY | STATUS | P# | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | Smith | London | 20 | P2 | Bolt | Green | 200 |
| S1 | Smith | London | 20 | P3 | Screw | Blue | 400 |
| S2 | Jones | Paris | 10 | P1 | Nut | Red | 300 |
| S1 | David | Rome | 40 | P4 | Screw | Red | 300 |
| S3 | Jeffrey | NewYork | 20 | P1 | Hammer(1) | Blue(1) | 100(1) |

Table `SP'2.1` (NULL IN S):
| S# | SNAME | CITY | STATUS | P# | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| NULL | NULL | NULL | NULL | P2 | Bolt | Green | 200 |

Table `SP'2.2` (NULL IN S EXCEPT S#):
| S# | SNAME | CITY | STATUS | P# | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | NULL | NULL | NULL | P2 | Bolt | Green | 200 |

Table `SP'2.3` (DELETE AND LOST EVERYTHING):
| S# | SNAME | CITY | STATUS | P# | PNAME | COLOR | QTY |
| :-: | :--: | :--: | :----: | :-: | :--: | :---: | :-: |
| S1 | Smith | London | 20 | P1 | Nut | Red | 300 |
| S1 | NULL | NULL | NULL | P2 | Bolt | Green | 200 |
| ~~S5~~ | ~~Peter~~ | ~~Amsterdam~~ | ~~20~~ | ~~P1~~ | ~~Nut~~ | ~~Red~~ | ~~600~~ |

After: REMOVE S5 P1
- We just remove Peter's only information and Amsterdam only information
from the DB.

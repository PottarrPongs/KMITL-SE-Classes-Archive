# Lecture 4

## From previous lecture

In the previous lecture, we discussed the discussion of relations,
relation variables, representations of relations, and properties of
tables which correctly represent relations. Multi-dimensional
representation of relations and data warehousing are also discussed.
Examples include tables which are not relations and tables which are
relations. Atomic values principle and definition, the reason why
a relational database table should not be called a 2-dimension table
was also touched.

## Integrity Rules

Rules that enforce correctness on the data structures.

### Structural constraints
AKA DB structure (comes with DB
model or the DBMS which enforces by default)
    - Entity Integrity $\rightarrow$ Primary key values must not me NULL
    - Referential Integrity $\rightarrow$ Foreign key values must match
    primary key values (or be NULL)

#### Entity Integrity (Cont. on Key)

We have many types of keys:

- Primary Key
- Super Key
- Candidate Key
- Simple Key
- Combined Key


##### Primary Key

The main identifier which uniquely identifies a tuple. (It may comprises
more than 1 attribute.)

- We never know the primary from the data from the DB, the only way is
to get a confirmation from the DB creator.

##### Super Key

An attribute or set of attributes which uniquely identifies a tuple.

- We can detect the Super Key by inspecting whether it contains Primary
Key or not, or if the Super Key is the full tuple, it is a real Super
Key.

##### Candidate Key

A Super Key which does not have a Super Key as a subset

| S# | SNAME | STATUS | CITY |
| :-: | :--: | :----: | :--: |

Let's `assume` in this case that `SNAME` is a Super Key (which might not
in other condition) and `S#` is a Primary Key.  
Now we have:

- `S#` is a Candidate Key
- `SNAME` is a Candidate Key

| S# | P# | QTY |
| :-: | :-: | :-: |

Let's assume that `S#` and `P#` are Super Key.  
Now we have:

- `(S#, P#)` is a Candidate Key

##### Alternate Key

Candidate Key which is not the Primary Key.

##### Simple Key

A key which which comprises only 1 attribute.

##### Combined Key (Composite Key)

A Simple Key which comprises more than 1 attribute

#### Entity Integrity (Cont. on NULL)

What is NULL?

Answer:  
1. Attribute applicable but values unknown.
2. Attribute not applicable
3. In temporal DB, it means `NOW`

| E# | ENAME | SALARY | SHIFT# |
| :-: | :--: | :----: | :----: |
| Normal | Normal | NULL Type 1 | NULL Type 2 |

| E# | POSITION | FromDate | ToDate |
| :-: | :--: | :----: | :----: |
| 1 | Manager | 1 JAN 2024 | 31 DEC 9999 |
| Normal | Normal | Normal Time | Infinity Time |

`31 DEC 9999` means now but sometimes people misinterpret.

| E# | POSITION | FromDate | ToDate |
| :-: | :--: | :----: | :----: |
| 1 | Manager | 1 JAN 2024 | NULL |
| Normal | Normal | Normal Time | NULL Type 3 |

#### Referential Integrity (Cont. on Foreign Key)

A Foreign Key is a Non-Key attribute of a relation which is the Primary
Key of other relations or the same relation.

Example in `EMP` (Employyes) Table and `DEPT` (Department) Table:  

`EMP`

| E# | D# |
| :-: | :-: |
| E1 | D1 |
| E2 | D1 |
| E3 | NULL |
| E4 | D20 |

`DEPT`

| D# | DNAME |
| :-: | :--: |

From earlier defined tables we can conclude that:  
- `D#` is a Foreign Key.
- `E4` is wrong because `D20` is invalid department.
- `E3` might be the manager with no department.

```sql
CREATE TABLE DEPT (D# ...)
    PRIMARY KEY is D#
CREATE TABLE EMP (D# ... D# ...)
    PRIMARY KEY is E#, FOREIGN KEY is D# MATCH D# of DEPT,
    DEFAULT is NULL,
    UPDATE [ RESTRICTED CASCADES DEFAULT ],
    DELETE [ RESTRICTED CASCADES DEFAULT ]

```

From this query:
- We no need to say `NOT NULL` in D# since it already is a Primary Key
- `UPDATE [ RESTRICTED ]` means every update in the `D#` will be rejected.
- `UPDATE [ CASCADES ]` means when you update `D#`, e.g. `D1` to `D30`,
every `D1` will be converted to `D30`
- `UPDATE [ DEFAULT ]` means when you update `D#`, e.g. `D1` to `D30`,
every `D1` will be converted to `NULL` due `DEFAULT is NULL` in the
`CREATE TABLE` query from start.
- Same, everything from `UPDATE [ ... ]` applies to `DELETE [ ... ]`.

### Business Rule
Rules on applications (In principle, all
rules should be declared on the DB and enforced by the DBMS. (This rule
is not standard depend on each program.)
    - You can create constraints in the DB

## Key Takeaway
- If you want to decrease maintenance cost in applications, you can use
`Thin Client Fat Server` architecture where you move workload into the
server and develop mostly in there. This is better in modern days where
we have cloud servers.
- Primary Key is a selected Candidate Key.
- `Key` $\neq$ `Index`
    - Index are values which can point to Non-Key Column.
    - Primary Key might not be an index.
    - In a nutshell:
        - Key is logical: Ensure uniqueness
        - Index is physical: Ensure fast access
- DBMS will reject insertion where:
    - The new data has the duplicate Primary Key.
    - The new data Primary Key is NULL.
- Do we need meaning in the Primary Key?
    - Answer: No, the intension of Primary Key is maintain the uniqueness
    of the data not for searching up the data from query. But you can
    define a meaning of it for better understanding from human POV and
    it can narrow down the search which is done by human. (Back in old
    days, we may need a meaning for that because languages like `COBOL`
    or `RPG` need to search data from file sorted by key with meaning.)
- Same object instance must have the same identifier.
    - Main concern with example: If you study in postgraduate in the
    same university, in principle, you should retain the same student
    ID. That violate the meaning of the student ID given earlier. That
    is why it may be not a good practice sometimes you define a meaning
    to a Primary Key.

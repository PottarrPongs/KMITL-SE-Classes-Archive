# Lecture 7
## From previous lecture

Table `S`:

- PK: `S#`
- CITY $\rightarrow$ STATUS

| S# | SNAME | CITY | STATUS |
| :-: | :--: | :--: | :----: |

This table is in 2NF but not 3NF

We have integrity constraint where FD is an integrity constraint which
is given by the application environment.  

This constraint can be enforced by a procedure for `INSERT`, `UPDATE`
checking.  
But we cannot prevent the constraint from `DELETE`

Solution in 3NF:

Table `S`:

- PK: `S#`

| S# | SNAME | CITY |
| :-: | :--: | :--: |

Table `C`:
- PK: `CITY`

| CITY | STATUS |
| :--: | :----: |

Key Takeaway (Previous Lecture):
- Do not split table unless it is mandatory.
- There is no Over-Normalization.


## Boyce Codd Normal Form (BCNF)

Properties:
- Every determinant is a Candidate Key.


Table `SSP`:

- `(S#, P#)` $\rightarrow$ `QTY`
- `S#` $\rightarrow$ `SNAME`
- `SNAME` $\rightarrow$ `S#`
- `(SNAME, P#)` $\rightarrow$ `QTY`

| S# | SNAME | P# | QTY |
| :-: | :--: | :-: | :-: |

Problems (3NF Bugs):
- Table that have multiple Candidate Keys.
- Those Candidate Key are composite.
- The Candidate Key overlap

`SSP` Bug is `(S#, P#)` and `(SNAME, P#)` has `P#` overlapping.

What is determinant?:
- Answer:
    - `(S#, P#)` $\rightarrow$ `QTY`
    - `S#` $\rightarrow$ `SNAME`
    - `SNAME` $\rightarrow$ `S#`
    - `(SNAME, P#)` $\rightarrow$ `QTY`

Explanation: We have 4 FDs in this format:

$$X \rightarrow Y$$

where $X$ is determinant and $Y$ is dependent.

$\therefore$ `SSP` is not BCNF because 4 Determinants but 2 Candidate
Keys.

Solution:

Table `SS`:

- `S#` $\rightarrow$ `SNAME`
- `SNAME` $\rightarrow$ `S#`

1 Determinants 1 Candidate Keys

| S# | SNAME |
| :-: | :--: |

- `(S#, P#)` $\rightarrow$ `QTY`

2 Determinants 2 Candidate Keys

Table `SP1`:
| S# | P# | QTY |
| :-: | :-: | :-: |

Table `SP2`:

- `(SNAME, P#)` $\rightarrow$ `QTY`

1 Determinants 1 Candidate Keys

| SNAME | P# | QTY |
| :--: | :-: | :-: |

You can choose either `SP1` or `SP2`.

Go to Example `EX1`


## 4th Normal Form (4NF)

Properties:
- Included in BCNF
- Only FD, no MVD

### Multivalued Dependence
Given Relation `R` with attributes `A`, `B`, `C`:
`R` will be MVD when `A` $\rightarrow$ `B` and `A` $\rightarrow$ `C` where
`B` and `C` are independence and `A` `B` and `C` can be composite.

> [!NOTE]  
> MVD needs at least 3 attributes.

From:

`A` $\rightarrow$ $\rightarrow$ `B` $\iff$ `A` $\rightarrow$ $\rightarrow$ `C`

We can say that:

`A` $\rightarrow$ $\rightarrow$ `B | C`

> [!IMPORTANT]  
> Multivalued Dependence is a relationship between attributes where  
> MVD: LHS $\rightarrow$ $\rightarrow$ RHS

> [!NOTE]  
> FD $\subset$ MVD

> [!NOTE]  
> `R(A, B, C)` can be split into 2 projections `R1(A, B)` and `R2(A, C)`
> $\iff$ `R(A, B, C)` has MVDs.

### The Lossless Join Property

A relation `R` can be split into smaller projections $\iff$ The join (natural
join) of the projections gives the original relation `R`.

## Conceptual Modeling

We will talk about this after Normalization

## Key Takeaway
- `BCNF` does not need to be included from other previous Normal Forms.

## Midterm Leak
- None today

## Appendix

### EX1

Given:

- `S#` $\rightarrow$ `SNAME`
- `SNAME` $\rightarrow$ `CITY`
- `CITY` $\rightarrow$ `STATUS`
- `S#` $\rightarrow$ `STATUS`
- `P#` $\rightarrow$ `PNAME`
- `P#` $\rightarrow$ `PCOLOR`
- `(S#, P#)` $\rightarrow$ `QTY`

`S#` $\rightarrow$ `STATUS` is a Transitive FD, can be derived fro other
FDs bv law of Transitivity.  
We can eliminate Transitive FD.

Building BCNF Tables:

Table `S`:

| S# | SNAME | CITY |
| :-: | :--: | :--: |

Table `P`:

| P# | PNAME | COLOR |
| :-: | :--: | :---: |

Table `C`:

| CITY | STATUS |
| :--: | :----: |

Table `SP`:

| S# | P# | QTY |
| :-: | :-: | :-: |

### EX2

Context: A university where the lecturers need the textbook certified
by the university.

Table `CTX (0NF)`:

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |
| Physics | {Prof. Green, Prof. Brown} | {Basic Mechanics, Principle of Optics} |
| Math | {Prof. Green} | {Basic Mechanics, Vector Analysis, Trigonometry} |

Table `CTX (1NF, 2NF, 3NF, BCNF)`:

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |
| Physics | Prof. Green | Basic Mechanics |
| Physics | Prof. Brown | Basic Mechanics |
| Physics | Prof. Green | Principle of Optics |
| Physics | Prof. Brown | Principle of Optics |
| Math | Prof. Green | Basic Mechanics |
| Math | Prof. Green | Vector Analysis |
| Math | Prof. Green | Trigonometry |

Why it is `2NF`, `3NF`, `BCNF`?
- Answer: No FD at all

Problems (`CTX (1NF, 2NF, 3NF, BCNF)`):
- PK constraint
- `INSERT` and `DELETE` problems as `EX2.1`

Tables `EX2.1`:

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |
| Physics | Ajarn Visit | NULL |

Issues:
- Cannot be inserted because PK cannot be NULL
the list of certified Textbook

Tables `EX2.2`:

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |
| Physics | Ajarn Sun | Simple Mechanics |

Issues:
- Cannot be inserted because Simple Mechanics Textbook is not in

### EX2 Solution

In `CTX (0NF)`
- `COURSE` $\rightarrow$ $\rightarrow$ `TEACHER`
- `COURSE` $\rightarrow$ $\rightarrow$ `TEXT`

Which means:

`COURSE` $\rightarrow$ $\rightarrow$ `TEACHER | TEXT`

Building Tables `4NF`:

Table `CT`:

| COURSE | TEACHER |
| :----: | :-----: |

Table `CX`:

| COURSE | TEXT |
| :----: | :--: |




### EX3.1

Context: Supplier table where Supplier Name, City and Supplier Email
are based on Supplier Number.

Table `S`:

- PK: `S#`
- `S#` $\rightarrow$ `SNAME`
- `S#` $\rightarrow$ `CITY`
- `S#` $\rightarrow$ `EMAIL`

| S# | SNAME | CITY | EMAIL |
| :-: | :--: | :--: | :---: |

Can be split into:

- PK: `S#`

| S# | SNAME |
| :-: | :--: |

- PK: `S#`

| S# | CITY |
| :-: | :-: |

- PK: `S#`

| S# | EMAIL |
| :-: | :--: |

But it is better to keep the `S` table because `S` is already in 4NF.

### EX3.2

Context: Supplier table where City Status is based on City.

Table `S`:

- PK: `S#`
- `CITY` $\rightarrow$ `STATUS`

| S# | SNAME | CITY | STATUS |
| :-: | :--: | :--: | :----: |
 
We can split into:

| S# | SNAME | CITY |
| :-: | :--: | :--: | 

| CITY | STATUS |
| :--: | :----: |

Split because `S` is neither in 2NF nor 4NF

### EX3.3

Table `CTX`:

Context: Based on `EX2`

- `COURSE` $\rightarrow$ $\rightarrow$ `TEACHER | TEXT`

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |

We can split into:

Table `CT`:

| COURSE | TEACHER |
| :----: | :-----: |

Table `CX`:

| COURSE | TEXT |
| :----: | :--: |

### EX3.4

Context: KMITL lecturer can use their own written Textbook.

Table `CTX_KMITL`:

- `COURSE` $\rightarrow$ $\rightarrow$ `TEACHER`
- `(COURSE, TEACHER)` $\rightarrow$ $\rightarrow$ `TEXT`

| COURSE | TEACHER | TEXT |
| :----: | :-----: | :--: |

Cannot be split because no MVD. There's nothing we can do...

### EX3.5

Context: From `EX3.3` but with number of session for each
`(COURSE, TEACHER, TEXT)`.

Table `CTXN`:

- `COURSE` $\rightarrow$ $\rightarrow$ `TEACHER | TEXT`
- `(COURSE, TEACHER, TEXT)` $\rightarrow$ $\rightarrow$ `NUMBER_OF_SESSION`

| COURSE | TEACHER | TEXT | NUMBER_OF_SESSION |
| :----: | :-----: | :--: | :---------------: |

Cannot be split because no MVD. There's nothing we can do...

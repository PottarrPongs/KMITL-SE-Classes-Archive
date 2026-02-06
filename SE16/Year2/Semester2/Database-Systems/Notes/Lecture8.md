# Lecture 8

## From previous lecture

### BCNF

Properties:
- Every determinant is an Candidate Key

### 4NF

Properties:
- In `BCNF`
- Every `MVD` in `R` is `FD`

> [!NOTE]  
> `MVD` Facts:  
> - `MVD` only exists when R has 3 or more attributes.
> - `MVD` is not just Many to Many Relation, there're something more.
> - If the table has no `MVD`, then it is already 4NF.

## 5th Normal Form (5NF)

Informal Definition:

If Relation `R` cannot be split, leave it. But if `R` can be split and
every projection of `R` after the split have at least a Candidate Key
of `R`, then `R` is in the `5NF`.

> [!NOTE]  
> 5NF DOES NOT refer to 4NF, it REFERs to 1NF.


## Key Takeaway
- `5NF` are very common in real practice.

## Midterm Leak

## Appendix

### EX0

`CITY` Table:

| CITY (PK) | TABLE |
| :-------: | :---: |

`SP` Table:

| S# (PK) | P# (PK) | QTY |
| :-----: | :-----: | :-: |

`S` Table:

| S# (PK) | SNAME | CITY |
| :-----: | :---: | :--: |

`P` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

> [!NOTE]  
> All tables from `EX0` are already in 5NF even though `S` Table can
> be split into table `S1` and `S2` but it is no need since `S` Table
> is already 5NF too.

`S1` Table:

| S# (PK) | SNAME |
| :-----: | :---: |

`S2` Table:

| S# (PK) | CITY |
| :-----: | :--: |

### EX1

`S` Table:

| S# (PK) | SNAME | CITY | EMAIL |
| :-----: | :---: | :--: | :---: |

`S` Table can be split into  

`S1.1` Table:

| S# (PK) | SNAME |
| :-----: | :---: |

`S1.2` Table:

| S# (PK) | CITY |
| :-----: | :--: |

`S1.3` Table:

| S# (PK) | EMAIL |
| :-----: | :---: |

or

`S2.1` Table:

| S# (PK) | SNAME | CITY |
| :-----: | :---: | :--: |

`S2.2` Table:

| S# (PK) | EMAIL |
| :-----: | :---: |

Is `S` in 5NF?
- Answer: Yes, in both cases it can be project back into the `S` Table.

### EX2

`S` Table:

Determinator:

`CITY` $\rightarrow$ `STATUS`

| S# (PK) | SNAME | CITY | EMAIL |
| :-----: | :---: | :--: | :---: |

`S` Table can be split into  

`S_SMALL1` Table:

| S# (PK) | SNAME | CITY |
| :-----: | :---: | :--: |

`CITY` Table:

| CITY | STATUS |
| :--: | :----: |


Is `S` in 5NF?
- Answer: No, because `CITY` Table does not have CK of `S` (AKA `S#`)  
$\therefore$ We should split it more.

> [!IMPORTANT]  
> We cannot split `S` Table into `S1`, `S2` and `S3` since
> `CITY` $\rightarrow$ `STATUS`.

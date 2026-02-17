# Lecture 11

## From previous lecture

We have done some work on `EX1.0`, now we do `EX1.1`

## Identifier Problem

- How to fix:
    - Find alternative identifiers
    - Use a surrogate key (system-generated, or application-generated
    identifiers)
    - Denormalization (to avoid the join BUT will face `INSERT` and
    `DELETE` problems)

## SQL

### SQL Modes of Operation

- Interactive Mode
    - User keys query into UI and send to DBMS and DBMS sends back to
    the UI.
- Embedded Mode
    - The program sends query to the DBMS and DBMS sends back to the
    program.

## Key Takeaway
- Definition misinterpretation:
    - In `EX0` do not call `DEPARTMENT` and `EMPLOYEE` entities, they
    are entity types
    - In `EX0` do not call `WORK_FOR` relation or relationship, it is
    relation type
    - Correct Definition in `EX0`: Entity type `EMPLOYEE` has Many to 1
    relationship type of `WORK_FOR` with entity type `DEPARTMENT`.
- In `EX2`, `SUPPLIER` entities instances are the actual suppliers
themselves BUT the `PART` entity instances are not the actual parts.
- In `EX3`, `CAR` entities instances can be interpreted into many ways:
    - Actual car itself individually
    - Car model
    - Solution: Make 2 entity types, `CAR` and `CAR_MODEL` where many
    `CAR` entity instances can be in 1 `CAR_MODEL` entity instance by
    using `HAS` relationship instances as `CAR` `HAS` `CAR_MODEL` by
    Many to 1.

## Final Leak
- None today...

## Appendix

### EX0

```mermaid
flowchart TD

    %% Entity Types %%

    %% Employee %%
    EM[Employee]
        EM_SSN([Social Security Number])
        EM_MORE([...])

    %% Project %%
    PJ[Project]
        PJ_NO([Project Number])
        PJ_MORE([...])

    %% Department %%
    DP[Department]
        DP_NO([Department Number])
        DP_MORE([...])

    %% Dependent %%
    DD[Dependent]
        DD_NAME([Name])
        DD_MORE([...])

    %% Relationship Types %%
    SV{Supervision}
    WF{Work For}
    MG{Manager}
        MG_SDATE([Start Date])
    WO{Work On}
        WO_HR([Hours])
    CT{Control}
    DF{Dependent of}

    %% Label %%
    LB11[1 Supervisor]
    LB12[1]
    LB13[1]
    LB14[1]
    LB15[1]
    LB16[1]
    LBM[m]
    LBN1[n Supervisee]
    LBN2[n]
    LBN3[n]
    LBN4[n]
    LBN5[n]

    %% Mapping %%
    EM ---- EM_SSN
    EM ---- EM_MORE

    PJ ---- PJ_NO
    PJ ---- PJ_MORE

    DP ---- DP_NO
    DP ---- DP_MORE

    DD ---- DD_NAME
    DD ---- DD_MORE

    MG ---- MG_SDATE

    WO ---- WO_HR

    EM ---- LB11 ---- SV
    SV ---- LBN1 ---- EM

    EM ---- LB12 ---- DF
    DF ==== LBN2 ==== DD

    EM ==== LBN3 ==== WF
    WF ==== LB13 ==== DP

    EM ---- LB14 ---- MG
    MG ---- LB15 ---- DP

    EM ==== LBM ==== WO
    EM ==== LBN4 ==== PJ

    DP ---- LB16 ---- CT
    CT ==== LBN5 ==== PJ
```

### EX1.0

```mermaid
flowchart TD

    %% Entity Types %%

    %% Student %%
    ST([Student])
        ST_ID(["<u>ID</u>"])
        ST_NAME([Name])
        ST_ADDR([Address])
        ST_CLAS([Class])
        ST_HPHN([Home Phone Number])

    %% Book %%
    BK([Book])
        BK_SID(["<u>Serial Registration ID</u>"])
        BK_NAME([Book Name])
        BK_ANAM([Author Name])
        BK_PUBL([Publisher])
        BK_YEAR([Year Published])
        BK_CANO([Call Number])

    %% Magazine %%
    MG([Magazine])
        MG_SID(["<u>Serial Registration ID</u>"])
        MG_NAME([Magazine Name])
        MG_PUBL([Publisher])
        MG_VOLN([Volume Number])
        MG_YEAR([Year Issued])
        MG_MONT([Month Issued])
        MG_CATE([Category])

    %% Relationship Types %%

    BBR{Borrow Book}
    MBR{Borrow Magazine}

    %% Label %%
    LB11[1]
    LB12[1]
    LBM[m]
    LBN[n]

    %% Mapping %%
    ST ---- ST_ID
    ST ---- ST_NAME
    ST ---- ST_ADDR
    ST ---- ST_CLAS
    ST ---- ST_HPHN

    BK ---- BK_SID
    BK ---- BK_NAME
    BK ---- BK_ANAM
    BK ---- BK_PUBL
    BK ---- BK_YEAR
    BK ---- BK_CANO

    MG ---- MG_SID
    MG ---- MG_NAME
    MG ---- MG_PU
    MG ---- MG_VOLN
    MG ---- MG_YEAR
    MG ---- MG_MONT
    MG ---- MG_CATE


    BK ---- LB12 ---- BBR
    BBR ---- LBM ---- ST
    MG ---- LB11 ---- MBR
    MBR ---- LBN ---- ST
```

`BOOK` Table:

| BSID (PK) | BNAME | ANAME | PUBLISHER | PUBL_YEAR | CALL_NO |
| :-------: | :---: | :---: | :-------: | :-------: | :-----: |

`MAGAZINE` Table:

| MSID (PK) | MNAME | PUBLISHER | VOL_NO | PUBL_YEAR | PUBL_MONTH | CATEGORY |
| :-------: | :---: | :-------: | :----: | :-------: | :--------: | :------: |

`STUDENT` Table:

| ID (PK) | SNAME | ADDRESS | CLASS | PHONE |
| :-----: | :---: | :-----: | :---: | :---: |

`BK_BORROW` Table:

| ID (PK, FK) | BSID (PK, FK) |
| :---------: | :-----------: |

`MG_BORROW` Table:

| ID (PK, FK) | MSID (PK, FK) |
| :---------: | :-----------: |

### EX1.1

```mermaid
flowchart TD

    %% Entity Types %%

    %% Student %%
    ST([Student])
        ST_ID(["<u>ID</u>"])
        ST_NAME([Name])
        ST_ADDR([Address])
        ST_CLAS([Class])
        ST_HPHN([Home Phone Number])

    %% Book %%
    BK([Book])
        BK_SID(["<u>Serial Registration ID</u>"])
        BK_NAME([Book Name])
        BK_ANAM([Author Name])
        BK_PUBL([Publisher])
        BK_YEAR([Year Published])
        BK_CANO([Call Number])

    %% Magazine %%
    MG([Magazine])
        MG_SID(["<u>Serial Registration ID</u>"])
        MG_NAME([Magazine Name])
        MG_PUBL([Publisher])
        MG_VOLN([Volume Number])
        MG_YEAR([Year Issued])
        MG_MONT([Month Issued])
        MG_CATE([Category])

    %% Relationship Types %%

    BBR{Borrow Book}
    MBR{Borrow Magazine}

    %% Label %%
    LB11[1]
    LB12[1]
    LBM[m]
    LBN[n]

    %% Mapping %%
    ST ---- ST_ID
    ST ---- ST_NAME
    ST ---- ST_ADDR
    ST ---- ST_CLAS
    ST ---- ST_HPHN

    BK ---- BK_SID
    BK ---- BK_NAME
    BK ---- BK_ANAM
    BK ---- BK_PUBL
    BK ---- BK_YEAR
    BK ---- BK_CANO

    MG ---- MG_SID
    MG ---- MG_NAME
    MG ---- MG_PU
    MG ---- MG_VOLN
    MG ---- MG_YEAR
    MG ---- MG_MONT
    MG ---- MG_CATE


    BK ---- LBM ---- BBR
    BBR ---- LB11 ---- ST
    MG ---- LBN ---- MBR
    MBR ---- LB12 ---- ST
```

> [!NOTE]  
> Don't forget to add `TEACHER` on the mermaid on the top diagram

`BOOK` Table:

Determinant:
- `CALL_NO` $\rightarrow$ `BNAME`
- `CALL_NO` $\rightarrow$ `PUBLISHER`
- `CALL_NO` $\rightarrow$ `A1`
- `CALL_NO` $\rightarrow$ `A2`
- `CALL_NO` $\rightarrow$ `A3`

| BSID (PK) | BNAME | A1 | A2 | A3 |PUBLISHER | PUBL_YEAR | CALL_NO | ID (FK) | BORROW_DATE |
| :-------: | :---: | :-: | :-: | :-: | :---: | :-------: | :-----: | :-----: | :---------: |

`MAGAZINE` Table:

Determinant:
- `MNAME` $\rightarrow$ `PUBLISHER`
- `MNAME` $\rightarrow$ `CATEGORY`

| MSID (PK) | MNAME | PUBLISHER | VOL_NO | PUBL_YEAR | PUBL_MONTH | CATEGORY | ID (FK) | BORROW_DATE |
| :-------: | :---: | :-------: | :----: | :-------: | :--------: | :------: | :-----: | :---------: |

`STUDENT` Table:

| ID (PK) | SNAME | ADDRESS | PHONE | CLASS | TEACHER |
| :-----: | :---: | :-----: | :---: | :---: | :-----: |

We can normalize them to 5NF:

`TITLE_BOOK` Table:

- Added `ISBN` to be PK

| ISBN (PK) | CALL_NO | BNAME | PUBLISHER | A1 | A2 | A3 |
| :-------: | :-----: | :---: | :----: | :-: | :-: | :-: |

`BOOK` Table:

| BSID (PK) | CALL_NO (FK) | ID | BORROW_DATE |
| :-------: | :----------: | :-: | :--------: |

`TITLE_MAGAZINE` Table:

- Added `M#` to be PK

| M# (PK) | MNAME | PUBLISHER | CATEGORY |
| :-----: | :---: | :-------: | :------: |

`MAGAZINE` Table:

| MSID (PK) | MNAME (FK) | VOL_NO | PUBL_MONTH | PUBL_YEAR |
| :-------: | :--------: | :----: | :--------: | :-------: |

`STUDENT` Table:

| ID (PK) | SNAME | ADDRESS | PHONE | CLASS |
| :-----: | :---: | :-----: | :---: | :---: |

`CLASS` Table:

| CLASS (PK) | TEACHER |
| :--------: | :-----: |

### EX2

### EX3

`CAR` Table:

| CREG# (PK) | ... | CM# (FK) |
| :--------: | :-| :------: |

`CAR_MODEL` Table:

| CM# (PK) | ... |
| :------: | :-: |

### EX4 (library on Steroid)

```mermaid
flowchart TD
```

`TITLE_BOOK` Table:
`BOOK` Table:
`TITLE_MAGAZINE` Table:
`MAGAZINE` Table:
`STUDENT` Table:

### EX5 (Book Borrowing on Steroid)

```mermaid
flowchart TD
```

One student may have many books borrwed but each book may only belongs
one student at the same time.

We need an identifier to identify each relationship instance.
$\therefore$ we need to change `BK_BORROW` from relationship type to
be an entity type which we call it an `Associate Entity Type`
(Entity Type which was once a Relationship Type).

### EX6 (Sport Equipment Set Borrow)

`STUDENT` Table:

| ID (PK) | ... |
| :-----: | :-: |

`ITEM` Table:

| I# (PK) | ... |
| :-----: | :-: |

`ITEM_BORROW` Table:

| IB# (PK) | ... | ID (FK) |
| :------: | :-: | :-----: |

`HAS` Table:

| IB# (PK) | I# |
| :-----: | :-: |

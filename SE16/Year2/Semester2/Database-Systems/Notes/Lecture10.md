# Lecture 10

## Mapping ERD to Relational Table

> [!IMPORTANT]  
> The mapping are not going to guarantee to map to 3NF since they still
> are no FD. (See in Appendix EX1)

See mostly in Appendix

## Key Takeaway
- After mapping from ERD, the tables are not guarantee to be 3NF.

## Final Leak
- None today...

## Appendix

### Case Study (Religion Talk)

### EX1.0: Supply

```mermaid
flowchart TD
    %% Types %%
    SUPPLIER["SUPPLIER"]
        SUPPLIER_S#(["<u>S#</u>"])
        SUPPLIER_SNAME([SNAME])
        SUPPLIER_CITY([CITY])
        SUPPLIER_STATUS([STATUS])
    PART["PART"]
        PART_P#(["<u>P#</u>"])
        PART_PNAME([PNAME])
        PART_COLOR([COLOR])
    SUPPLY{"SUPPLY"}
        SUPPLY_QTY([QTY])

    %% Mapping %%
    SUPPLIER ---- SUPPLIER_S#
    SUPPLIER ---- SUPPLIER_SNAME
    SUPPLIER ---- SUPPLIER_CITY
    SUPPLIER ---- SUPPLIER_STATUS

    PART ---- PART_P#
    PART ---- PART_PNAME
    PART ---- PART_COLOR

    SUPPLY ---- SUPPLY_QTY

    SUPPLIER ---- SUPPLY
    SUPPLY ---- PART
```

`SUPPLIER` Table:

- `CITY` $\rightarrow$ `STATUS`

| S# (PK) | SNAME | CITY | STATUS |
| :-----: | :---: | :--: | :----: |

`PART` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

`SUPPLY` Table:

| S# (PK) | P# (PK) | QTY |
| :-----: | :-----: | :-: |

### EX1.1

| S# (PK) | SNAME | CITY | STATUS | P# (PK) | PNAME | COLOR | QTY |
| :-----: | :---: | :--: | :----: | :-----: | :---: | :---: | :-: |

> [!IMPORTANT]  
> From EX1.1, from here if the ERD has `1 - 1` relationship types. We
> cannot map it into a big table.

> [!NOTE]  
> We can map `1 - 1` relationship into 2 ways. (See in EX1.2)

### EX1.2.1

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS |
| :-----: | :---: | :--: | :----: |

`PART` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

`SUPPLY` Table:

| S# (PK) | P# (PK) | QTY |
| :-----: | :-----: | :-: |

### EX1.2.2.1

In this case, we extend the `SUPPLIER` Table.
This is useful when the query are mainly ask for supplier details, else
we need to join table.

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS | P# (FK) | QTY |
| :-----: | :---: | :--: | :----: | :-----: | :-: |

`PART` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

### EX1.2.2.2

In this case, we extend the `PART` Table.
This is useful when the query are mainly ask for part details, else we
need to join table.

`PART` Table:

| P# (PK) | PNAME | COLOR | S# (FK) | QTY |
| :-----: | :---: | :---: | :-----: | :-: |

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS |
| :-----: | :---: | :--: | :----: |

### EX1.3

When the relationship types is `1 - Many`, the only correct way is

`PART` Table:

| P# (PK) | PNAME | COLOR | S# (FK) | QTY |
| :-----: | :---: | :---: | :-----: | :-: |

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS |
| :-----: | :---: | :--: | :----: |

If we use this (which is wrong)

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS | P# (FK) | QTY |
| :-----: | :---: | :--: | :----: | :-----: | :-: |

`PART` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

It will have the array of `(P#, QTY)` which violate the rule of
Relational DB.

### EX1.4

When the relationship types is `Many - Many`, the only correct way is

In this case, we must use the 3rd table.

`SUPPLIER` Table:

| S# (PK) | SNAME | CITY | STATUS |
| :-----: | :---: | :--: | :----: |

`PART` Table:

| P# (PK) | PNAME | COLOR |
| :-----: | :---: | :---: |

`SUPPLY` Table:

| S# (PK) | P# (PK) | QTY |
| :-----: | :-----: | :-: |

> ![IMPORTANT]  
> BUT we cannot conclude that it is in 3NF, since we have not known about
> `CITY` $\rightarrow$ `STATUS` FD.

### EX2: Case Study (Religion Talk) (Cont.)

```mermaid
flowchart TD

    %% Entity Types %%

    RELIGION[RELIGION]
        RELIGION_RCODE(["<u>RCODE</u>"])
        RELIGION_RNAME([RNAME])
        RELIGION_TNAME([TNAME])
        RELIGION_ADHERENT([ADHERENT])
    TEXT[TEXT]
        TEXT_TXCODE(["<u>TXCODE</u>"])
        TEXT_TEXT([TEXT])
        TEXT_TXNAME([TXNAME])
    SPEAKER[SPEAKER]

    %% Relationship Types %%
    READ[READ]
    SPEAK[SPEAK]
        SPEAK_NO_SESSION([NO_SESSION])

    %% Mapping %%
    RELIGION ---- RELIGION_RCODE
    RELIGION ---- RELIGION_RNAME
    RELIGION ---- RELIGION_TNAME
    RELIGION ---- RELIGION_ADHERENT

    TEXT ---- TEXT_TXCODE
    TEXT ---- TEXT_TEXT
    TEXT ---- TEXT_TXNAME

    SPEAK ---- SPEAK_NO_SESSION

    RELIGION ---- SPEAKER
    SPEAKER ---- TEXT
```


`RELIGION` Table:

| RCODE (PK) | RNAME | TNAME | ADHERENT |
| :--------: | :---: | :---: | :------: |

`TEXT` Table:

| TXCODE (PK) | TEXT | TXNAME | RCODE (FK) |
| :---------: | :--: | :----: | :--------: |

`SPEAKER` Table:

| SNAME (PK) |
| :--------: |

`READ` Table:

| SNAME (PK, FK) | TXCODE (PK, FK) |
| :------------: | :-------------: |

`SPEAK` Table:

| SNAME (PK, FK) | RCODE (PK, FK) | NO_SESSION |
| :------------: | :------------: | :--------: |

> [!NOTE]  
> `RELIGION`, `TEXT` and `SPEAKER` Tables represent entity schema where
> relations there represent entity instances.  
> `READ` and `SPEAK` Tables represent relationship types where
> relations there represent relationship instances.

> [!TIP]  
> Sometimes, entity table can be called `Master Table`.
> Also, relationship table can be called `Transaction Table` too.

> [!NOTE]  
> `SPEAKER` Table is a table with unary relation.

Now, we shall normalize it to 5NF. (We added Alternate Key to let you
know more.)

`RELIGION` Table:

| RCODE (PK) | RNAME (AK) | TNAME (AK) | ADHERENT |
| :--------: | :--------: | :--------: | :------: |

`TEXT` Table:

| TXCODE (PK) | TEXT (AK) | TXNAME | RCODE (FK) |
| :---------: | :-------: | :----: | :--------: |

`SPEAKER` Table:

| SNAME (PK) |
| :--------: |

`READ` Table:

| SNAME (PK, FK) | TXCODE (PK, FK) |
| :------------: | :-------------: |

`SPEAK` Table:

| SNAME (PK, FK) | RCODE (PK, FK) | NO_SESSION |
| :------------: | :------------: | :--------: |

Yes, the same set of tables...  
$\therefore$ it is already in 5NF.

### EX3: Employees and Departments

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

### EX4: Case Study (Library)

Given Properties:
- Book
    - Book Name
    - Author Name
    - Publisher
    - Year Published
    - Call Number
    - Serial Registration Number
- Magazine
    - Magazine Name
    - Magazine Publisher
    - Magazine Volume Number
    - Month Issued
    - Year Issued
    - Category
    - Serial Registration Number
- Student
    - ID
    - Name
    - Address
    - Class
    - Home Phone Number

We can draw as ERD as follow:

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

We can separate into tables as follow:

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

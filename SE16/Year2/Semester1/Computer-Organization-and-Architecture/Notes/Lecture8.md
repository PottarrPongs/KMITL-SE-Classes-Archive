# Lecture 8: Pipelining

```
LD r0, r1, #5
```

```
Instruction RegisterDestination  RegisterSource, Operand
```

We use 5 CLK Cycle to finish 1 Instruction (CPI (CLK Cycle Per Instruction) = 5)

The minimum CPI is 5 where the worst case is calculate by `LongestDelay - CriticalPath`

## Pipelining Register (Pipeline Latch)

- PL is a special register placed between stages of pipeline in a processor

## Instruction Cycle

From Lecture 4, we have metioned that, to complete an instruction we
need to do 5 steps (1 per a CLK cycle)  
1. Fetch $\rightarrow$ Access instruction memory
2. Decode $\rightarrow$ Decode instruction and read source registers
3. Execute $\rightarrow$ Perform an ALU operation, calculate a memory
address, or compute a branch target address.
4. Memory $\rightarrow$ Access data memory
5. Store $\rightarrow$ Write to the register file

## Stall

## An Ideal Pipeline (Pipelining without Stall)

## Stalling to Access Memory

The latency of accessing off-chip memory (DRAM) is typically 10-100 times
higher than our pipelined processor's clocl period.

In order to avoid stalling, we must use the on-chip `caches`.

## Cache Hit/Miss Penalties and Impact on Performance

| Cache Level | Hit Penalty (Cycles) | Miss Penalty (Cycles) | Notes |
| :---------: | :------------------: | :-------------------: | :---: |
| L1 (Instruction/Data) | 1-2 | 10-20 (to L2) | Small, fast |
| L2 (Unified) | 10-20 | 50-100 (to L3 or DRAM) | Shared, medium size |
| L3 () | 1-2 | 10-20 (to L2) | Small, fast |
| L1 (Instruction/Data) | 1-2 | 10-20 (to L2) | Small, fast |

## Pipeline Hazard

Is when Pipelining is not smooth AKA it has a Interuption.

3 Types of Pipeline Hazard

- Structural Hazard $\rightarrow$ They fight for the resource in the memory.
- Data Hazard $\rightarrow$ They want to read data but not available.
or cannot write but the dataa is not available for writing.
- Control Hazard $\rightarrow$ They want to jump to somewhere but
cannot jump directly due to some problems.

### Structural Hazard

- Cause: 2 or more instructions need the same hardware or resource.
- Fix: 
- Preventation:

### Data Hazard

- Cause:
    - One instruction relies on the data produced by another instruction.
    These dependencies often dictate................
        - True Dependency (RAW: Read After Write) $\rightarrow$ 
        An instruction depends on the result of a previous instruction.
            - E.g.
            ```
            ADD r1, r2, r3
            SUB r4, r1, r5
            ```
        - Anti-Dependency (WAR: Write After Read) $\rightarrow$
        An instruction writes to a data location that is read by the
        instruction that precedes it (overwrites before read).
            - E.g.
            ```
            LOAD r0, 0(r2)
            ADD r1, r3, r4
            ```
        - Output Dependency (WAW: Write After Write) $\rightarrow$
        Two instructions write to the same data location.
            - E.g.
            ```
            ADD r1, r2, r3
            MUL r1, r4, r5
            ```

- Fix:
    - Data Forwarding (Data Hazard Forwarding) $\rightarrow$ Forwarding result data to a special
    register
    - Pipeline Stalls (Pipeline Bubbles) $\rightarrow$ Make empty CLK cycle and do nothing (Stall)
    - Out-of-Order Execution $\rightarrow$ Done by Compiler or Assembler: Reorder the instructions
    - Register Renaming $\rightarrow$ Done by Assembler: It ........
- Preventation:

#### Data dependencies

- True Data Dependencies
- Name Dependencies

#### Benefits and drawsback of Data Hazard Management Tecniques

| ... | ... | ... |

### Control Hazard

- Cause: Jumping and caused of wasting CLK cycle(s) because the
CLK cycle(s) being wasted was used in instruction(s) that dropped after fetching the jump
- Fix:

## Pipeline CPI

## Optimal Pipeline Depth

## Typical Pipeline Lengths

## Diversified Pipelines

## Limits of Pipelining

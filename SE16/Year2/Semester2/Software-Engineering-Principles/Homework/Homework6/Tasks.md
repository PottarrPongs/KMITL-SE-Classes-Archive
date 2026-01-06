| No. | Label  | Name                      | Days to complete | Predecessor              |
| :-: | :---:  | :------------------------ | :--------------: | :----------------------: |
| 1   | START  | Start the project (01/01/2026)          | 0  | NULL                     |
| 2   | T1     | Prepare Project Topic                   | 2  | START (1)                |
| 3   | T2     | Define Requirements                     | 4  | START (1)                |
| 4   | T3     | Decide Core Features                    | 3  | START (1)                |
| 5   | T4     | Decide Technology Stack                 | 2  | START (1)                |
| 6   | M1     | Finished Planning Phase                 | 0  | T1, T2, T3, T4 (2;3;4;5) |
| 7   | T5     | Design UI Layout                        | 3  | M1 (6)                   |
| 8   | T6     | Design and Normalize Database           | 4  | M1 (6)                   |
| 9   | T7     | Design API                              | 6  | M1 (6)                   |
| 10  | M2.1   | Finished Designing Phase (Client)       | 0  | T5 (7)                   |
| 11  | M2.2   | Finished Designing Phase (Server)       | 0  | T6, T7 (8;9)             |
| 12  | T8     | Implement Client Side                   | 18 | M2.1 (10)                |
| 13  | T9     | Implement Server Side                   | 22 | M2.2 (11)                |
| 14  | M3.1   | Finished Development Phase (Client)     | 0  | T8 (12)                  |
| 15  | M3.2   | Finished Development Phase (Server)     | 0  | T9 (13)                  |
| 16  | T10    | Unit Test (Client)                      | 2  | M3.1 (14)                |
| 17  | T11    | Unit Test (Server)                      | 2  | M3.2 (15)                |
| 18  | M4     | Finished Testing Phase                  | 0  | T10, T11 (16;17)         |
| 19  | T12    | Deploy Client Side                      | 1  | M4 (18)                  |
| 20  | T13    | Deploy Server Side                      | 1  | M4 (18)                  |
| 21  | FINISH | Finished Project                        | 0  | T12, T13 (19;20)         |

## T9 Sub-Tasks
- Implement all Client Side Page
    - Main Page
    - User Settings Page
    - Task Assignment Page
        - Live Markdown Preview
        - Simple Editor
        - Save File Button
    - Design Page
        - Gantt Chart
        - Class Diagram
        - Interaction Diagram

## T10 Sub-Tasks
- Implement Program API
- Implement Database

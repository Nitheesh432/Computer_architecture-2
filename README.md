# Computer Architecture Assignment — Group 2

**College:** New Horizon College of Engineering  
**Department:** Artificial Intelligence and Machine Learning  
**Course:** Computer Architecture  
**Course code:** 25AIM34  
**Semester / Section:** III E  
**Group:** 2 (USN ending with 1, 6, 8)

## Question 1: Signed Binary Arithmetic
The program performs 8-bit two's complement addition for `25 + (+18)` and `(-25) + (-18)`. It displays operands, binary addition, carry-out, signed decimal result, and signed overflow.

| Expression | Operand 1 | Operand 2 | Result | Decimal | Overflow |
|---|---|---|---|---:|---|
| 25 + (+18) | `00011001` | `00010010` | `00101011` | 43 | No |
| (-25) + (-18) | `11100111` | `11101110` | `11010101` | -43 | No |

## Question 2: Logical Shift Operations
The program displays each step of these 8-bit shifts.

| Operation | Step 1 | Final result |
|---|---|---|
| Left shift `10110110` by 2 | `01101100` | `11011000` |
| Right shift `11010100` by 2 | `01101010` | `00110101` |

## Files
- `question1.py` — Signed binary arithmetic
- `question2.py` — Logical shift operations
- `README.md` — Assignment details and expected results

## How to run
Run these commands from a terminal in this folder:

```bash
python question1.py
python question2.py
```

After running each program on your computer, capture genuine terminal screenshots and upload them as `question1_output.png` and `question2_output.png`.

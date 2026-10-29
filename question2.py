# Question 2: Logical Shift Operations on 8-bit Binary Numbers

def logical_left_shift(binary, positions):
    print("\n(a) Logical left shift of 10110110 by 2 positions")
    print("Original 8-bit number:", binary)
    for step in range(1, positions + 1):
        binary = binary[1:] + "0"
        print(f"After shift {step}: {binary}")
    print("Final 8-bit result:", binary)

def logical_right_shift(binary, positions):
    print("\n(b) Logical right shift of 11010100 by 2 positions")
    print("Original 8-bit number:", binary)
    for step in range(1, positions + 1):
        binary = "0" + binary[:-1]
        print(f"After shift {step}: {binary}")
    print("Final 8-bit result:", binary)

if __name__ == "__main__":
    print("LOGICAL SHIFT OPERATIONS ON 8-BIT BINARY NUMBERS")
    logical_left_shift("10110110", 2)
    logical_right_shift("11010100", 2)

# Question 1: Signed Binary Arithmetic using 8-bit 2's Complement

def to_8bit_binary(number):
    if not -128 <= number <= 127:
        raise ValueError("Number must be between -128 and 127.")
    return format(number & 0xFF, "08b")

def add_8bit_binary(first, second):
    carry = 0
    result = ""
    for i in range(7, -1, -1):
        total = int(first[i]) + int(second[i]) + carry
        result = str(total % 2) + result
        carry = total // 2
    return result, carry

def binary_to_signed_decimal(binary):
    value = int(binary, 2)
    return value - 256 if binary[0] == "1" else value

def perform_addition(number1, number2):
    binary1 = to_8bit_binary(number1)
    binary2 = to_8bit_binary(number2)
    result, carry_out = add_8bit_binary(binary1, binary2)
    decimal_result = binary_to_signed_decimal(result)
    overflow = ((number1 >= 0) == (number2 >= 0) and
                ((decimal_result >= 0) != (number1 >= 0)))
    print(f"Operand 1: {number1} = {binary1}")
    print(f"Operand 2: {number2} = {binary2}")
    print("\nBinary addition:")
    print(f"  {binary1}")
    print(f"+ {binary2}")
    print("  --------")
    print(f"  {result}")
    print(f"Carry out: {carry_out}")
    print(f"Final result (binary): {result}")
    print(f"Final result (decimal): {decimal_result}")
    print(f"Arithmetic overflow: {'Yes' if overflow else 'No'}")

if __name__ == "__main__":
    print("SIGNED BINARY ARITHMETIC USING 8-BIT 2'S COMPLEMENT")
    print("\n(a) 25 + (+18)")
    perform_addition(25, 18)
    print("\n(b) (-25) + (-18)")
    perform_addition(-25, -18)

import math

def calculate_math_operations(num):
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sine_result = math.sin(num)

    print("results:")
    print(f"square root of {num} = {sqrt_result}")
    print(f"natural logrithm (log base e) of {num} = {log_result}")
    print(f"sine of {num} (in radian) = {sine_result}")

calculate_math_operations(5)
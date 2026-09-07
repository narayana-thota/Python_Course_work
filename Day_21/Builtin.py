import math
import platform
import random
import sys
from collections import Counter, defaultdict, deque

# ==========================================
# 1. SYSTEM & PLATFORM INFORMATION
# ==========================================
print("--- System & Platform Information ---")
print("Command Line Args:", sys.argv)  # List of command-line arguments
print("Python Version:", sys.version)  # Details about Python version
print("Module Search Path:", sys.path)  # Directories Python searches for modules

print("OS System:", platform.system())  # e.g., 'Windows', 'Linux', 'Darwin'
print("OS Release:", platform.release())  # e.g., '10', '20.6.0'
print("Platform Info:", platform.platform())  # Complete platform string


# ==========================================
# 2. MATHEMATICAL OPERATIONS & TRIGONOMETRY
# ==========================================
print("\n--- Math Operations ---")
print("Pi:", math.pi)  # 3.141592653589793
print("Euler's Number (e):", math.e)  # 2.718281828459045
print("Logarithm (base 2 of 2):", math.log(2, 2))  # 1.0

# Note: Trigonometric functions in math expect values in radians (not degrees)
print("Sin(30 rad):", math.sin(30))
print("Cos(30 rad):", math.cos(30))
print("Tan(30 rad):", math.tan(30))

print("Convert 30 rad to degrees:", math.degrees(30))
print("Convert 30 deg to radians:", math.radians(30))

print("Factorial of 5:", math.factorial(5))  # 120
print("GCD of 2 and 6:", math.gcd(2, 6))  # 2
print("Square root of 36:", math.sqrt(36))  # 6.0
print("4 raised to power 6:", math.pow(4, 6))  # 4096.0


# ==========================================
# 3. ROUNDING METHODS
# ==========================================
print("\n--- Rounding Operations ---")
# math.ceil() rounds UP to the nearest integer
print("Ceil(5.1):", math.ceil(5.1))  # 6
print("Ceil(5.9):", math.ceil(5.9))  # 6
print("Ceil(5.0):", math.ceil(5.0))  # 5

# math.floor() rounds DOWN to the nearest integer
print("Floor(5.9):", math.floor(5.9))  # 5
print("Floor(5.1):", math.floor(5.1))  # 5
print("Floor(5.0):", math.floor(5.0))  # 5

# round() rounds to the nearest even number on halves (Banker's rounding)
print("Round(5.7):", round(5.7))  # 6
print("Round(5.4):", round(5.4))  # 5
print("Round(5.5):", round(5.5))  # 6


# ==========================================
# 4. RANDOMIZATION
# ==========================================
print("\n--- Randomization ---")
# Seed guarantees the same random sequence across executions
random.seed(9)

print("Random Float (0.0 to 1.0):", random.random())
print("Random Integer (1 to 6):", random.randint(1, 6))
print("Random Uniform Float (1 to 6):", random.uniform(1, 6))

coins = ["heads", "tails"]
print("Random Choice from list:", random.choice(coins))

lang = ["python", "java", "c++", "c#"]
random.shuffle(lang)  # Modifies the list in-place
print("Shuffled List:", lang)


# ==========================================
# 5. ADVANCED COLLECTIONS & COUNTERS
# ==========================================
print("\n--- Collections & Dictionaries ---")
s = "python programing"

# Using Counter to get frequencies automatically
res_counter = Counter(s)
print("Counter result:", res_counter)

# Doing the same frequency count manually using a standard dict
manual_dict = {}
for char in s:
    if char in manual_dict:
        manual_dict[char] += 1
    else:
        manual_dict[char] = 1
print("Manual dict result:", manual_dict)

# Using defaultdict to safely append lists without checking key existence
res_defaultdict = defaultdict(list)
prod = ["suger", "salt", "milk"]
for item in prod:
    res_defaultdict[item].append(["des", "rev", "com"])
print("Defaultdict result:", dict(res_defaultdict))

# Working with a Deque (Double-ended Queue)
l_deque = deque([])
l_deque.appendleft(10)  # [10]
l_deque.appendleft(20)  # [20, 10]
l_deque.appendleft(30)  # [30, 20, 10]
l_deque.appendleft(40)  # [40, 30, 20, 10]
l_deque.pop()  # Removes 10 -> [40, 30, 20]
l_deque.pop()  # Removes 20 -> [40, 30]
l_deque.appendleft(50)  # [50, 40, 30]
l_deque.appendleft(60)  # [60, 50, 40, 30]
print("Deque final state:", l_deque)


# ==========================================
# 6. PROGRAM EXIT
# ==========================================
print("\nProgram finished successfully. Exiting now...")
sys.exit()  # Cleanly exits the Python runtime environment

"""
Exercise 5: Remove items from the set at once
Write a Python program to remove items 10, 20, 30 from the following set at once.

Given:

set1 = {10, 20, 30, 40, 50}
Expected output:

{40, 50}
"""

set1 = {10, 20, 30, 40, 50}

rem = {10, 20, 30}

s3 = set1-rem

print(s3)
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:13:18 2023

@author: kurs
"""
# Ausgabe ob kleiner, größer oder gleich
a = 7
b = 7

if a < b:
    print("a ist kleiner als b")
elif a > b:
    print("a ist größer als b")
else:
    print("a ist gleich b")
print("\n-------------------------------------\n")

# Schlechte Lösung eines Programmierstils
if a < b:
    print("a ist kleiner als b")
if a > b:
    print("a ist größer als b")
if a == b:
    print("a ist gleich b")
#!/data/data/com.termux/files/usr/bin/env python3.6

#imports
import chalk    #for colored output
from sys import exit #for exit()
from time import sleep#for sleep()

while True:
        chalk.green("Options:")
        chalk.green("Enter 'add' to add two numbers")
        chalk.green("Enter 'sub' to subtract two numbers")
        chalk.green("Enter 'mul' to multiply two numbers")
        chalk.green("Enter 'div' to divide two numbers")
        chalk.green("Enter 'exit' to quit")
        user_input = input("#> ")

        if user_input == "exit":    #exit app..
        	#break
                chalk.blue('Now Exiting...')
                sleep(5)  #pulse 5s
                exit()  #exit 0
        elif user_input == "add":   # add two numbers
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 + num2)
            chalk.blue("[#] " + result) #show results
            sleep(3)   #pulse 3s
        elif user_input == "sub":   #sub two numbers
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 - num2)
            chalk.blue("[#] " + result) #show results
            sleep(3)   #pulse 3s
        elif user_input == "mul":   #mult two numbers
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 * num2)
            chalk.blue("[#] " + result) #show results
            sleep(3)   #pulse 3s
        elif user_input == "div":   #divide two numbers
            num1 = float(input("Enter a large number: "))
            num2 = float(input("Enter a small number: "))
            if num2 == 0:   #test to see if num2 is Divisionbyzero error
                chalk.yellow("[!] " "Can't divide by zero.")    #warn if num2 is 0
                sleep(5)  #pulse 5s
                continue
            result = str(num1 / num2)
            chalk.blue("[#] " + result) #show results
            sleep(3)   #pulse 3s
        else:
            chalk.red("Unknown input")  #give error mess
            sleep(5)  #pulse 5s

"""
#   A simple calculater.
#   written by, S. Gibson.
#   written on, Dec 20, 2016.
#
#   Feel free to change.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:26:25 2021

@author: hp
"""

def main():
    print('This will calculate shipping, handling and taxes on your purchase')
    calc_subtotal()   

def calc_subtotal():
    while True:
        subtotal = float(input('Enter your subtotal please: '))
        if subtotal >= 1 and subtotal <= 9999:
            print('This is a valid amount')
            break
        else:
            print('Invalid amount')
            continue
    calc_shipping(subtotal)

def calc_shipping(subtotal):
    shipping_cost = subtotal * .10
    calc_handling(subtotal, shipping_cost)

def calc_handling(subtotal, shipping_cost):
    handling_fee = 0
    if subtotal < 100:
        print('There is a 2 dollar handling fee')
        handling_fee += 2
    else:
        print('There is no handling fee')
    calc_tax(subtotal, shipping_cost, handling_fee)

def calc_tax(subtotal, shipping_cost, handling_fee):
    tax = subtotal * .06
    calc_total(subtotal, shipping_cost, handling_fee, tax)

def calc_total(subtotal, shipping_cost, handling_fee, tax):
    print('\nProduct Total Information')
    print('\tSubtotal: ${}'.format(subtotal))
    print('\tShipping: ${}'.format(shipping_cost))
    print('\tHandling: ${}'.format(handling_fee))
    print('\tSales tax: ${}'.format(tax))
    total = subtotal + shipping_cost + handling_fee + tax
    print('\tGrand total: ${}'.format(total))

main()
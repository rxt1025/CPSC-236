#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def sales_tax(total):
    
    sales_tax= total*0.06
    return round(sales_tax, 2)

def total_after_tax(total, sales_tax):
    
    total_after_tax = total+sales_tax
    return round(total_after_tax, 2)
    
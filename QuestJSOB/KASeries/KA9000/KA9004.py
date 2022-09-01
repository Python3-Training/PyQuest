#!/usr/bin/env python3
# Mission: Provide additonal *args & **kwargs examples.
# File: KA9004.py

### Problem:
##
##def fun1(one, *args, **kwargs):
##    print(one, *args, f'{**kwargs}')
##
##fun1('zParam', 'a','b', a='3', b='4')

def fun2(two, *args, **kwargs):
    print(two, *args, **kwargs)

fun2('Two')

fun2('Two', 'hi', 'we', 'got ...')

fun2('Two', 'hi', 'we', 'got ...', sep='|', end='$')

fun2('Two', 'hi', 'we', 'got ...', a='|', b='$')

#!/usr/bin/env python3
# Mission: Demonstrate exec() using global parameters.
# File: KA9003.py

my_global = 123

exec("print(my_global)")
exec("print(my_global)", {'my_global':42})




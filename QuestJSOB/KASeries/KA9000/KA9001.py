#!/usr/bin/env python3
# Mission: Report default class members.
# File: KA9001.py

for ss, member in enumerate(sorted(dir(object())),1):
	print(ss, member)


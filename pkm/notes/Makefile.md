---
title:  Makefile
created: Sunday 23rd April 2023 16:54
aliases: 
tags: lenguages
---
## Colors

- [Color Coding Makefile Output](http://jamesdolan.blogspot.com/2009/10/color-coding-makefile-output.html)
- [Bash Colors](https://www.shellhacks.com/bash-colors/)
- [A Makefile for managing an OpenSSL CA](https://gist.github.com/ab/4570034)
- [Makefile tutorial](https://makefiletutorial.com/#top)
- [What is the difference between the GNU Makefile variable assignments =, ?=, := and +=?](https://stackoverflow.com/questions/448910/what-is-the-difference-between-the-gnu-makefile-variable-assignments-a)

```makefile
NO_COLOR=\e[0m
OK_COLOR=\e[32m
ERROR_COLOR=\e[31m
WARN_COLOR=\e[33m

OK_STRING=$(OK_COLOR)[OK]$(NO_COLOR)
ERROR_STRING=$(ERROR_COLOR)[ERRORS]$(NO_COLOR)
WARN_STRING=$(WARN_COLOR)[WARNINGS]$(NO_COLOR)

ac:
	@echo -e "$(OK_STRING)"
```
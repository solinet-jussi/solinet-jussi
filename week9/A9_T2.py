########################################################
# Task A9_T2
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import sys

print("Program starting.")
exit_code = int(input("Insert exit code(0-255): "))

if exit_code == 0:
	print("Clean exit")
else:
	print("Error code")

sys.exit(exit_code)

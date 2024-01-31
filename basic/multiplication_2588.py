import sys
input = sys.stdin.readline

operand_1 = int(input().strip())
operand_2 = int(input().strip())

operand_2_100 = operand_2 // 100
operand_2_10 = operand_2 // 10 % 10
operand_2_1 = operand_2 % 10

print(operand_1 * operand_2_1)
print(operand_1 * operand_2_10)
print(operand_1 * operand_2_100)
print(operand_1 * operand_2)

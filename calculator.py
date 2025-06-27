class Calculator:
    def add(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        if b == 0:
            return ("Zero division Error: zero is not divisible!")
        return a / b
def main():
    calc =Calculator()

print("Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.Division")
print("5.Exit!")

while True:
    choice = input("Enter Your choice(1-5):")
    if choice == "5":
        print("Existing the calculator Good bye!")
        break
    if choice in ["1","2","3","4"]:
        try:
            num1 = float(input("Enter a First number:"))
            num2 = float(input("Enter Second number:"))
        except ValueError:
            print("Invalid input!.Enter valid numbers")
        continue

        if choice == "1":
            print("Result:",calc.add(num1,num2))
        elif choice == "2":
            print("Result",calc.sub(num1,num2))
        elif choice == "3":
            print("Result",calc.mul(num1,num2))
        elif choice == "4":
            print("Result",calc.div(num1,num2))
    else:
        print("Invalid choice! choose valid choice")
        if __name__ == "__main__":
            main()
        

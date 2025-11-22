class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        #self.expenses = []
        #self.categories = []  # ✅ spelled correctly
        self.expenses_dict = {}

    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"Enter number of {self.expense_type} expenses you want to add (integers only): "))
                break
            except:
                print()
                print("** ERROR **")
                print("Wrong input. Enter INTEGERS only!\n")

        print()
        print(f'Enter expenses in \"Type Cost\" format. For example: Milk 10')
        for i in range(num_expenses):
            while True:
                try:
                    type, exp = input(f"Enter expense #{i+1}: ").split()
                    self.expenses_dict[type] = float(exp)
                   # self.expenses.append(float(exp))
                   # self.categories.append(type)  # ✅ add this line
                    break
                except:
                    print()
                    print("** ERROR **")
                    print("Please follow the format correctly (e.g., Milk 10)")
                    continue
        self.write_to_file()
        
    def get_expenses(self):
        print()
        print(f"Total money you spent on {self.expense_type} is ${sum(self.expenses_dict.values())}")
        return sum(self.expenses_dict.values())

    def get_expenses_list(self):
        print()
        print(f"List of {self.expense_type} expenses are:") 

        for type, exp in self.expenses_dict.items():
                print(f"{type} : ${str(exp)}")

    def write_to_file(self):
        with open("data.txt", "a") as data:
            data.write(self.expense_type)
            data.write("\n")

            for type, exp in self.expenses_dict.items():
                data.write(f"{type} : ${str(exp)}")
                data.write("\n")
            data.write("\n")

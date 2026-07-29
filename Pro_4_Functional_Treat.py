print("Welcome to the Data Analyzer and Transformer Program")
Arrays=[]

def add_data():
    global Arrays
    
    print("1.1D array")
    print("2.2D array")

    option = int(input("Enter a number for array:"))

    if option == 1:

        num =list(map(int , input("Enter data for a 1D array(seprated by space):").split()))

        Arrays.append(num)
        print("Data has been stored successfully!")

    elif option == 2:

        num = []

        for i in range(3):
            row = list(map(int , input(f"Enter Row {i + 1} : ").split()))

            num.append(row)

            
        Arrays.append(num)
        print("Data has been stored successfully!")
 
    else:
        print("Invalid choice")


def Display_data():
  
    print("\nData Summary:")
    print("- Total elements:",len(Arrays[0]))
    print("- Minimum Value:",min(Arrays[0]))
    print("- Maximum Value:",max(Arrays[0]))
    print("- Sum of all Values:",sum(Arrays[0]))
    print("- avarage value:",sum(Arrays[0])/len(Arrays[0]))
    
def calculate_factorial():
    
    n = int(input("Enter a number to calulate its factorial: "))
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n*factorial(n-1)
    print("Factorial is : ", factorial(n))

def filter_data():

    value=int(input("Enter a threshold value to filter out data above this value:"))

    numbers=list(filter(lambda x:x >= value,Arrays[0]))
   
    print(filter_data.__doc__)
    print(numbers)
    return numbers

def sort_data():
    if len(Arrays) == 0:
        print("\n No Data Found!")
        return

    print("\n sorting options :")
    print("1. Ascending Order")
    print("2. Descending Order")

    choice = input("Enter your choice :")

    if choice == "1":
        print("Sorted Data in Ascending order :", sorted(Arrays))
    else:
        print("Sorted Data in Descending order :", sorted(Arrays , reverse=True))
    
def display_dataset(*args,**kwargs):

    Minimum=min(args)
    Maximum=max(args)
    Total=sum(args)
    Average=sum(args)/len(args)
    
    if kwargs.get("show",True):

        print("- Data Statistics:") 
        print("- Minimum value:",Minimum)
        print("- Maximum value:",Maximum)
        print("- Sum of all values:",Total)
        print("- Average value:",Average)

    return Minimum,Maximum,Total,Average
    
def exit():
    print("Thank you for using the data Analyzer and Transformer")
    print("Program. Goodbye!")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summery(Built-in Functions)")
    print("3. Calculate Factorial(Recurtion)")
    print("4. Filter Data by Threshld(Lamda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics(Return Multiple Values)")
    print("7.Exit Program")

    choice = int(input("Please enter your choice:"))

    if choice==1:
        add_data()
    elif choice==2:
        Display_data()
    elif choice==3:
        calculate_factorial()
    elif choice==4:
        filter_data()
    elif choice==5:
        sort_data()
    elif choice==6:
        Minimum,Maximum,Sum,Avarage=display_dataset(*Arrays[0],show=True)
    elif choice==7:
        exit()
        break
    else:
        print("\n Invalid data")

    

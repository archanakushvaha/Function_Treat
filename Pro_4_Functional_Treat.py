data = []

def add_data():

    global data

    data = list(map(int ,input("Enter data for a 1D array(separated by spaces): ").split()))

    print("Data has been stored successfully!")

def data_summary():
    if len(data) == 0:
        print("\n No Data Found!!! ")
        return

    print("\n Data Summary:")
    print("Total elements: " ,len(data) )
    print("Minimum value: ",min(data))
    print("Maximum value: ",max(data))
    print("Sum of all value: ",sum(data))

    average = sum(data)/len(data)
    print("Average value :" , average)
    
def calculate_factorial():
    n = int(input("Enter a number to calulate its factorial: "))
    def factorial(n):
        if n == 1:
            return 1
        return n*factorial(n-1)
    print(factorial(n))
    
       
def filter_data():

    if len(data) == 0:
        print("\n No Data Found!!! ")
        return
    threshold = int(input("Enter a threshold value to filter out data above this value: "))

    my_filter = lambda x: x >= threshold
    result = list(filter(my_filter , data))

    print(f"Filtered Data (value >= {threshold}):  {result}")

def sort_data():
    if len(data) == 0:
        print("\n No Data Found!")
        return

    print("\n sorting options :")
    print("1. Ascending Order")
    print("2. Descending Order")

    choice = input("Enter your choice :")

    if choice == "1":
        print("Sorted Data in Ascending order :", sorted(data))
    else:
        print("Sorted Data in Descending order :", sorted(data , reverse=True))
    
def display_statistics():

    if len(data) == 0:
        print("\n No data found!!!")
        return
    
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / count
    
    print("Dataset Statistics:")
    print(f"-Minimum value : ",minimum)
    print(f"-Maximum value : ",maximum)
    print(f"-Sum of Element : ",total)
    print(f"-Average value : ",average)
    
    
# Main Menu

while True:
    print("\n Welcome to Data Analyzer and Transformer Program")
    print("Main Menu: ")
    print("1. Input Data")
    print("2. Display Data Summary(Built-in Functions)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Fliter Data by Threshold(Lambda function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics(Return Multiple values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        add_data()
    elif choice == "2":
        data_summary()
    elif choice == "3":
        calculate_factorial()
    elif choice == "4":
        filter_data()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        display_statistics()
    elif choice == "7":
        print("\n Thank you for using the Data Analyzerand Transformer program. Goodbye!")
        break
    else:
        print("\n Invalid choice! Please try again.")        

        

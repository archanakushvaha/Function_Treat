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
    
def factorial():
    num = input("Enter a number to calulate its factorial: ")
    def factorial(num):
        if n == 1:
            return 1
        return n*factorial(n-1)
    print(factorial(5))
    
       
def filter_data():

    if len(data)==0:
        print("\n No Data Found!!! ")
        return
    data =int(input("Enter a threshold value to filter out data above this value: "))

    my_filter = lambda x : x >= data
    result = list(filter(my_filter,data))

    print("Filtered Data (value >= {data}): ")

def sort_data():
    
    

def display_statistics():


    

# Main Menu

while True:
    print("\n=====Welcome to Data Analyzer Program=====")
    print("1. Input Data")
    print("2. Display Data Summary(Built-in Functions)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Fliter Data by Threshold(Lambda function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics(Return Multiple values)")
    print("7. Exit Program")

    choice = input("Please enter your choice (1-7): ")

    if choice == "1":
        add_data()
    elif choice == "2":
        data_summary()
    elif choice == "3":
        run_factorial()
    elif choice == "4":
        filter_data()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        display_ststistics()
    elif choice == "7":
        print("\n Thank you for usingthe program. Goodbye!")
        break
    else:
        print("\n Invalid choice! Please try again.")        

        

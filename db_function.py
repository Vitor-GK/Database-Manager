import mysql.connector
import time
import datetime
from decimal import Decimal
import sys

invalid_digits = " @#$%&*"

def Time():
    time.sleep(3)
    print("\nReturning to the main menu.")
    time.sleep(2)

def Separation():
    print("/"*40)
    print("\n")

def ReturnOrNot(function):
    while True:
        try:
            result = int(input(f"Enter \"0\" to return or \"1\" to {function}: "))
            if result == 0:
                print("Returning to the main menu!")
                return 0
            elif result == 1:
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Invalid option. Please enter a number.")

def ColumnsName(cursor):
    cursor.execute("SELECT * FROM Employees LIMIT 0;")
    discarded = cursor.fetchall()
    name_of_columns = [desc[0] for desc in cursor.description]
    return name_of_columns

def ShowTable(cursor):
    
    columns_name = ColumnsName(cursor)
    cursor.execute("SELECT * FROM Employees;")
    result = cursor.fetchall()
    print(columns_name)

    for record in result:
        formatted = []
        for value in record:
            if isinstance(value, datetime.date):
                formatted.append(value.strftime("%Y-%m-%d"))
            elif isinstance(value, Decimal):
                formatted.append(f"{value:.2f}")
            else:
                formatted.append(str(value))
        print(formatted)

    print("\n")
    Time()

def ShowRecord(cursor):

    if ReturnOrNot("show a record") == 0:
        return
    
    while True:
        try:
            cursor.execute("SELECT employee_id FROM Employees")
            id_list = [row[0] for row in cursor.fetchall()]
            print(f"ID list: {id_list}\n")

            result = int(input("Insert the ID from the record that you want to see: "))

            if result in id_list:
                break
            elif result == 0:
                print("Returning!\n")
                return
            else:
                print("Invalid ID!")
        except ValueError:
            print("Invalid ID!")
    
    cursor.execute("SELECT * FROM Employees WHERE employee_id = %s", (result,))
    print(cursor.fetchall())
    Time()
   
def ShowColumn(cursor):

    name_of_columns = ColumnsName(cursor)

    if ReturnOrNot("show a column") == 0:
        return

    while True:
        
        print(name_of_columns)
        result = input("\nEnter the name of the column that you want to see: ")
        
        if result.strip() != "" and result in name_of_columns:
            break
        else:
            print("Invalid option, try again!")
    
    cursor.execute(f"SELECT {result} FROM Employees;")
    column = cursor.fetchall()
    print(f"{result}\n")
    for value in column:
        print(value)
    Time()

def InsertRecord(cursor, conn):
    
    name_of_columns = [column for column in ColumnsName(cursor) if column != "employee_id"]

    if ReturnOrNot("insert a record") == 0:
        return

    values = []
    for column in name_of_columns:
        value = input(f"{column}: ").strip()
        values.append(value)

    ph = ", ".join(["%s"] * len(name_of_columns))
    columns = ", ".join(name_of_columns)
    sql_command = f"INSERT INTO Employees ({columns}) VALUES ({ph})"

    cursor.execute(sql_command, values)

    conn.commit()
    print("The record was successfully inserted!")
    Time()

def UpdateRecord(cursor, conn):
    name_of_columns = ColumnsName(cursor)

    cursor.execute("SELECT employee_id FROM Employees")
    id_list = [id[0] for id in cursor.fetchall()]

    if ReturnOrNot("update a record") == 0:
        return

    print("Which record do you want to update? (insert one of the IDs below):")
    print(id_list)

    while True:
        try:    
            selected_id = int(input("id: "))
            if selected_id in id_list:
                break
            else:
                print("Invalid ID. Try Again!")
        except ValueError:
            print("Enter a valid integer")
    values = []
    update_columns = [column for column in name_of_columns if column != "employee_id"  ]
    
    print(f"Now insert the new values for each of the following columns from the ID: {selected_id}")
    for column in update_columns:
        value = input(f"{column}: ").strip()
        values.append(value)

    update = ", ".join([f"{column} = %s" for column in update_columns])
    sql_command = f"UPDATE Employees SET {update} WHERE employee_id = %s"
    cursor.execute(sql_command, values + [selected_id])
    
    conn.commit()
    print("The row was successfully updated")
    Time()

    

def DeleteRecord(cursor, conn):
    
    if ReturnOrNot("delete a record") == 0:
        return
    
    while True:

        try:
            deleted_id = int(input("Enter the ID from the row that will be delete: " ))
            cursor.execute("SELECT employee_id FROM Employees;")
            id_list = [row[0] for row in cursor.fetchall()]
            if deleted_id in id_list:
                break
            else:
                print("This ID is not in the table!")
        except ValueError:
            print("Invalid ID. Try again.")

    cursor.execute("DELETE FROM Employees WHERE employee_id = %s",(deleted_id,))
    print(f"The row with the ID {deleted_id} was deleted")

    conn.commit()
    print("The row was successfully deleted")
    Time()


def CreateColumn(cursor, conn):

    name_of_columns = ColumnsName(cursor)
    if ReturnOrNot("create a column") == 0:
        return

    print("Choose the type of column to create:\n")
    print("1. Column for integers;\n2. Column for date(YYYY/MM/DD);\n3. Column for money;\n4. Column for text;\n")
    options = [1, 2, 3, 4]
    while True:
        column_type = int(input("Answer: "))
        if column_type in options:
            print(f"option {column_type} chosen.\n")
            break
        else:
            print("Invalid option. Try again!\n")
    
    while True:
        new_column_name = input("Enter a name for the column(use \"_\" instead of space, do not use uppercase or special characters): ")
        if any(char in invalid_digits for char in new_column_name):
            print("Invalid name: do not use special characters.\n")
        elif  not new_column_name.islower():
            print("Invalid name: the name must be lowercase.\n")
        elif new_column_name.isdigit():
            print("Invalid name: cannot start with a number.\n")
        elif new_column_name[0].isdigit():
            print("Invalid name: cannot start with a number.\n")
        elif new_column_name in name_of_columns:
            print("Invalid name: cannot have columns with the same name.\n")
        else :
            print(f"The column {new_column_name} is created!\n")
            break
    
    
    if column_type == 1:
        cursor.execute(f"ALTER TABLE Employees ADD {new_column_name} INT;")
        
    elif column_type == 2:
        cursor.execute(f"ALTER TABLE Employees ADD {new_column_name} DATE;")
            
    elif column_type == 3:
        cursor.execute(f"ALTER TABLE Employees ADD {new_column_name} DECIMAL(10, 2);")
        
    else:
        cursor.execute(f"ALTER TABLE Employees ADD {new_column_name} VARCHAR(50)")

    conn.commit()
    print("The column was successfully created")

    Time()
    

def DeleteColumn(cursor, conn):

    if ReturnOrNot("delete a column") == 0:
        return

    name_of_columns = ColumnsName(cursor)
    
    while True:    
        print("Enter the name of the column that you want to remove:")
        print(name_of_columns)
        removed_column = input()
        if removed_column in name_of_columns:
            break
        else:
            print("This column is not in the table")
    cursor.execute(f"ALTER TABLE Employees DROP COLUMN {removed_column};")
    print(f"The column {removed_column} was removed")

    conn.commit()

    Time()

def Menu(cursor, conn):
    
    Separation()
    print("Main Menu:\n\n1. Show table/records/columns;\n2. Enter/update/delete data;\n3. Create/delete columns;\n4. Exit program;\n")

    while True: 
        try:
            choice = int(input("Choose the number of desired option: "))
            if choice in (1, 2, 3,):
                print(f"////////////////////////////////////////\nOption {choice} was selected. choose one of the items below:\n")
                break
            elif choice is 4:
                print(f"////////////////////////////////////////\nOption {choice} was selected.\n")
                break

        except ValueError:
            print("Error: input must be a valid number.\n////////////////////////////////////////\n")
    
    if choice == 1:
        print("1. Show entire table;\n2. Show a specific record;\n3. Show a column;\n4. Return;\n")
        while True:
            try:    
                sub_choice = int(input("Choose the number of desired option: "))
                if sub_choice in (1, 2, 3, 4):
                    break
            except ValueError:
                print("Error: input must be a valid number.\n////////////////////////////////////////\n")

        if sub_choice == 1:
            ShowTable(cursor)

        elif sub_choice == 2:
            ShowRecord(cursor)

        elif sub_choice == 3:
            ShowColumn(cursor)
        
        else:
            return

    elif choice == 2:
        print("1. Insert a record;\n2. update a record;\n3. Delete a record;\n4. Return;\n")
        while True:    
            try:
                sub_choice = int(input("Choose the number of desired option: "))
                if sub_choice in (1, 2, 3, 4):
                    break
            except ValueError:
                print("Error: input must be a valid number.\n////////////////////////////////////////\n")
        
        if sub_choice == 1:
            InsertRecord(cursor, conn)

        elif sub_choice == 2:
            UpdateRecord(cursor, conn)

        elif sub_choice == 3:
            DeleteRecord(cursor, conn)

        else:
            return

    elif choice == 3:
        print("1. Create a column;\n2. Delete a column;\n3. Return\n")
        while True:
            try:
                sub_choice = int(input("Choose the number of desired option: "))
                if sub_choice in (1, 2, 3):
                    break
            except ValueError:
                print("Error: input must be a valid number.\n////////////////////////////////////////\n")
        
        if sub_choice == 1:
            CreateColumn(cursor, conn)

        elif sub_choice == 2:
            DeleteColumn(cursor, conn)

        else:
            return
    
    else:
        print("Program terminated.")
        sys.exit(0)
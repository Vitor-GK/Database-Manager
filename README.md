#Database-Manager
Description: A simple Python program that allows a user to interact with a pre-existing database and table for managing employee registrations in a business context. The manager can query the entire table, specific records, or individual columns, as 
well as add or delete records and columns. The program uses MySQL cursors for database interaction.


Functionalities:

  - Show the entire table;
  - Show a specific record;
  - Show a column;
  - Insert a new record;
  - Update a record;
  - Delete a record;
  - Create a new column;
  - Delete a column;

Technologies:

  - Python
  - MySQL
  - mysql-connector-python

Requirements:

  - Python >= 3.6
  - MySQL Server
  - mysql-connector-python

Installation:

  **mysql-connector-python**: 
  Install this library using the command `pip install mysql-connector-python` in a terminal.

  **MySQL Server**: 
  MySQL Server is necessary to create the database on your machine, which is essential for
  the program to work. Download it from the the official MySQL website:           
  `https://dev.mysql.com/downloads/mysql/`. Select Version and Operating System that match your system.
  Then, follow the steps provided by the installer.

  **Python**: 
  Ensure Python (version 3.6 or higher) is installed on your machine. Download it from the official website: 
  https://www.python.org/downloads/ and follow the installation instructions for your operating system.


Explanations:

  **Creation of Database on Mysql Workbech**: 
  After the installation of MySQL and selecting an user, open your code editor and enter the                                                 following code:
  
  ```sql
  CREATE DATABASE Business;
 
  CREATE TABLE Employees(
  employee_id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(50),
  birth_date DATE,
  salary DECIMAL(10,2)
  );
  ``` 
  Then save and execute the code in MySQL Workbench.

  
  **Connecting to the Database**:
  As indicated in the messages printed on screen, at the beginning of the program, the code already has default configurations, so 
  you only need to press "Enter" to accept the defaults. Except for the cases if you have created a 
  password (you will need to enter it correctly) and if you have created a user(if you do not, use root).


  **How to Run**:
  Open your operating system's terminal or your code editor's terminal and run the command `python database_manager.py`. If your machine
  has more than one Python version installed, use `python3 database_manager.py`. After running the program, follow the on-screen 
  instructions to connect to the database.


  Tips/Notes:

   - Be attentive to your Python version;
   - If you have created passwords or users for MySQL, enter them correctly;
   - The program uses port 3306 to connect to MySQL database. If your MySQL Server is using a different port, please change
     it to 3306;
   - Make sure to run the program from the folder where the project files (database_manager.py and db_function.py) are located. Running 
     it from a different directory may cause errors.


Personal Objectives with the Program:
    
  One of the main objectives of making this program is to practice and consolidate the knowledge I have recently acquired in Python and 
  SQL. This program is and will continue to be important for reinforcing and improving everything I have learned so far, such as 
  programming logic, Python, SQL, databases, cursors, good coding practices, libraries, data manipulation, error handling, user input 
  validation, etc.
  In addition, another purpose of this program is to improve my portfolio, demonstrating my practical skills and knowledge of the 
  topics necessary to develop this code. For the first version, I am satisfied with the results.


Future Improvements and Current Issues:

  **Future Improvements**:
    - Add support for multiple tables;
    - Implement advanced queries (filters, sorting);
    - Add a Graphical User Interface(GUI);
    - Improve and standardize the input validation and formatting;
    - Add visual graphics and reports;
    
  **Current Issues**:
    - Inconsistent output formatting;
    - Limited functionality;
    - Potential SQL Injection vulnerabilities;

I plan to release new versions as I learn more. In "Future Improvements" I already show some of my ideas that I think will make the code 
better and allow me to practice new knowledge. I am interested in learning some new libraries that could help me with the "Future 
Improvements" and in other projects, like: SQLAlchemy, pandas, Tkinter, PyQt, matplotlib, Pydantic and many others.

Study Sources:

The main source for the knowledge necessary to do this program was the following project/course:

  -Leveling Phase Project Course (Certificate on LinkedIn)

It provided an introduction to key skills such as Python and SQL, and served as the main reason for creating this project is to put these 
skills into practice.
I also consulted additional videos and other materials beyond the course, which were very helpful, but there are too many to list each 
one here.

Acknowledgements:
  Thanks for checking out this project!
  I am open to any constructive feedback and suggestions. You can reach me through the contacts below:

  **Email**: vitorgkockhann@gmail.com
  **LinkedIn**: https://www.linkedin.com/in/vitor-glier-kockhann-956a9b353/ 
  
  
  
                                               
                                                  

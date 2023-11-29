CRUD Operations using Python and CLI

Overview
This repository is designed to facilitate CRUD (Create-Read-Update-Delete) operations using Python and a Command Line Interface (CLI). 

<img width="748" alt="Screenshot 2023-11-28 at 11 57 09 PM" src="https://github.com/nogibjj/sqlite-lab_rt/assets/143838819/ec700c2c-8b93-48ad-8a89-f0cc0ee5024c">

Features
Automated Logging: All CRUD operations are logged in query_logs for easy tracking.
CLI Interaction: Perform database operations through simple CLI commands.
Automated Testing: Utilizes GitHub Actions to run tests and log CRUD operations on repository updates.
Getting Started

Installation
the possible commands and their relevant arguments are:

create: To crete a Table in a SQLite DB by reading the information from the specified CSV file.
Args: (db_name, dataset, auto)
read: To run a SQLite READ query entered by the user and return the output.
Args: (db_name, table_name, query)
update: To run a SQLite UPDATE query entered by the user.
Args: (db_name, table_name, query)
delete: To run a SQLite DELETE query entered by the user.
Args: (db_name, table_name, query)
create_data: To create CSV file in the Data folder from the given source.
Args: (source, file_name, auto)
delete_data: To delete the CSV file.
Args: (file_name, auto)
clear_log: To clear the query_logs file.
Args: (log_file)
Usage
Explain how to use your application, including CLI commands and their arguments.

Example Commands:
Create: python main.py create [args] - Creates a table, etc.
Read: python main.py read [args] - Executes a read query, etc.
More commands...
Sample Execution
Show an example of the program in action, possibly with screenshots or code blocks.


Repository Structure
query_logs: Logs of CRUD operations.
README.md: This file.
requirements.txt: List of dependencies.
.github/workflows: CI/CD configurations.
Makefile: Instructions for automation processes.
.devcontainer: Configuration for the virtual environment.
Data: Default storage for generated CSV files.
resources: Additional supporting files.
Contributing
Guide on how others can contribute to your project.

Sample Execution and Test
Sample Execution: a read command is used without any arguments, so the first 5 rows of the default Database and Table are returned as expected:
<img width="981" alt="Screenshot 2023-11-28 at 11 59 32 PM" src="https://github.com/nogibjj/sqlite-lab_rt/assets/143838819/63c3e813-251c-4e39-bad8-db346ea0844e">

Testing: "make test" command is run to verify all functionalities are working as expected and to see if the CRUD actions are being performed.

Note: Coverage is intentioanlly not kept at 100% as we do not call the clear_log funtion which would clear the logs.
<img width="981" alt="Screenshot 2023-11-29 at 12 00 08 AM" src="https://github.com/nogibjj/sqlite-lab_rt/assets/143838819/3c4f1a1f-5875-4c46-97aa-e656dcbc8b69">


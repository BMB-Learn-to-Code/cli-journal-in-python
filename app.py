from database import add_items, view_items, close_connection, create_db
from datetime import datetime
# Create the menu variable with the prompt content (print the menu)
# # The prompt should contemplate three options, create a new entry (1), list all entries (2), exit the app (3)
menu = """Please select one of the following tasks
1 - Create a new entry to the journal.
2 - List all entries.
3 - Exit """

# Create a welcome variable to store the alternatice welcome message
welcome = "Welcome to your daily CLI journal"

# Create DB
create_db()

# Initiate the REPL  that collects each time the task to be executed (a while loop, if the user types tree it breaks the loop)
print(welcome)
while (user_input := input(menu)) != "3":
   if user_input == "1":
       print("Adding...")
       add_items()
   elif user_input == "2":
       print("Viewing...")
       entries = view_items()
       for entry in entries:
        print(datetime.fromisoformat(entry[1]).strftime("%Y-%m-%d %H:%M:%S"), f"- {entry[0]}\n")
   else:
       print("Invalid option please chose an option from 1 to 3")

close_connection()

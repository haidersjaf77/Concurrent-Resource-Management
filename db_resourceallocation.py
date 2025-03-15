import threading
import time

class Database:
    def __init__(self):
        self.locked = False

    def execute_transaction(self, user):
        while self.locked:
            time.sleep(1)
        self.locked = True
        print(f"User {user.name} executes a transaction.")
        time.sleep(2)
        self.locked = False

# List of User objects
users = [User("A"), User("B")]

# Create a Database object
database = Database()

# List to store thread objects
threads = []

# Create and start threads for each user to execute a transaction on the database
for user in users:
    t = threading.Thread(target=database.execute_transaction, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

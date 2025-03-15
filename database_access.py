import threading
import time

class User:
    def __init__(self, name):
        self.name = name
        self.transactions = []

# Function to simulate reading data for a user
def read_data(user):
    user.transactions.append("read")
    print(f"User {user.name} reads data.")
    time.sleep(2)

# Function to simulate writing data for a user
def write_data(user):
    user.transactions.append("write")
    print(f"User {user.name} writes data.")
    time.sleep(2)

# List of User objects
users = [User("A"), User("B")]

# Function to execute a transaction for a user
def execute_transaction(user):
    print(f"User {user.name} starts a transaction.")
    read_data(user)
    write_data(user)
    print(f"User {user.name} finishes a transaction.")

# List to store thread objects
threads = []

# Create and start threads for each user
for user in users:
    t = threading.Thread(target=execute_transaction, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

def execute_transaction(user):
    print(f"User {user.name} starts a transaction.")
    
    while True:
        with threading.Lock():
            if database.locked:
                print(f"User {user.name} is waiting for the database to be released.")
                time.sleep(1)
            else:
                database.locked = True
                break

    read_data(user)
    write_data(user)

    with threading.Lock():
        database.locked = False

    print(f"User {user.name} finishes a transaction.")

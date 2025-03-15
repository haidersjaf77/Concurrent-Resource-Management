import threading

# Assume that no user requests a transaction
system_state = {
    'user_A': {'read_server': False, 'write_server': False},
    'user_B': {'read_server': False, 'write_server': False},
}

# Check if there's a risk of deadlock
def check_for_deadlock(system_state, user, server):
    system_state[user][server] = True
    if is_circular_wait(system_state):
        return True
    for other_user in ['user_A', 'user_B']:
        if other_user != user:
            for other_server in ['read_server', 'write_server']:
                if system_state[other_user][other_server]:
                    return check_for_deadlock(system_state, other_user, other_server)
    return False

# Check if there's a circular wait
def is_circular_wait(system_state):
    count = 0
    for user in ['user_A', 'user_B']:
        for server in ['read_server', 'write_server']:
            if system_state[user][server]:
                count += 1
    return count == 2

# Grant access to a user for a specific server
def grant_resource(system_state, user, server):
    system_state[user][server] = True
    print(f"Access granted to {server} for {user}.")

# Deny access or schedule it for later
def deny_or_schedule_resource(system_state, user, server):
    print(f"Access to {server} for {user} is denied.")

# Request access to a server
def request_resource(system_state, user, server):
    if not system_state[user][server]:
        if not check_for_deadlock(system_state, user, server):
            grant_resource(system_state, user, server)
            print(f"Access granted to {server} for {user}.")
        else:
            deny_or_schedule_resource(system_state, user, server)
    else:
        print(f"{user} already has access to {server}.")

# Create threads for Users A and B to request access concurrently
thread_a = threading.Thread(target=request_resource, args=(system_state, 'user_A', 'read_server'))
thread_b = threading.Thread(target=request_resource, args=(system_state, 'user_B', 'write_server'))

# Start the threads concurrently
thread_a.start()
thread_b.start()

# Wait for both threads to finish
thread_a.join()
thread_b.join()

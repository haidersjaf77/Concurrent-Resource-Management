# Grant access to User A for the read server
grant_resource(system_state, 'user_A', 'read_server')
print("User A granted access to read server.")

# Grant access to User B for the write server
grant_resource(system_state, 'user_B', 'write_server')
print("User B granted access to write server.")

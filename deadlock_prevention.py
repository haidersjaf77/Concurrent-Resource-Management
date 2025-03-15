# Release resources after completing tasks
def release_resources(system_state, user, server):
    # Release resources in a specific order
    if user == 'user_A':
        grant_resource(system_state, 'user_A', 'write_server')
        grant_resource(system_state, 'user_B', 'read_server')
        print("Resources released for User A.")
    elif user == 'user_B':
        grant_resource(system_state, 'user_B', 'read_server')
        grant_resource(system_state, 'user_A', 'write_server')
        print("Resources released for User B.")

release_resources(system_state, 'user_A', 'read_server')
release_resources(system_state, 'user_B', 'write_server')

"""• Task: Refactor inefficient linear searches using appropriate data structures.
• Focus Areas:
o Time complexity
o Data structure choice
Legacy Code:
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
    if u == name:
        found = True
print("Access Granted" if found else "Access Denied")
"""
#Refactor inefficient linear searches using appropriate data structures
class UserManager:
    """
    A class to manage user access by storing usernames in a set for efficient lookup.
    
    This class encapsulates the logic for checking if a username exists in the user list, providing O(1) time complexity for lookups.
    """
    
    def __init__(self, users):
        """
        Initialize the UserManager with a list of users.
        
        Parameters:
        users (list): A list of usernames to be managed.
        """
        self.users = set(users)  # Using a set for O(1) average time complexity on lookups
    
    def check_access(self, name):
        """
        Check if the given username exists in the user set and return access status.
        
        Parameters:
        name (str): The username to check for access.
        
        Returns:
        str: "Access Granted" if the user exists, otherwise "Access Denied".
        """
        return "Access Granted" if name in self.users else "Access Denied"
# Example usage
if __name__ == "__main__":
    users = ["admin", "guest", "editor", "viewer"]
    user_manager = UserManager(users)
    name = input("Enter username: ")
    access_status = user_manager.check_access(name)
    print(access_status)
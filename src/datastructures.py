"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

        # Initial family members
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # This method generates a random ID for new members
    def _generateId(self):
        return randint(0, 99999999)

    # Adds a new member to the family
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    # Deletes a member by ID
    def delete_member(self, id):
        initial_count = len(self._members)
        self._members = [m for m in self._members if m["id"] != id]
        return len(self._members) < initial_count

    # Returns a specific member by ID
    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    # Returns all family members
    def get_all_members(self):
        return self._members


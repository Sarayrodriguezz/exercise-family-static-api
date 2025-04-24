
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  # para IDs secuenciales
        self._members = []
        # Miembros iniciales
        self.add_member({"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]})
        self.add_member({"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]})
        self.add_member({"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]})

    # generar IDs secuenciales
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["last_name"] = self.last_name
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
facility_list = []
def get_last_id():
    if facility_list:
        last_facility = facility_list[-1]
    else:
        return 1
    return last_facility.id + 1
class Facility:
    def __init__(self, name, description, location):

        self.id = get_last_id()
        self.name = name
        self.description = description
        self.location = location

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location
        }
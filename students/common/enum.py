import enum
class Faculty(str,enum.Enum):
    SCIENCE = 'science'
    COMMERCE = 'commerce'
    ART = 'art'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

class Hobby(str, enum.Enum):
    CRICKET = 'cricket'
    TENNIS = 'tennis'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

class Status(str,enum.Enum):
    ENROLLED = 'Enrolled'
    COMPLETED = 'Completed'
    DROPPED = 'Dropped'
    WITHDRAWN = 'Withdrawn'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

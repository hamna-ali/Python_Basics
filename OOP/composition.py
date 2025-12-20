class Finger:
    def move(self):
        return "Finger is moving"


class Body:
    def __init__(self):
        self.fingers = [Finger() for _ in range(5)]

    def move_fingers(self):
        return [finger.move() for finger in self.fingers]


body = Body()
print(body.move_fingers())

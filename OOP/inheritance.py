class OutdoorGame:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def play(self):
        return f"{self.name} is being played with {self.players} players."


class Soccer(OutdoorGame):
    def __init__(self):
        super().__init__("Soccer", 11)


class Cricket(OutdoorGame):
    def __init__(self):
        super().__init__("Cricket", 11)


soccer = Soccer()
cricket = Cricket()

print(soccer.play())
print(cricket.play())

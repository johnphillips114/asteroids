class Score():
    def __init__(self):
        self.score = 0

    def update(self, dt):
        self.score += (1 * dt)
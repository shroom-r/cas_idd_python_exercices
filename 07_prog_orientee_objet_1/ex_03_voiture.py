class Car:
    def __init__(self, x, y, direction):
        self.x = float(x)
        self.y = float(y)
        self.direction = direction

    def state(self):
        print(f'Car: x={self.x} y={self.y} direction={self.direction}')

    def forward(self, value = 1):
        if self.direction == 'up':
            self.y += value
        elif self.direction == 'right':
            self.x += value
        elif self.direction == 'down':
            self.y -= value
        elif self.direction == 'left':
            self.x -= value
    
    def right(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'up'

    def left(self):
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'down':
            self.direction = 'right'
        elif self.direction == 'left':
            self.direction = 'down'
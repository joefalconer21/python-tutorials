# usually we only have one class per file

# we have to pass a default argument, generally called self, at the very least
# self refers to and gives us info on the current instance of a class
# it doesn't have to be called self

class Monster:
    hit_points = 1
    color = 'yellow'
    weapon = 'sword'
    sound = 'roar'

    def battlecry(self):
        return self.sound.upper()

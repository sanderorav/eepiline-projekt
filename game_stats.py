class GameStats():
    
    
    def __init__(self):
        self.game_active = False
        self.reset_stats()
        self.music_on = True
    
    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.bonus = 0
        self.record = self.record_loader()
        self.min_speed = 1
        self.max_speed = 5
    
    def record_loader(self):
        with open ("record.txt", "r") as file:
            record = int(file.read())
        return record
    
    def record_saver(self, new_record):
        if new_record > self.record:
            self.record = new_record
            with open ("record.txt", "w") as file:
                file.write(str(new_record))
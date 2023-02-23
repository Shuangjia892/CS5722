class CdPlayer:
    def __init__(self, description, amplifier):
        self.description = description
        self.currentTrack = 0
        self.amplifier = amplifier
        self.title = None
        self.on_track_finished_callback = None

    def on(self):
        print(self.description + " on")

    def off(self):
        print(self.description + " off")

    def eject(self):
        self.title = None
        print(self.description + " eject")

    def play(self, title):
        self.title = title
        self.currentTrack = 0
        print(self.description + ' playing "' + self.title + '"')

    def playTrack(self, track):
        if self.title is None:
            print(self.description + " can't play track " + str(track) + ", no cd inserted")
        else:
            self.currentTrack = track
            print(self.description + " playing track " + str(self.currentTrack))

    def stop(self):
        self.currentTrack = 0
        print(self.description + " stopped")

    def pause(self):
        print(self.description + ' paused "' + self.title + '"')

    def __str__(self):
        return self.description
    

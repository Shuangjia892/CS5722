from CDplayer import CdPlayer


class Amplifier:
    def __init__(self, description, cd_player):
        self.description = description
        self.cd_player = cd_player
        self.volume = 0

    def on(self):
        print(self.description + " on")

    def off(self):
        print(self.description + " off")

    def setVolume(self, volume):
        self.volume = volume
        print(self.description + " setting volume to " + str(self.volume))

    def __str__(self):
        return self.description
    
class MusicPlayer:
    def __init__(self):
        self.amplifier = Amplifier("Top-O-Line Amplifier", None)
        self.cd_player = CdPlayer("CD Player", self.amplifier)

    def play(self, title):
        self.cd_player.play(title)

music_player = MusicPlayer()
music_player.play("Stairway to Heaven")
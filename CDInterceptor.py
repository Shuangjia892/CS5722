from cdplayer import CdPlayer

#Create a cdplayer interceptor    
class CdPlayerInterceptor(CdPlayer):
    def __init__(self, description, amplifier):
        super().__init__(description, amplifier)
        self.intercepted_title = None
        self.interceptor = None

    def play(self, title):
        if self.interceptor:
            intercepted_title = self.interceptor(title)
            if intercepted_title:
                title = intercepted_title
        super().play(title)

    def set_interceptor(self, interceptor):
        self.interceptor = interceptor


def interceptor(title):
    if title == "Bad Song":
        return "Good Song"
    return title

cd_player = CdPlayerInterceptor("CD Player", "Amplifier")
cd_player.set_interceptor(interceptor)
cd_player.play("Bad Song")
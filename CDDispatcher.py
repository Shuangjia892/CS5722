from CDplayer import CdPlayer

class CdPlayerDispatcher:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, message_type, handler):
        if message_type not in self.handlers:
            self.handlers[message_type] = []
        self.handlers[message_type].append(handler)

    def dispatch(self, message):
        message_type = type(message)
        if message_type in self.handlers:
            handlers = self.handlers[message_type]
            for handler in handlers:
                handler(message)
        else:
            print(f"No handler registered for message type: {message_type}")

cd_player = CdPlayer("CD Player", "Amplifier")
dispatcher = CdPlayerDispatcher()

def play_handler(title):
    cd_player.play(title)

dispatcher.register_handler(str, play_handler)

dispatcher.dispatch("Bad Song")
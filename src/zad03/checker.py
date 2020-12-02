from src.zad03.env import Env


class Checker:
    def __init__(self):
        self.env = Env()

    def remainder(self, file):
        time = self.env.getTime()

        if time > 17:
            self.env.playWavFile(file)
            return self.env.wavWasPlayed(file)
        else:
            return self.env.resetWav(file)

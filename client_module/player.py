import vlc


class player:
    def __init__(self):
        self.instance = vlc.Instance("--fullscreen")
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new("sample2.mp4")
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.play()

    def set_time(self, time_to_set):
        self.player.set_time(time_to_set)

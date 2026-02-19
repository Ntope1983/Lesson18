import random


# Represents a single video item
class Video:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Artist:{self.artist}\nTitle:{self.title}\nDuration:{self.duration}"


# Playlist holds multiple videos
class Playlist:
    def __init__(self, title, description, duration, videos=None):
        self.title = title
        self.description = description
        self.duration = duration
        self.videos = videos if videos is not None else []

    def add_video(self, video):
        self.videos.append(video)

    def __str__(self):
        header = f"Title:{self.title},Description:{self.description},Duration:{self.duration}\n"
        videos_text = "\n".join(str(video) for video in self.videos)
        return header + videos_text

    # Return random video recommendation
    def recommendation(self):
        if self.videos:
            return random.choice(self.videos)
        print("There is no video in this playlist")
        return None


# Specialized playlist for classical music
class ClassicalPlaylist(Playlist):
    def __init__(self, title, description, duration, videos, period):
        super().__init__(title, description, duration, videos)
        self.period = period

    # Recommend first video instead of random
    def recommendation(self):
        if self.videos:
            return self.videos[0]
        print("There is no video in this playlist")
        return None


def main():
    p = Playlist("Zouzounia", "Paidika tragoudia", "45.18",
                 [Video("ZouzTV", "Xarwpa ta dio mou xeria ta xtipw", "03.22"),
                  Video("ZouzTv", "Magia i melissa", "04.17")])

    print(p)
    print("Recomendation1",p.recommendation())

    c = ClassicalPlaylist("Beethoven No.9", "", "88.13",
                          [Video("Beethoven", "Track 01", "03.22"),
                           Video("Beethoven", "Track 02", "04.17")], "baroque")

    print(c)
    print("Recomendation2",c.recommendation())


main()
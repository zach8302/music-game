from time import sleep

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.songwriting = 0
        self.production = 0
        self.singing = 0
        self.guitar = 0
        self.piano = 0
        self.bass = 0
        self.drums = 0
        self.fame = 0
        self.equipment = 0
        self.money = 200

    def singing_lesson(self):
        if self.singing < 100:
            self.singing += 10

    def production_class(self):
        if self.production < 100:
            self.production += 10

    def guitar_lesson(self):
        if self.guitar < 100:
            self.guitar += 10

    def life_experience(self):
        if self.songwriting < 100:
            self.songwriting += 10

    def make_tiktok(self):
        if self.fame < 100:
            self.fame += 10

    def release_song(self, draft, band=None):
        if band:
            hype = band.fame
        else:
            hype = self.fame
        draft.hype = hype
        draft.released = True
        return draft

    def write_song(self, name, writer, producer, singer=None, guitarist=None):
        a = writer.songwriting
        b = producer.production
        if writer.songwriting > producer.production + 20:
            a = producer.production + 20
        elif writer.songwriting < producer.production - 20:
            b = writer.songwriting + 20
        quality = 10 * (a + b) // 200
        draft = Song(name, quality, 0)
        return draft

class Shop():
    def __init__(self):
        self.items = []

class Song():
    def __init__(self, name, quality, hype):
        self.quality = quality
        self.growth = 1.7 ** (quality)
        self.name = name
        self.hype = hype
        self.released = False
        self.sales = 0

class Band():
    def __init__(self, name, musiscians):
        self.musicians = musiscians
        self.songs = []
        self.name = name
        self.fame = sum([m.fame for m in musiscians])

def elapse_week_song(song, artist):
    sales = int(song.growth * song.hype)
    artist.fame += sales // 10
    artist.fame = min(100, artist.fame)
    song.growth *= 0.6
    song.sales += sales
    artist.money += sales

def elapse_week(songs, artist):
    artist.money -= 30
    for song in songs:
        elapse_week_song(song, artist)

def display_charts(released):
    released.sort(key=lambda x: x.sales, reverse=True)
    for s in released:
        print(f"{s.name}: {s.sales} units sold, {s.quality}/10 quality")
    print("\n")

def player_stats(player):
    print(player.name)
    print(f"Fame: {player.fame}")
    print(f"Money: {player.money}")
    print(f"Guitar: {player.guitar}")
    print(f"Singing: {player.singing}")
    print(f"Songwriting: {player.songwriting}")
    print(f"Production: {player.production}\n")

    

print("What is your name?")
name = input()
player = Player(name)
drafts = []
released = []
print("\n")

while player.money > 0:

    print("Player:")
    player_stats(player)
    sleep(2)

    print("Charts:")
    display_charts(released)
    sleep(3)

    print("What would you like to do?\n[w] Write Song\n[r] Release Song\n[t] Train ($50)\n[l] Live Life\n[h] Make a TikTok")
    choice = input()

    if choice == "w":
        print("\nWhat is the song called:")
        name = input()
        draft = player.write_song(name, player, player, player, player)
        drafts.append(draft)
    elif choice == "r":
        print("\nWhich song # would you like to release:")
        for i, d in enumerate(drafts):
            print(f"{i}: {d.name}")
        ind = input()
        if not ind.isdigit():
            continue
        ind = int(ind)
        if 0 <= int(ind) < len(drafts):
            song = player.release_song(draft=drafts[ind])
            drafts.pop(ind)
            released.append(song)
    elif choice == "t":
        player.money -= 50
        player.guitar_lesson()
        player.singing_lesson()
        player.production_class()
    elif choice == "l":
        player.life_experience()
    elif choice == "h":
        player.make_tiktok()
    elapse_week(released, player)
    print("\n")
    
print("Broke ass bitch")

    
    

    









def on_button_pressed_a():
    global count, index
    count = randint(0, 5)
    basic.show_string("MUSIC")
    basic.show_string("" + str(count))
    if count <= 1:
        basic.show_string("TIME")
    else:
        basic.show_string("TIMES")
    while index <= count - 1:
        basic.show_string("" + str((count - index)))
        music.play_melody("C C G G A A G - ", 120)
        music.play_melody("F F E E D D C - ", 120)
        music.play_melody("G G F F E E D - ", 120)
        music.play_melody("G G F F E E D - ", 120)
        music.play_melody("C C G G A A G - ", 120)
        music.play_melody("F F E E D D C - ", 120)
        basic.show_icon(IconNames.HAPPY)
        basic.pause(1000)
        basic.clear_screen()
        index += 1
    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def play_music(notes: List[number], fraq: List[number], tempo: number):
    global i, x, y
    music.set_tempo(tempo)
    i = 0
    while i <= len(notes) - 1:
        x = notes[i]
        y = fraq[i]
        if x == 0:
            music.rest(beats[y])
        else:
            music.play_tone(freqs[x], beats[y])
        i += 1

def on_button_pressed_b():
    global tunes_1, beats_1
    tunes_1 = [1, 2, 3, 1, 1, 2, 3, 1, 3, 4, 5, 3, 4, 5, 3, 0]
    beats_1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2]
    play_music(tunes_1, beats_1, 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

beats_1: List[number] = []
tunes_1: List[number] = []
y = 0
x = 0
i = 0
index = 0
count = 0
beats: List[number] = []
freqs: List[number] = []
# music notes: 1-7 for central 1-7, 8-14 for high 1-7, -1~-7 for low 1-7
freqs = [0,
    262,
    294,
    330,
    349,
    392,
    440,
    494,
    523,
    587,
    659,
    698,
    784,
    880,
    988,
    247,
    220,
    196,
    175,
    165,
    147,
    131]
# music beats: 0 for breve, 1 for double, 2 for whole, 3 for half, 4 for 1/4, 5 for 1/8, 6 for 1/16.
beats = [music.beat(BeatFraction.BREVE),
    music.beat(BeatFraction.DOUBLE),
    music.beat(BeatFraction.WHOLE),
    music.beat(BeatFraction.HALF),
    music.beat(BeatFraction.QUARTER),
    music.beat(BeatFraction.EIGHTH),
    music.beat(BeatFraction.SIXTEENTH)]
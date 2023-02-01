input.onButtonPressed(Button.A, function () {
    count = randint(0, 5)
    basic.showString("MUSIC")
    basic.showString("" + count)
    if (count <= 1) {
        basic.showString("TIME")
    } else {
        basic.showString("TIMES")
    }
    while (index <= count - 1) {
        basic.showString("" + (count - index))
        music.playMelody("C C G G A A G - ", 120)
        music.playMelody("F F E E D D C - ", 120)
        music.playMelody("G G F F E E D - ", 120)
        music.playMelody("G G F F E E D - ", 120)
        music.playMelody("C C G G A A G - ", 120)
        music.playMelody("F F E E D D C - ", 120)
        basic.showIcon(IconNames.Happy)
        basic.pause(1000)
        basic.clearScreen()
        index += 1
    }
    basic.showIcon(IconNames.Yes)
    basic.pause(1000)
    basic.clearScreen()
})
function play_music (notes: number[], fraq: number[], tempo: number) {
    music.setTempo(tempo)
    i = 0
    while (i <= notes.length - 1) {
        x = notes[i]
        y = fraq[i]
        if (x == 0) {
            music.rest(beats[y])
        } else {
            music.playTone(freqs[x], beats[y])
        }
        i += 1
    }
}
input.onButtonPressed(Button.B, function () {
    tunes_1 = [
    1,
    2,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    5,
    3,
    4,
    5,
    3,
    0
    ]
    beats_1 = [
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    1,
    2,
    2
    ]
    play_music(tunes_1, beats_1, 120)
})
let beats_1: number[] = []
let tunes_1: number[] = []
let y = 0
let x = 0
let i = 0
let index = 0
let count = 0
let beats: number[] = []
let freqs: number[] = []
// music notes: 1-7 for central 1-7, 8-14 for high 1-7, -1~-7 for low 1-7
freqs = [
0,
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
131
]
// music beats: 0 for breve, 1 for double, 2 for whole, 3 for half, 4 for 1/4, 5 for 1/8, 6 for 1/16.
beats = [
music.beat(BeatFraction.Breve),
music.beat(BeatFraction.Double),
music.beat(BeatFraction.Whole),
music.beat(BeatFraction.Half),
music.beat(BeatFraction.Quarter),
music.beat(BeatFraction.Eighth),
music.beat(BeatFraction.Sixteenth)
]

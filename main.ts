let count = 0
input.onButtonPressed(Button.A, function () {
    count = randint(0, 3)
    basic.showString("Alarm")
    basic.showString("" + count)
    basic.showString("times")
    for (let index = 0; index <= count - 1; index++) {
        music.playMelody("C C G G A A G - ", 120)
        music.playMelody("F F E E D D C - ", 120)
        music.playMelody("G G F F E E D - ", 120)
        music.playMelody("G G F F E E D - ", 120)
        music.playMelody("C C G G A A G - ", 120)
        music.playMelody("F F E E D D C - ", 120)
        basic.showIcon(IconNames.Happy)
        basic.pause(1000)
        basic.showString("" + (count - index - 1))
        basic.clearScreen()
    }
    basic.showIcon(IconNames.Yes)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Whole))
})

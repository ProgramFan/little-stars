count = 0

def on_button_pressed_a():
    global count
    count = randint(0, 5)
    basic.show_string("Alarm")
    basic.show_string("" + str((count)))
    basic.show_string("times")
    for index in range(count):
        music.play_melody("C C G G A A G - ", 120)
        music.play_melody("F F E E D D C - ", 120)
        music.play_melody("G G F F E E D - ", 120)
        music.play_melody("G G F F E E D - ", 120)
        music.play_melody("C C G G A A G - ", 120)
        music.play_melody("F F E E D D C - ", 120)
        basic.show_icon(IconNames.HAPPY)
        basic.pause(1000)
        basic.show_string(str((count - index - 1)))
        basic.clear_screen()
    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

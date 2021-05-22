"""Various utility functions"""
import gensound
import numpy as np
import easygui

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def get_list_of_notes(lower_octave_limit, higher_octave_limit):
    notes = NOTES
    notes_with_octaves = []
    for i in range(lower_octave_limit, higher_octave_limit):
        for note in notes:
            notes_with_octaves.append(note + str(i))
    return notes_with_octaves


def get_octave(note):
    if note == "pause":
        return 3
    return int(note[1])


def play_note(note, duration):
    # Get sine wave
    s = gensound.Sine(note, duration * 1000.0)

    # TODO Compensate amplitude?

    # Add fade
    fade_in = gensound.transforms.Fade(is_in=True, duration=100.0)
    s = s * fade_in

    # TODO fade out

    # Play note
    s.play()


def show_gui():
    return easygui.buttonbox("Which note?", "Note", NOTES)


def is_correct(note, answer):
    return note[:-1] == answer

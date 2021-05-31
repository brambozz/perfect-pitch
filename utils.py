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


def get_note_without_octave(note):
    return note[:-1]


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
    return get_note_without_octave(note) == answer


def note_to_number(note):
    note_to_number_dict = {}
    note_to_number_dict["C"] = 0
    note_to_number_dict["C#"] = 1
    note_to_number_dict["D"] = 2
    note_to_number_dict["D#"] = 3
    note_to_number_dict["E"] = 4
    note_to_number_dict["F"] = 5
    note_to_number_dict["F#"] = 6
    note_to_number_dict["G"] = 7
    note_to_number_dict["G#"] = 8
    note_to_number_dict["A"] = 9
    note_to_number_dict["A#"] = 10
    note_to_number_dict["B"] = 11

    return note_to_number_dict[note]


def get_distance(note_1, note_2):
    note_1 = note_to_number(note_1)
    note_2 = note_to_number(note_2)
    low_note = min([note_1, note_2])
    high_note = max([note_1, note_2])
    distance_1 = high_note - low_note
    distance_2 = 12 + low_note - high_note

    return min([distance_1, distance_2])

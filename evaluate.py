"""Evaluate perfect pitch with 100 random notes"""
import utils
import random
import pandas as pd
import time

# Parameters
n = 3
duration = 0.5
lower_octave_limit = 3
higher_octave_limit = 6  # This octave is not included in the test

# Prepare
notes = utils.get_list_of_notes(lower_octave_limit, higher_octave_limit)
df = pd.DataFrame(columns=["note", "answer", "duration"])

# Run test
for i in range(n):
    note = random.choice(notes)

    utils.play_note(note, duration)
    tic = time.time()
    answer = utils.show_gui()
    toc = time.time()
    time_interval = f"{toc-tic:.2f}"
    is_correct = utils.is_correct(note, answer)

    df.at[i] = [note, answer, time_interval]

# TODO write to csv with datetime stamp
df.to_csv("test.csv", index_label="number")

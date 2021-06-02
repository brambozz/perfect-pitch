"""Binary exercise - try to distinguish one target pitch from all others"""
import utils
import random

# Parameters
target = "C"
weight = 0.2
n = 25
duration = 1
lower_octave_limit = 3
higher_octave_limit = 6  # This octave is not included

# Prepare
notes_without_target = utils.NOTES.copy()
notes_without_target.remove(target)
target_notes = utils.get_list_of_notes(
    lower_octave_limit, higher_octave_limit, exclude=notes_without_target
)
notes = utils.get_list_of_notes(
    lower_octave_limit, higher_octave_limit, exclude=[target]
)

# Status print
print(f"Targeting {target} with weight {weight}")

# Run exercise
counter = 0
for i in range(n):
    if random.random() < weight:
        is_target = True
        note = random.choice(target_notes)
    else:
        is_target = False
        note = random.choice(notes)

    utils.play_note(note, duration)

    answer = None
    while answer != "y" and answer != "n":
        answer = utils.input_char("Is this: {target}? (y/n)")

    if is_target and answer == "y":
        print("Correct!")
        counter += 1
    elif not is_target and answer == "n":
        print("Correct!")
        counter += 1
    else:
        print("Incorrect")

# Print statistics
print(f"{counter}/{n} correct answers ({counter/n * 100}%)")

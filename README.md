# Perfect pitch

Since reading about an adult that developed perfect pitch (in the book
[Peak](http://peakthebook.com/index.html)), I want to give it a shot as
well. This repository houses some simple code to help achieve that goal.

## Evaluation

Before developing perfect pitch, I need a way to reliably assess my
progress. In other words, something that tells me: 
how perfect is my pitch? I do this by running `evaluate.py`. This is a
simple test that does the following:

1. Play 100 random notes between C2 and C6
2. For each notes, I must indicate which of the twelve notes I hear

The script tracks for each note what my choice was and how much time it
took me to answer.

## TODO

- [ ] Find a good criterion for perfect pitch following the evaluation results.

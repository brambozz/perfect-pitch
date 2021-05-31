"""Process results of an evaluate.py test run"""
import pandas as pd
import numpy as np
import argparse
import utils


class Processor:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, index_col=0)

    def run(self):
        self.correct_percentage = self._get_correct_percentage()
        self.distance = self._get_distance()

        self._pretty_print_results()

    def _get_correct_percentage(self):
        counter = 0
        for index, row in self.df.iterrows():
            if utils.is_correct(row["note"], row["answer"]):
                counter += 1

        return counter / len(self.df)

    def _get_distance(self):
        distance = []
        for index, row in self.df.iterrows():
            distance.append(
                utils.get_distance(
                    utils.get_note_without_octave(row["note"]), row["answer"]
                )
            )

        return np.array(distance)

    def _pretty_print_results(self):
        print(f"{self.correct_percentage*100} notes correct")
        for i in range(1, 7):
            print(f"{np.sum(self.distance == i)} notes {i} off")


def main(args):
    processor = Processor(args.csv_path)
    processor.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    args = parser.parse_args()
    main(args)

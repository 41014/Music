#major scale: whole whole half whole whole whole half
#integer notation!!!!!!! never heard of it until just now and it rules
import random

class Music:

    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    majorScale = [0, 2, 4, 5, 7, 9, 11]
    minorScale = [0, 2, 3, 5, 7, 8, 10]
    majorTriad = [0, 4, 7]
    minorTriad = [0, 3, 7]
    augmentedTriad = [0, 4, 8] 
    diminishedTriad = [0, 3, 6]
    majorSeventh = [0, 4, 7, 11]
    minorSeventh = [0, 3, 7, 10]
    dominantSeventh = [0, 4, 7, 10]

    def __init__(self, root):
        root = root.capitalize()
        if root.endswith("b"):
            self.notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
            self.root = root
        else:
            self.root = root
        self.chromatic = self.notes[self.notes.index(self.root):] + self.notes[:self.notes.index(self.root)]
        self.majorscale = [self.chromatic[_] for _ in self.majorScale]
        self.minorscale = [self.chromatic[_] for _ in self.minorScale]
        self.majortriad = [self.chromatic[_] for _ in self.majorTriad]
        self.minortriad = [self.chromatic[_] for _ in self.minorTriad] 
        self.augmentedtriad = [self.chromatic[_] for _ in self.augmentedTriad]
        self.diminishedtriad = [self.chromatic[_] for _ in self.diminishedTriad]
        self.majorseventh = [self.chromatic[_] for _ in self.majorSeventh]
        self.minorseventh = [self.chromatic[_] for _ in self.minorSeventh]
        self.dominantseventh = [self.chromatic[_] for _ in self.dominantSeventh]



#check check check
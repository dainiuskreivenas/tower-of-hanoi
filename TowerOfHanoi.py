"""

Tower of Hanoi expert system.
Usage new instance pass in number of discs. Run a simulation.

"""
from rbs import NealCoverFunctions
from rbs import FSAHelperFunctions
from rbs import NeuralCognitiveArchitectureBuilder

class TowerOfHanoi:
    def __init__(self, sim, simulator, discNum):
        self.neal = NealCoverFunctions(simulator, sim)
        self.fsa = FSAHelperFunctions(simulator, sim, self.neal)

        self.narc = NeuralCognitiveArchitectureBuilder(simulator, sim, self.fsa, self.neal).build()

        self.narc.addRule(
            "ToH",
            [
                (True, "ToH", ("?d",), "r1"),            
            ],
            [
                ("assert", ("tower", ("A",))),
                ("assert", ("tower", ("B",))),
                ("assert", ("tower", ("C",))),
                ("assert", ("stackTop", (0,))),
                ("assert", ("stack", (0, "goal", 1, "?d", "A", "C"))),
                ("assert", ("addDisk", ("?d", "A"))),
                ("retract", "r1")
            ]
        )

        self.narc.addRule(
            "addDisk",
            [
                (True, "addDisk", ("?d","?from"), "a"),
                ("test", ">", "?d", 1)
            ],
            [
                ("retract", "a"),
                ("assert", ("diskAt", ("?d", "?from"))),
                ("assert", ("addDisk", (("-", "?d", 1),"?from")))
            ]
        )

        self.narc.addRule(
            "addFinalDisk",
            [
                (True, "addDisk", ("?d","?from"), "a"),
                ("test", "=", "?d", 1)
            ],
            [
                ("retract", "a"),
                ("assert", ("diskAt", ("?d", "?from")))
            ]
        )

        self.narc.addRule(
            "GoalToGoals",
            [
                (True, "stack", ("?t", "goal", "?topDisc", "?bottomDisc", "?from", "?to"), "g"),
                (True, "stackTop", ("?t",), "st"),
                (True, "tower", ("?from",), "towerFrom"),
                (True, "tower", ("?to",), "towerTo"),
                (True, "tower", ("?other",), "towerOther"),
                ("test", "<>", "?from", "?other"),
                ("test", "<>", "?to", "?other"),
                ("test", "<", ("+", "?topDisc", 1), "?bottomDisc"),
            ],
            [
                ("retract", "g"),
                ("retract", "st"),
                ("assert", ("stackTop",(("+","?t",2),))),
                ("assert", ("stack", ("?t", "goal", "?topDisc", ("-", "?bottomDisc", 1), "?other", "?to"))),
                ("assert", ("stack", (("+", "?t", 1), "move", "?bottomDisc", "?from", "?to"))),
                ("assert", ("stack", (("+", "?t", 2), "goal", "?topDisc", ("-", "?bottomDisc", 1), "?from", "?other")))
            ]
        )

        self.narc.addRule(
            "GoalToMoves",
            [
                (True, "stack", ("?t", "goal", "?topDisc", "?bottomDisc", "?from", "?to"), "g"),
                (True, "stackTop", ("?t",), "st"),
                (True, "tower", ("?from",), "towerFrom"),
                (True, "tower", ("?to",), "towerTo"),
                (True, "tower", ("?other",), "towerOther"),
                ("test", "<>", "?from", "?other"),
                ("test", "<>", "?to", "?other"),
                ("test", "=", ("+", "?topDisc", 1), "?bottomDisc"),
            ],
            [
                ("retract", "g"),
                ("retract", "st"),
                ("assert", ("stackTop",(("+", "?t", 2),))),
                ("assert", ("stack", ("?t", "move", "?topDisc", "?other", "?to"))),
                ("assert", ("stack", (("+", "?t", 1), "move", "?bottomDisc", "?from", "?to"))),
                ("assert", ("stack", (("+", "?t", 2), "move", "?topDisc", "?from", "?other")))
            ]
        )

        self.narc.addRule(
            "MakeMove",
            [
                (True, "stack", ("?t","move","?disc","?from","?to"), "g"),
                (True, "stackTop", ("?t",), "st"),
                (True, "diskAt", ("?disc","?from"), "d")
            ],
            [
                ("retract", "g"),
                ("retract", "d"),
                ("retract", "st"),
                ("assert", ("diskAt",("?disc","?to"))),
                ("assert", ("stackTop",(("-","?t",1),)))
            ]
        )

        self.narc.addFact("ToH", (discNum,))

        self.narc.apply()


    def printSpikes(self, name):
        self.narc.printSpikes()

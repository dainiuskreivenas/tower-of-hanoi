"""

Tower of Hanoi 3 disc problem test

"""
#import pyNN.spiNNaker as sim
import pyNN.nest as sim

from TowerOfHanoi import TowerOfHanoi

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

#toh = TowerOfHanoi(sim, "spinnaker", 3)
toh = TowerOfHanoi(sim, "nest", 3)

sim.run(1500)

toh.printSpikes("TowerOfHanoi_3")

sim.end()
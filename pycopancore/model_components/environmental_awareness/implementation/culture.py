"""Culture process taxon mixing class template.
"""

# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

from .... import Event
from .. import interface as I
from ...base import interface as B
from numpy.random import exponential, uniform

class Culture (I.Culture):
    """Culture process taxon mixin implementation class."""

    # process-related methods:

    def next_awareness_update_time(self, t):
        """time of next awareness update"""
        res = t + exponential(1. / self.awareness_update_rate)
        return res

    def update_individuals_awareness(self, t):
        """let some individuals update their awareness"""
        for w in self.worlds:
            for i in w.individuals:
                if uniform() < self.awareness_update_fraction:
                    i.update_awareness(t)

    processes = [
                 Event("update individuals' awareness",
                       [B.Culture.worlds.individuals.is_environmentally_friendly],
                       ["time",
                        next_awareness_update_time,
                        update_individuals_awareness])                 
                 ]

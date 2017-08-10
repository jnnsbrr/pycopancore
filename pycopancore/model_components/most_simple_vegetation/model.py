"""Model mixing class most_simple_vegetation."""

# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

from . import interface as I
# import all needed entity type implementation classes:
from .implementation import Cell
# import all needed process taxon implementation classes:
# none needed


class Model (I.Model):
    """Model mixin class."""

    # mixins provided by this model component:

    entity_types = [Cell]
    """list of entity types augmented by this component"""
    process_taxa = []
    """list of process taxa augmented by this component"""
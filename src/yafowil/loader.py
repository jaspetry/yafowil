import os
import yafowil.utils


def register():
    import yafowil.common
    import yafowil.compound
    import yafowil.table
    import yafowil.plans


for ep in yafowil.utils.get_entry_points('register'):
    ep.load()()

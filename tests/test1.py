# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:24:31 2019

@author: nicka
"""
import sys
import json
from DiscreteLatticeMech import Solver, Writer

if __name__ == "__main__":

    filepath = 'InputData_CarreReentrantEx.json'

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except IOError as error:
        print("could not open input file {}".format(filepath))
        sys.exit(1)

    solver = Solver()
    solver.solve(data)

    writer = Writer()
    writer.WriteTensorsToFile(solver.CMatTensor, solver.FlexMatTensor)
    writer.WriteEffectivePropertiesToFile(solver.Bulk, solver.Ex, solver.Ey, solver.Poissonyx, solver.Poissonxy, solver.G, solver.rho)
    writer.PlotEffectiveProperties(solver.Bulk, solver.Ex, solver.Ey, solver.Poissonyx, solver.Poissonxy, solver.G)
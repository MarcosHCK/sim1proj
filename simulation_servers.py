# Copyright (c) 2023-2025
# This file is part of sim1proj.
#
# sim1proj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sim1proj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sim1proj. If not, see <http://www.gnu.org/licenses/>.
#
from curses_simulation import CursesSimulation
from distributions import distributions
from simulation_stats import StatSimulation
import argparse

def run_simulation(max_client=5, min_client=1, max_server=10, min_server=5, c=0, n=10, G='uniform', Gi=None, M='uniform', duration=10):

    parser = argparse.ArgumentParser(description='sim1proj')
    parser.add_argument('--max-client', default=max_client, help='Max wait time for clients', metavar='INTEGER', type=int)
    parser.add_argument('--min-client', default=min_client, help='Min wait time for clients', metavar='INTEGER', type=int)
    parser.add_argument('--max-server', default=max_server, help='Max wait time for servers', metavar='INTEGER', type=int)
    parser.add_argument('--min-server', default=min_server, help='Min wait time for servers', metavar='INTEGER', type=int)
    parser.add_argument('-c', default=c, help='Initial number of simulated clients', metavar='INTEGER', type=int)
    parser.add_argument('-n', default=n, help='Number of simulated servers', metavar='INTEGER', type=int)
    parser.add_argument('-G', default=G, help='Distribution for all service\'s time', metavar='NAME', type=str)
    parser.add_argument('-Gi', default=Gi, help='Distribution for i-nth service\'s time', metavar='N:NAME', type=str)
    parser.add_argument('-M', default=M, help='Distribution for client arrival time', metavar='NAME', type=str)
    parser.add_argument('--duration', type=int, default=duration, help='Duration of the simulation in seconds')

    args = parser.parse_args()

    Gidist = [ lambda: distributions [dist] (args.max_server, args.min_server) for dist in Gi ] if Gi != None else [ lambda: distributions[args.G] (args.max_server, args.min_server) for i in range(args.n) ]
    Mdist = lambda: distributions[args.M] (args.max_client, args.min_client)

    simulation = CursesSimulation(args.n, Gidist, Mdist)

    for i in range(args.c):
        simulation.pushClient()

    simulation.simulate(args.duration, 0.001)

    print(f'cycleCount = {simulation.cycleCount}')
    print(f'maxClientsInQueue = {simulation.maxClientsInQueue}')
    print(f'maxClientWaitTime = {simulation.maxClientWaitTime}')
    print(f'meanClientWaitTime = {simulation.meanClientWaitTime}')
    print(f'totalClientsServed = {simulation.totalClientsServed}')
    print(f'totalWaitTime = {simulation.totalWaitTime}')
    print(f'totalUsageTime = {simulation.totalUsageTime}')
    print(f'averageServiceTimePerClient = {simulation.averageServiceTimePerClient}')
    print(f'max-client = {args.max_client}')
    print(f'min-client = {args.min_client}')
    print(f'max-server = {args.max_server}')
    print(f'min-server = {args.min_server}')
    print(f'initial number of simulated clients = {args.c}')
    print(f'number of simulated servers = {args.n}')
    print(f'distribution for all service\'s time = {args.G}')
    print(f'distribution for i-nth service\'s time = {args.Gi}')
    print(f'distribution for client arrival time = {args.M}')
    print(f'duration = {args.duration}')

    results = [simulation.cycleCount, simulation.maxClientsInQueue, simulation.maxClientWaitTime, simulation.meanClientWaitTime, simulation.totalClientsServed, simulation.totalWaitTime, simulation.totalUsageTime, simulation.averageServiceTimePerClient]
    results.extend([args.max_client, args.min_client, args.max_server, args.min_server, args.c, args.n, args.G, args.Gi, args.M, args.duration]) # Agregar los argumentos al final de los resultados
    StatSimulation.save(results)

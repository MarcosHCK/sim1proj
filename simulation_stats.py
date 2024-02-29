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
from simulation import Simulation
import csv, os

class StatSimulation(Simulation):
    cycleCount =   0
    maxClientsInQueue =   0
    maxClientWaitTime =   0
    totalClientsServed =   0
    totalWaitTime =   0
    totalServiceTime =   0 

    @property
    def meanClientWaitTime(self) -> float:
        return self.totalWaitTime / self.totalClientsServed

    @property
    def totalUsageTime(self) -> float:
        return self.totalWaitTime + self.totalServiceTime

    @property
    def averageServiceTimePerClient(self) -> float:
        return self.totalServiceTime / self.totalClientsServed

    def completeCycle(self, timeUnit: float):
        super().completeCycle(timeUnit)
        self.cycleCount = self.cycleCount +   1

    def updateClientQueue(self):
        super().updateClientQueue()
        self.maxClientsInQueue = max(self.maxClientsInQueue, len(self.clients))

    def updateServerAsFinished(self, i: int):
        super().updateServerAsFinished(i)
        self.maxClientWaitTime = max(self.maxClientWaitTime, self.servers[i].client.tl)
        self.totalClientsServed = self.totalClientsServed +   1
        self.totalWaitTime = self.totalWaitTime + self.servers[i].client.tl
        self.totalServiceTime = self.totalServiceTime + self.servers[i].ttl  # Asumiendo que ttl es el tiempo de servicio del cliente

    def save(lista_valores):
        filename = 'results.csv'
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as archivo_csv:
                pass  
      
        with open(filename, 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            filas_vacias = [] 
            for i, fila in enumerate(reader):
                if not any(fila): 
                    filas_vacias.append(i)
           
            if not filas_vacias:
                filas_vacias.append(len(list(reader)))

        with open(filename, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(lista_valores)

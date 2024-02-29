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
from collections import namedtuple
from typing import Callable
import time

Client = namedtuple ('Client', [ 'tl', 'id' ])
Server = namedtuple ('Server', [ 'ttl', 'client' ])
MAX_QUEUE_LENGTH = 20
TOTAL_CLIENTES_ATENDIDOS = 1000


class Simulation:

  clients = []
  nextClient = 1
  nextClientIn = 0

  def beginCycle (self):
    pass

  def completeCycle (self, timeUnit: float):

    time.sleep (timeUnit)

  def pushClient (self):

    client = Client (tl = 0, id = self.nextClient)

    self.nextClient = self.nextClient + 1
    self.nextClientIn = self.Mdist ()
    self.clients.append (client)

  def simulate(self, duration, timeUnit: float):
    start_time = time.time()
    elapsed_time = 0
    total_clientes_atendidos = 0 

    while elapsed_time < duration:
        self.beginCycle()

        for i in range(self.servers.__len__()):
            self.updateServer(i)

        self.updateClientQueue()
        self.completeCycle(timeUnit)

        if total_clientes_atendidos >= TOTAL_CLIENTES_ATENDIDOS:
            print(f"La simulación ha sido detenida después de atender {total_clientes_atendidos} clientes.")
            break

        elapsed_time = time.time() - start_time

        total_clientes_atendidos += self.servers.__len__() 
        
  def updateClientQueue (self):

    for i in range (self.clients.__len__ ()):

      self.updateClientTL (i)

    if (self.nextClientIn > 0):

      self.updateClientQueueTTL ()
    else:

      self.pushClient ()

  def updateClientTL (self, i: int):

    self.clients[i] = Client (id = self.clients[i].id, tl = self.clients[i].tl + 1)

  def updateClientQueueTTL (self):

    self.nextClientIn = self.nextClientIn - 1

  def updateServer (self, i: int):

    if (self.servers[i].ttl > 0):

      self.updateServerTTL (i)
    else:

      if (self.clients.__len__ () == 0):

        self.updateServerAsIdle (i)
      else:

        self.updateServerAsFinished (i)

  def updateServerTTL (self, i: int):

    self.servers[i] = Server (client = self.servers[i].client, ttl = self.servers[i].ttl - 1)

  def updateServerAsIdle (self, i: int):

    pass

  def updateServerAsFinished (self, i: int):

    self.servers[i] = Server (client = self.clients.pop (), ttl = self.Gidist[i] ())

  def __init__ (self, n: int, Gidist: [Callable [[], int]], Mdist: Callable [[], int]):

    self.clients = [ ]
    self.servers = [ Server (0, 0) for i in range (n) ]

    self.Gidist = Gidist
    self.Mdist = Mdist

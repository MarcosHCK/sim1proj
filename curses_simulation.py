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
from simulation_stats import StatSimulation
import curses

class CursesSimulation (StatSimulation):

  def simulate (self, duration,timeUnit: float):

    self.scr = curses.initscr ()

    try:

        super ().simulate (duration, timeUnit)
 
    except KeyboardInterrupt:

      curses.endwin ()

    except Exception as e:

      curses.endwin ()
      raise e

    curses.endwin ()

  def beginCycle (self):

    super ().beginCycle ()
    self.scr.clear ()

  def completeCycle (self, timeUnit: float):

    super ().completeCycle (timeUnit)
    self.scr.refresh ()

  def updateClientQueue (self):

    super ().updateClientQueue ()
    self.scr.addstr (self.servers.__len__ (), 0, f'clients in queue {self.clients.__len__ ()}')

  def updateServerTTL (self, i: int):

    super ().updateServerTTL (i)
    self.scr.addstr (i, 0, f'server {i} is busy with {self.servers[i].client.id}')

  def updateServerAsIdle (self, i: int):

    super ().updateServerAsIdle (i)
    self.scr.addstr (i, 0, f'server {i} is idle')

  def updateServerAsFinished (self, i: int):

    client = self.clients[-1]

    super ().updateServerAsFinished (i)
    self.scr.addstr (i, 0, f'server {i} got client {client.id}')

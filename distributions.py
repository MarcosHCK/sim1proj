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
import random
from scipy.stats import poisson, expon

def uniform(minN: int, maxN: int) -> int:
    return int(random.uniform(minN, maxN))

def normal(minN: int, maxN: int) -> int:
    mean = (maxN + minN) / 2
    sdev = (maxN - minN) / (2 * 1.645)
    return int(random.normalvariate(mean, sdev))

def poisson_distribution(minN: int, maxN: int) -> int:
    lambda_ = (maxN + minN) / 2
    return int(poisson.rvs(mu=lambda_, size=1)[0])

def exponential_distribution(max_value: float, min_value: float) -> float:
    scale = max_value - min_value 
    return float(expon.rvs(scale=scale, size=1)[0])

distributions = {
    'normal': normal,
    'uniform': uniform,
    'poisson': poisson_distribution,
    'exponential': exponential_distribution
}

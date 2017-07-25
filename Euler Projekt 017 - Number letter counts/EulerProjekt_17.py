# -*- coding: utf-8 -*-
"""
Created on Jul 22, 2017
@author: Ancient Abysswalker
"""

from num2text import *
import re

print(sum(len(re.sub('[ -]', '',i)) for i in [n2t(j) for j in range(1,1001)]))
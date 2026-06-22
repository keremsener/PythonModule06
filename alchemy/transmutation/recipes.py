# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:00:10 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:00:14 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..potions import strength_potion
from alchemy.elements import create_air
import elements

def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}'\
and '{strength_potion()}' mixed with '{elements.create_fire()}'"

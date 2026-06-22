# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:00:31 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:12:06 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_earth, create_air
import elements


def strength_potion() -> str:
    return f"Strength potion brewed with\
 '{elements.create_fire()}' and '{elements.create_water()}'"


def healing_potion() -> str:
    return f"Healing potion brewed\
 with '{create_earth()}' and '{create_air()}'"

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 11:39:16 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 11:52:47 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    status = validate_ingredients(ingredients)
    
    if "INVALID" in status:
        return f"Spell rejected: {spell_name} ({status})"
    return f"Spell recorded: {spell_name} ({status})"
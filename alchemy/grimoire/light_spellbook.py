# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 11:29:43 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:10:47 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator
    status = light_validator.validate_ingredients(ingredients)

    if "INVALID" in status:
        return f"Spell rejected: {spell_name} ({status})"
    return f"Spell recorded: {spell_name} ({status})"

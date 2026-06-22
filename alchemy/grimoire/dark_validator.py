# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_validator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 11:43:43 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:10:42 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    for item in allowed_ingredients:
        if item in ingredients_lower:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"

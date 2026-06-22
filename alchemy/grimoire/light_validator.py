# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_validator.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 11:38:27 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 11:38:39 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from . import light_spellbook

def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spellbook.light_spell_allowed_ingredients()
    
    ingredients_lower = ingredients.lower()
    
    for item in allowed_ingredients:
        if item in ingredients_lower:
            return f"{ingredients} VALID"  
    return f"{ingredients} INVALID"

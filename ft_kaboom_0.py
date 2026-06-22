# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:07:13 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:07:18 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire.light_spellbook as light_spellbook

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:", light_spellbook.light_spell_record("Fantasy", "Earth, wind and fire"))

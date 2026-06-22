# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:03:38 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:04:33 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print("Testing strength_potion:", alchemy.strength_potion())
    print("Testing heal alias:", alchemy.heal())

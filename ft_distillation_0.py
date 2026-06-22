# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:03:31 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:03:34 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import strength_potion, healing_potion

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", strength_potion())
    print("Testing healing_potion:", healing_potion())

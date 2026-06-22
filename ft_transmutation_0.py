# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:07:25 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:16:38 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation.recipes

if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    path = alchemy.transmutation.recipes
    print(path.lead_to_gold())

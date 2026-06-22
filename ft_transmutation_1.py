# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:07:32 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:07:37 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    path =  alchemy.transmutation
    print("Import transmutation module directly")
    print("Testing lead to gold:", path.lead_to_gold())

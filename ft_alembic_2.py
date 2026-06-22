# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_2.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:00:53 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:00:56 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements

if __name__ == "__main__":
    elements = alchemy.elements
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", elements.create_earth())

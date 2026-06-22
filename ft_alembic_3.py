# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:00:57 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:01:01 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...'\
 structure")
    print("Testing create_air:", create_air())

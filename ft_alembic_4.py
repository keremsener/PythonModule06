# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ksener <ksener@student.42kocaeli.com.tr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/22 12:01:03 by ksener          #+#    #+#               #
#  Updated: 2026/06/22 12:09:13 by ksener          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")

    print("Testing create_air:", alchemy.create_air())
    print("Testing the hidden create_earth:", alchemy.create_earth())

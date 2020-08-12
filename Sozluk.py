K1 = { 1, 2, 4, 5, 7, 8, 9}
K2 = { 3, 4, 5, 6, 10}
K1, K2 -> ({ 1, 2, 4, 5, 6, 7, 8, 9}, { 3, 4, 5, 6, 10})
K1 | K2 	-> { 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10}	# Birlesdirme (union)
K1 – K2 	-> {1, 2, 7, 8, 9}			# Ferqi (difference)
K1 & K2		-> {4, 5, 6}				# Kesisme (intersection)
K1 ^ K2	-> {1, 2, 3, 7, 8, 9, 10}			# Simetrik ferq (symmetric_difference)


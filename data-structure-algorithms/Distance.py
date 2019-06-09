########################################################################


########################################################################

import numpy as np
from tqdm import tqdm

########################################################################


def Euclidean(points, target=None):
    '''
    The simplist euclidean distance is the result of 
    "Pythagorean theorem", indicating the shortest distance between
    points.
                                  _____________________
    - The mathematical formula = V(B1-A1)^2 + (B2-A2)^2

    If the dimensions are getting higher, it can be B3, B4, B5...
    '''
    rows = points.shape[0]

    if target is not None:
        # target = np.tile(target, (rows, 1))
        dist = np.square(target - points)
        dist = np.sqrt(np.sum(dist, axis=1))
        return dist.reshape(rows, -1)

    else:
        matrix = np.zeros((rows, rows))
        points_t = points.transpose()

        for i in range(rows):
            for j in range(rows):
                dist = np.square(points[i, :] - points_t[:, j])
                matrix[i][j] = np.sqrt(np.sum(dist))

        return matrix


########################################################################

# if __name__ == '__main__':
# 	points_2d = np.array([[0.0, 0.0],
# 	                      [0.0, 0.1],
# 	                      [0.1, 0.0],
# 	                      [0.1, 0.1],
# 	                      [1.0, 1.0],
# 	                      [1.0, 1.1],
# 	                      [1.1, 1.0],
# 	                      [1.1, 1.1]])
# 	print(points_2d.transpose())

#     a = Euclidean(points_2d, target=[0.0, 0.0])
#     print(a)

########################################################################

class Levenshtein:
	"""docstring for Levenshtein"""
	def __init__(self, threshold=4):
		self.threshold = threshold
		self.matrix = None

	def distance(self, from_str, to_str):
	    # Read the info of inputs strings and create an empty matrix.
		rows, cols = (len(to_str) + 1, len(from_str) + 1)
		matrix = np.tile([-1], rows * cols).reshape(rows, cols)
		
		# If the 2 elements are identical, do not calculate.
		if from_str == to_str:
			self.matrix = matrix + 1
			return 0

		else:
		    # Attach the first cols and rows to the matrix.
			matrix[0, :] = np.arange(cols)
			matrix[:, 0] = np.arange(rows)

			# Iterate through each elements in the string accordingly.
			switcher = True
			for i, b in enumerate(to_str):
				for j, a in enumerate(from_str):
					# If there are same elements waiting to be changed, ...
					if a == b:
						# ... the upper left value can be assigned directly.
						matrix[i+1, j+1] = matrix[i, j]
					else:
						# Otherwise, find the minimum value of the 2x2 unit.
						matrix[i+1, j+1] = np.min([matrix[i+0, j+1],
												   matrix[i+0, j+0],
												   matrix[i+1, j+0]]) + 1

					if i == j:
						# If the distance is far longer than our expectation, ...
						if matrix[i+1, i+1] > self.threshold:
							switcher = False
							# ... stop the calculation.
							break

				# The stop order should include the outer loop.
				if switcher is False:
					break

			# Save the result to an attribute.
			self.matrix = matrix

			# If the distance is still found out bigger than the threshold, ...
			if matrix[-1, -1] > self.threshold:
				# .. do this.
				return -1
			else:
				return matrix[-1, -1]

	def fit(self, alist, blist):
		# To return the scalable result, use this method.
		
		rows, cols = (len(alist), len(blist))
		records = np.tile([-1], rows * cols).reshape(rows, cols)

		# Compare each element with each others.
		for i, a in enumerate(alist):
			for j, b in enumerate(blist):
				dist = self.distance(a, b)
				if dist >= 0:
					records[i, j] = dist

		return records


########################################################################

if __name__ == '__main__':
	editing = Levenshtein(threshold=1)
	print(editing.distance('广东深圳南山', '广东深圳南山区'))
	# print(editing.matrix)

	# print(editing.distance(['this', 'is', 'sth', 'called', 'ML'],
	# 					   ['this', 'is.', 'sb', 'called', 'J']))
	# print(editing.matrix)
# 
	# print(editing.fit(['thealool','theiou','theyue','thisthis'],
					  # ['thea', 'this', 'thei', 'the']))

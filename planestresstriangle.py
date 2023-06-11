# Nicolò Grilli
# University of Bristol
# 11 Giugno 2023

# a plane stress triangle element
# Notation CPS3 used in Abaqus

import numpy as np

class PlainStressTriangle(ConstantStrainTriangle):
	
	def __init__(self,nodes,material):
		super().__init__(nodes,material)

	# calculate material stiffness matrix
	def calculate_D(self):
		self.D = np.zeros(shape=(3,3))
		self.D[0,0] = 1.0
		self.D[0,1] = self.poisson_ratio
		self.D[1,0] = self.poisson_ratio
		self.D[1,1] = 1.0
		self.D[2,2] = (1.0 - self.poisson_ratio) / 2.0
		self.D *= self.young_modulus / (1.0 - self.poisson_ratio * self.poisson_ratio)

	# calculate full element stiffness matrix
	def calculate_stiffness_matrix(self):
		DB = np.matmul(self.D, self.B)
		self.stiffness_matrix = self.area * np.matmul(np.transpose(self.B), DB)
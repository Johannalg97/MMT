from transfer_matrix_method import TransferMatrixMethod





def reflectance(transfer_matrix):
     a = transfer_matrix[1][0] / transfer_matrix[0][0] 
     reflectancia = abs(a)**2
     return reflectancia

def transmittance(transfer_matrix):
     a = 1 / transfer_matrix[0][0]
     transmittance = abs(a)**2
     return transmittance





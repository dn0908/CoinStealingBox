##############   MAIN CODE   ###############

# while cap_opened :
#     if coin detected :
#         if won > 500:
#             turn motor clockwise
#         else:
#             turn motor counter clockwise
#     else : --coin not detected
#         motor stop


from imports import *
 
from ProfessorBox import ProffesorBox

if __name__ == "__main__":
    Box = ProffesorBox()
    Box.run()
#Variant 27:
#VN={S, A, B},
#VT={a, b, c},
#P={
#   S → aA
#   A → bS
#   S → bB
#   A → cA
#   A → aB
#   B → aB
#   B → b
#}
class Grammar:
    def __init__ (self):
        self.VN = {'S', 'A', 'B'}
        self.VT = {'a', 'b', 'c'}
        self.P = {
            'S': ['aA','bB'],
            'B': ['aB', 'b'],
            'A': ['cA', 'aB', 'bS'],
        }
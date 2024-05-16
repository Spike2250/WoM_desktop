class MedicalUnit:
    def __init__(self, id_=None, tags=set(), data={}):
        self.id_ = id_
        self.tags = tags
        self.data = data

    def ___str__(self):
        pass


class ClinicalDiagnosis(MedicalUnit):
    def __init__(self, main=[],
                 concomitant=[],
                 scale={}, icf=[]):
        self.main = main
        self.concomitant = concomitant
        self.scale = scale
        self.icf = icf


class NosologicalUnit(MedicalUnit):
    def __init__(self, id_=None,
                 data={}, syndromes=[], mkb10=''):
        self.id = self.is_new(id_)
        self.data = data
        self.syndromes = syndromes
        self.mkb10 = mkb10

    def is_new(self, id_):
        if id_ is None:
            # генерация нового id
            pass
        return id_


class Syndrome(MedicalUnit):
    def __init__(self):
        super().__init__()



c = Syndrome()
print(c)
print(c.__dict__)
print(c.data)

b = Syndrome(id_=1235, tags=set(1, 5, 'гемиS'), data={'111': 'texttexttext'})
print(b.id_)
print(c.data)
print(b.tags)

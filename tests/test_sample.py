from classgen import ClassGenerator

class TestClass:

    def test_class_attributes(self):
        cg = ClassGenerator('student', ['m1', 'm2', 'm3'], ['m1', 'm2', 'm3'])
        assert cg.name == 'student'
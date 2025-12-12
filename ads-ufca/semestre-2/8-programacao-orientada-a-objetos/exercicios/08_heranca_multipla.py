class A:
    def falar(self):
        print('A.Falar')

class B:
    def falar(self):
        print('B.Falar')

class C(A,B):
    pass

c = C()
c.falar()


from ClassAModule import ClassA
from ClassBModule import ClassB
from ClassCModule import ClassC
from ClassDModule import ClassD

class Application:
    def run(self):
        # self.testAccess()
        self.testMultiInheritance()

    def testMultiInheritance(self):
        c1 = ClassC()
        print(f'C1 = {c1}')

        d1 = ClassD()       
        print(f'd1 = {d1}') 

        # c1.commonMethod()
        d1.commonMethod()


    def testAccess(self):
        a1 = ClassA()
        print(a1)
        a1.changeMembers()
        print(a1)
        a1.n1 = 5
        a1._n2 = 10
        # a1.__n3 = 15 # won't change __n3
        a1.setN3(15)
        print(a1)
        # print(f'n3 = {a1.__n3}') #error; can't access __n3 outside the class
        print(f'n3 = {a1.getN3()}')

        print(f'{ ("-" * 60)}')

        b1 = ClassB()
        print(b1)
        b1.changeNumber()
        print(b1)

        b2 = ClassB()
        print(b2)
        b2.k1 = 890
        b2._k2 = 982
        print(b2)

        print(f'{ ("-" * 60)} Shared members')
        ClassA.s_num = 9999
        print(f' A1 s_num = {ClassA.s_num}')
        print(f' sum = { ClassA.s_num + a1.n1 }')
        
        ClassA.changeStaticVariable()
        a2 = ClassA()
        print(f' A2 s_num = {ClassA.s_num}')


app = Application()
app.run()
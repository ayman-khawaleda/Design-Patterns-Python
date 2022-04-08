from CreationalPatterns.Singleton_MonoState.MonoState import CFO

def main():
    c1 = CFO()
    c1.name = 'Steven'
    c1.money_managed = 100
    print(c1)
    c2 = CFO()
    c2.name = 'John'
    c2.money_managed = 120
    print(c1,c2,sep='\n')
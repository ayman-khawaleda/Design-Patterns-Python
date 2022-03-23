from CreationalPatterns.Factory.FactoryMethod import PointFactory

def main():
    p1 = PointFactory.new_cartesian_point(20,10)
    p2 = PointFactory.new_polar_point(5,45)
    print(p1)
    print(p2)
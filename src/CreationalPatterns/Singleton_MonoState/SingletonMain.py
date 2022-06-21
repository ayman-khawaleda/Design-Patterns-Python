from .DB import DB
def main():
    d1 = DB(*[1,2,5])
    d2 = DB(*[2,5,6])
    d3 = DB(*[8,8,8,8])
    print(d1 == d2 == d3)
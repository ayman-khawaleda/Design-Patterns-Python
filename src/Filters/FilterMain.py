from turtle import color
from Filters.Types import Color,Size
from Filters.Specification import ColorSpecification,SizeSpecification,AndSpecification,OrSpecification
from Filters.Item import Item
from Filters.Filter import SingleSpecificationFilter

def main():
    house = Item('house',Color.WHITE,Size.LARGE)
    egg = Item('egg',Color.WHITE,Size.SMALL)
    table = Item('table',Color.RED,Size.MEDIUM)
    book = Item('book',Color.BLUE,Size.SMALL)

    color_spec = ColorSpecification(Color.WHITE)
    size_spec = SizeSpecification(Size.SMALL)

    ssfilter = SingleSpecificationFilter()
    print('\nFilter By Color:')
    for res in ssfilter.filter([house,egg,table,book],color_spec):
        print(res)
    
    print('\nFilter By Size:')
    for res in ssfilter.filter([house,egg,table,book],size_spec):
        print(res)
    
    print('\nFilter By Size And Color')
    white_small = AndSpecification(color_spec,size_spec)
    for res in ssfilter.filter([house,egg,table,book],white_small):
        print(res)

    print('\nFilter By Size OR Color')
    white_small = OrSpecification(color_spec,size_spec)
    for res in ssfilter.filter([house,egg,table,book],white_small):
        print(res)
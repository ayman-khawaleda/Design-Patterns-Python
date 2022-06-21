class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
def draw_point(p):
    print('.',end='')

class Line:
    def __init__(self,start_p,end_p):
        self.start = start_p
        self.end = end_p

class Rectangle(list):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.append(Line(Point(x,y),Point(x+width,y)))
        self.append(Line(Point(x+width,y),Point(x+width,y+height)))
        self.append(Line(Point(x,y),Point(x,y+height)))
        self.append(Line(Point(x,y+height),Point(x+width,y+height)))

def draw_rect(rcs):
    print("---- Drawing ---- \n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print('\n')

class LineToPointAdapter:
    cache = {}
    def __init__(self,line):
        super().__init__()
        self.h = hash(line)
        if self.h in self.cache:
            return

        print(f"Generating Points For Line"
                f"({line.start.x},{line.start.y})->({line.end.x},{line.end.y})"
        )
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y,line.end.y)
        bottom = max(line.start.y,line.end.y)

        points = []

        if right - left == 0:
            for y in range(top,bottom):
                points.append(Point(left,y))
        elif line.end.y - line.start.y:
            for x in range(left,right):
                points.append(Point(x,top))
        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h]) 
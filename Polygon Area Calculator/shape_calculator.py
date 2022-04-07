class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


    def set_width(self, swidth):
        self.width = swidth


    def set_height(self, sheight):
        self.height = sheight


    def get_area(self):
        return (self.width * self.height)


    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)


    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)


    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for row in range(self.height):
            picture += "*" * self.width + "\n"
        return picture


    def get_amount_inside(self, obj):
        return ((self.width // obj.width) * (self.height // obj.height))

class Square(Rectangle):    
    def __init__(self,num):
        super().__init__(num, num)


    def __str__(self):
        return f"Square(side={self.width})"


    def set_side(self, num):
        self.width = num
        self.height = num


    def set_height(self, num):
        self.set_side(num)

    
    def set_width(self, num):
        self.set_side(num)
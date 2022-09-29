from item import Item
class Phone(Item): 
        def __init__(self,name: str,price: float,quantity: int,brocken_phones=1):
         super().__init__( #inherits Attributes and  methods from the Item class
            name,price,quantity
         )
        
         self.brocken_phones = brocken_phones
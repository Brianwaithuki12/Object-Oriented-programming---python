import csv
from logging import raiseExceptions
class Item:

    pay_rate = 0.8 #The pay rate after 20% discount (class attribute)
    all = []
    def __init__(self,name: str,price: float,quantity: int): #the init function will run for each instance of the class item
       #Run validations to the received arguments
         assert price >= 0 , f"Price {price} is not greater than or equal to zero! "
         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
       #Assign to self object
       #instance attributes
         self.__name = name
         self.__price = price
         self.quantity = quantity # self.quantity is the defanation of the attribute  
        
        #actions to execute
         Item.all.append(self) 

    @property
    def price(self):
      return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increament(self,increament_value):
        self.__price = self.__price + self.__price * increament_value

    @property  #property decorator a read only attribute
    def name(self):
        return self.__name #double __ prevents access to those attributes .

    @name.setter #allow users to be able to  set a new value for name
    def name(self, value):
        if len(value) > 10: # >>>> encapsulation (restriction of access to attributes)
            raiseExceptions("the name is too long") #restricts user to set new value to more than 10 characters
        else:
          self.__name = value # the value will set the new name to the __name attribute

    def calculate_total_price(self):
        return self.__price * self.quantity

    

    @classmethod
    def instantiate_from_csv(cls):   #this method instantiates all the instances from the csv file.
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #imports as a dictionary and stores on the reader variable
            items = list(reader)#converts the reader variable to a string

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #count out the floats that are point zero
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False    
   
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    def __connect(self, smtp_server): # abstraction restricting accessibility    
      pass

    def __prepare_body(self):
       return    f"""
       Hello Someone.
       we have {self.name} {self.quantity} times.
       Regards , Brian
       """
    def __send(self):
      pass
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()   

    


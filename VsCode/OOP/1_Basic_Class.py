# OOP 
class User():
    def __init__(self,email):
        self.email =email

    def sign_in(self):
        print("Player logged in")

class PlayerCharacter(User):           # Inheritance Example
    # Class Object Attributes
    membership = True;
    def __init__(self,name,age,email):
        super.__init__(email)          # Super Method to call the parent constructor
        # User.__init__(self,email)    # Alternate way to use the Super Method
        self.name = name;    # Attributes
        self.age = age;

    def run(self):
        print("Run")

    @classmethod
    def adding_player(cls,age,name):
        return cls(name,age)

    @staticmethod
    def adding_numbers(num1,num2):
        return num1+num2;

        



player1 = PlayerCharacter("Rorona Zoro","24")
player2 = PlayerCharacter("Gaurav Kumar Thakur","21")
player1.weapon = "Sword";

print("Player 1 stats")
print("===============\n")
print(player1.name)
print(player1.age)
player1.run()
print(player1.weapon)

print("\nPlayer 2 stats")
print("===============\n")

print(player2.name)
print(player2.age)
player2.run()


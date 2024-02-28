import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

user_card_list = []
computer_card_list = []

for _ in range(2):
    user_card_list.append((random.choice(cards)))
    computer_card_list.append((random.choice(cards)))

def decision(user,comp):
  user_sum = sum(user)
  comp_sum = sum(comp)
  if user_sum == comp_sum :
      return "Its a Tie"  
  elif user_sum <=21 and comp_sum <= 21:
      result = "user win " if user_sum > comp_sum else "comp win"
      return result
  elif user_sum > 21 and comp_sum <= 21:
      print("Computer Wins")
  elif comp_sum > 21 and user_sum <= 21:
       return "user_Wins"
  elif user_sum > 21 and comp_sum > 21:
      final_sum_user = user_sum - 21
      final_sum_comp = comp_sum -21
      result = "user win " if final_sum_user < final_sum_comp else "comp win"
      return result

def blackjack(user,comp):
    print(logo)
    print(f"Your cards : {user}")
    print(f"Computer's first card : {comp[0]}")

    while True: 
        choice = input("Type \'y\' to get Hit, type \'n\' to Stand : ")
    
    
        if 'n' in choice:
            while sum(comp) < 17:
                comp.append(random.choice(cards))
            
            if sum(comp) > 21:
                return "Computer Bust , User Wins"
            return decision(user,comp)
        
        elif 'y' in choice:
            user.append(random.choice(cards))
        #   comp.append(random.randint(1,10))
            print(f"\nYour cards : {user}\n")
        if sum(user) > 21:
            return "User Bust , Computer Wins"
        # return decision(user,comp)
        else:
            print("Invalid Value!")
    
print("\n",blackjack(user_card_list,computer_card_list))
print("=======================================")
print(f"\nUser_Cards : {user_card_list} => {sum(user_card_list)} \nComputer_Cards : {computer_card_list} => {sum(computer_card_list)} \n")

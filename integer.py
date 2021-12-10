# Created by: Logan Sweeney
# Created on: Dec. 9, 2021
# This program asks for a number then says if it's a positive or negative number.

def main():

  user_input = float(input("Enter a character: "))
  
  def askAgain():
    user_answer = str(input("Would you like to put another character? "))
    
    if user_answer == "yes":
        print()
        main()
    elif user_answer == "no":
        print()
        print("Thanks for trying it out anyway!")
    else:
        print()
        print("Error. Try again?")
        askAgain()


  if user_input < 0:
        print()
        print("That is a negative Number!")
        print()
        askAgain()
  elif user_input > 0:
        print()
        print("This is a positive number.")
        print()
        askAgain()
  elif user_input == 0:
        print()
        print("That's just zero!")
        print()
        askAgain()



if __name__ == "__main__":
  main()
  
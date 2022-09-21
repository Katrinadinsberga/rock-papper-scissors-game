human_turn = input(" input human turn:")
computer_turn = input("input computer turn:")
 
if human_turn == "rock" and computer_turn == "scissors":
    print("Human wins!")
elif human_turn == "paper" and computer_turn == "rock":
    print("Human wins!")
elif human_turn == "scissors" and computer_turn == "paper":
    print("Human wins!")
else:
  print("computer wins")
if human_turn == computer_turn:
  print("draw!")
exit == print("thanks for playing!")   

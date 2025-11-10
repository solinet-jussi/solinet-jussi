# Course task: A7_T6 - Rock Paper Scissors

import random
random.seed(1234)

# ASCII art for choices
ROCK_ART = (
    "    _______\n"
    "---'   ____)\n"
    "      (_____)\n"
    "      (_____)\n"
    "      (____)\n"
    "---.__(___)"
)

PAPER_ART = (
    "     _______\n"
    "---'    ____)____\n"
    "           ______)\n"
    "          _______)\n"
    "         _______)\n"
    "---.__________)"
)

SCISSORS_ART = (
    "    _______\n"
    "---'   ____)____\n"
    "          ______)\n"
    "       __________)\n"
    "      (____)\n"
    "---.__(___)"
)

def getChoiceName(choice: int) -> str:
    """Convert choice number to name."""
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def getChoiceArt(choice: int) -> str:
    """Get ASCII art for choice."""
    if choice == 1:
        return ROCK_ART
    elif choice == 2:
        return PAPER_ART
    else:
        return SCISSORS_ART

def determineWinner(playerChoice: int, botChoice: int, playerName: str) -> str:
    """Determine winner and return result message."""
    playerNameLower = getChoiceName(playerChoice)
    
    if playerChoice == botChoice:
        return f"Draw! Both players chose {playerNameLower}."
    
    # Rock beats scissors
    if playerChoice == 1 and botChoice == 3:
        return f"{playerName} rock beats RPS-3PO scissors."
    if botChoice == 1 and playerChoice == 3:
        return f"RPS-3PO rock beats {playerName} scissors."
    
    # Paper beats rock
    if playerChoice == 2 and botChoice == 1:
        return f"{playerName} paper beats RPS-3PO rock."
    if botChoice == 2 and playerChoice == 1:
        return f"RPS-3PO paper beats {playerName} rock."
    
    # Scissors beat paper
    if playerChoice == 3 and botChoice == 2:
        return f"{playerName} scissors beats RPS-3PO paper."
    if botChoice == 3 and playerChoice == 2:
        return f"RPS-3PO scissors beats {playerName} paper."
    
    return ""

def playRound(playerName: str, playerChoice: int, playerWins: list[int], botWins: list[int], draws: list[int]) -> None:
    """Play a single round of RPS."""
    print("Rock! Paper! Scissors! Shoot!\n")
    
    # Get bot's choice
    botChoice = random.randint(1, 3)
    
    # Display player's choice
    print("#########################")
    print(f"{playerName} chose {getChoiceName(playerChoice)}.\n")
    print(getChoiceArt(playerChoice))
    print()
    
    # Display bot's choice
    print("#########################")
    print(f"RPS-3PO chose {getChoiceName(botChoice)}.\n")
    print(getChoiceArt(botChoice))
    print()
    print("#########################")
    print()
    
    # Determine winner
    result = determineWinner(playerChoice, botChoice, playerName)
    print(result)
    
    # Update scores
    if playerChoice == botChoice:
        draws[0] += 1
    elif (playerChoice == 1 and botChoice == 3) or \
         (playerChoice == 2 and botChoice == 1) or \
         (playerChoice == 3 and botChoice == 2):
        playerWins[0] += 1
    else:
        botWins[0] += 1
    
    return None

def main() -> None:
    # Initialize scores
    playerWins = [0]
    botWins = [0]
    draws = [0]
    
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    playerName = input("Insert player name: ")
    print(f"Welcome {playerName}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    print()
    
    # Game loop
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = input("Your choice: ")
        
        if choice == "0":
            break
        
        if choice in ["1", "2", "3"]:
            playerChoice = int(choice)
            playRound(playerName, playerChoice, playerWins, botWins, draws)
        else:
            print("Invalid choice. Please try again.")
            print()
    
    # Display results
    print()
    print("Results:")
    print(f"{playerName} - wins ({playerWins[0]}), losses ({botWins[0]}), draws ({draws[0]})")
    print(f"RPS-3PO - wins ({botWins[0]}), losses ({playerWins[0]}), draws ({draws[0]})")
    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()


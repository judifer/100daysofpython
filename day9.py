from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print("Welcome to the auction!\n")
# print(logo)

bids = dict()

def bidding():
    a = input("Please enter your full name.\n")
    b = float(input("Please enter the amount you want to bid.\n"))
    bids[a] = b
    c = input("Type 'yes' if another person wants to bid.\n").lower()
    if c == "yes":
        clear()
        return bidding()
    else:
        clear()
        print(logo)
        return winning()

def winning():
    winner = max(bids, key=bids.get)
    return f"The winner is {winner} with a bid of {'{:.2f}'.format(bids[winner])} €."

print(bidding())

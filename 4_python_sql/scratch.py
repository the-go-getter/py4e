'''
   Pradeepti Tandra
   CS5001 Fall 2020
   HW 1 - ATM
'''


def main():
    # obtaining input from user
    money = int(input("Welcome to PDQ Bank! How much to withdraw?: "))

    FIFTIES = money // 50
    TWENTIES = (money - (FIFTIES * 50)) // 20
    TENS = (money - ((FIFTIES * 50) + (TWENTIES * 20))) // 10
    FIVES = (money - ((FIFTIES * 50) + (TWENTIES * 20) + (TENS * 10))) // 5
    ONES = (money - ((FIFTIES * 50) + (TWENTIES * 20) + (TENS * 10) + (FIVES * 5)))

    print("Chaching!\n",
          "You asked for $", money,
          "\n That breaks down to:\n",
          FIFTIES, "fifties,\n",
          TWENTIES, "twenties,\n",
          TENS, "tens,\n",
          FIVES, "fives,\n",
          ONES, "ones")


if __name__ == "__main__":
    main()
class People:
    ambulatory = True
    sight = True

    def buy_ticket(self):
        print("Here the traveler checks or buys a subway ticket.")

    def enter_turnstile(self):
        print("Here the traveler enters the correct turnstile.")

    def wait(self):
        print("Here the traveler waits in the holding area.")

    def go_restroom(self):
        print("Here the traveler uses the correct restroom needed.")

    def PrintVariable(self):
        print(ambulatory)
        print(sight)

class Ticket_Kiosk:
    braille = True

    def buy_ticket(self):
        print("Here the traveler can buy a ticket.")

    def check_ticket(self):
        print("Here the traveler can check if the ticket is valid.")

    def PrintVariable(self):
        print(braille)

class Turnstile:
    accessible = True

    def Go_Through(self):
        print("Here the traveler can go through the right turnstile.")

    def Check_Ticket(self):
        print("Here the traveler runs their valid ticket.")

    def PrintVariable(self):
        print(accessible)

class Restroom:
    accessible = True
    parent = True
    companion = True

    def Go_Restroom(self):
        print("Here the traveler picks the right restroom stall.")

    def PrintVariable(self):
        print(accessible)
        print(parent)
        print(companion)

#Remember this method gets executed sinces its our 'main'
def main():
    Traveler = People()
    print(Traveler.sight)
    Traveler.buy_ticket()

    Ticket = Ticket_Kiosk()
    print(Ticket.braille)
    Ticket.buy_ticket()

    Entrance = Turnstile()
    print(Entrance.accessible)
    Entrance.Go_Through()

    Bathroom = Restroom()
    print(Bathroom.accessible)
    Bathroom.Go_Restroom()

if __name__ == "__main__":
    main()
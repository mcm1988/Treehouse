TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining:

    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    try:
        num_tickets = int(input("Hello {}. How many tickets would you like to purchase?  ".format(name)))
        if num_tickets > tickets_remaining:
            raise ValueError("{}. There are only {} tickets remaining!".format(name, tickets_remaining))
        if not num_tickets > 0:
            raise ValueError("Please enter a value that is more than 0")
    except ValueError as err:
        print("Sorry {} but an error occurred. Error:{}. Please try again.".format(name, err))
    else:
        price = calculate_price(num_tickets)
        print("Total cost of your tickets (Including £{} service charge): £{}.00".format(price, SERVICE_CHARGE))
        should_proceed = input("Do you want to proceed? Y/N  ")
        if should_proceed.upper() == "Y":
            # TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))

print("Sorry! We're sold out!!! :(")

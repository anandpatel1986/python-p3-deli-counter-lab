
def line(katz_deli):
    
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        message="The line is currently:"
        index = 1
        for person in katz_deli:
            message = message + f" {index}. {person}"
            index += 1
        print(message)

def take_a_number(katz_deli, name):
    print(f"Welcome, {name}. You are number {len(katz_deli)+1} in line.")
    katz_deli.append(name)
    
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
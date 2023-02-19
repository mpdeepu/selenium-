company= input("enter skill of an employee")
match company:
    case "quaityengineer":
        print("good at inspection and documentation.")
    case "purchaseengineer":
        print("good at material purchase")
    case _:
        print("not good at any kind of skill.") 

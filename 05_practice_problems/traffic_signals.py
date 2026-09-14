signal=input("enter a color:")
match signal:
    case 'red':
        print("Traffic Signal: Red -> Stop")
    case 'yellow':
        print("Traffic Signal: Yellow ->Get Ready")
    case 'green':
        print("Traffic Signal: Green ->Go")
    case _:
        print("Invalid Colors")
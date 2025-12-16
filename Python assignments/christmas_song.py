day = int(input("Enter day (1-12): "))
match day:
    case 12:
        print("Twelve drummers drumming,")
    case 11:
        print("Eleven pipers piping,")
    case 10:
        print("Ten lords a-leaping,")
    case 9:
        print("Nine ladies dancing,")
    case 8:
        print("Eight maids a-milking,")
    case 7:
        print("Seven swans a-swimming,")
    case 6:
        print("Six geese a-laying,")
    case 5:
        print("Five gold rings,")
    case 4:
        print("Four calling birds,")
    case 3:
        print("Three French hens,")
    case 2:
        print("Two turtle doves,")
    case 1:
        print("And a patridge in a pear tree. ")
    case _:
        print("Invalid day")


print("List of menu functions\n")

print( "Nokia Phone Menu")

print ("1.  Phone book\n2.  Messages\n3.  Chat\n4.  Call register\n5.  Tones")
print ("6.  Settings\n7.  Call divert\n8.  Games\n9.  Calculator\n10.  Reminders")
print ("11.  Clock\n12.  Profiles\n13.  SIM services")

option = int(input("\nEnter an option: "))

match (option):
    case 1:
        print("\nPhone book")
        print("1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags")
        phone_book_option = int(input("\nEnter an option: "))
        match (phone_book_option):
            case 8:
                print("\nOptions: ")
                print("1. Type of views\n2. Memory status")
    case 2:
        print("Messages")
        print ("1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10.Service command editor")
        messages_option = int(input("\nEnter an option: "))
        match (messages_option):
            case 7:
                print("1. Set\n2. Common")
                message_setting_option = int(input("Enter an option: "))
                match (message_setting_option):
                    case 1:
                        print("1. Message centre number\n2. Messages sent as\n3. Message validity")
                    case 2:
                        print("1. Delivery reports\n2. Reply via same centre\n3. Character support")
    
    case 3:
        print("Chat")

    case 4:
        print("Call register")
        print("1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit")
        call_register_option = int(input("Enter an option: "))
        match(call_register_option):
            case 5:
                print("1. Last call duration\n2. All calls’ duration\n3. Received calls’ duration\n4. Dialled calls’ duration\n5. Clear timers")

            case 6:
                print("1. Last call cost\n2. All calls’ cost\n3. Clear counters")
                
            case 7:
                print("1. Call cost limit\n2. Show costs in")

 















     
        







print("List of menu functions\n")


while True:
    print("""
    Main Menu
    1.Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10.Reminders
    11. Clock
    12. Profiles
    13. SIM services
    0. Exit
    """)

    option = int(input("Enter an option: "))

    match (option):
        case 1:
            while True:             
                print("""
                Phone book Menu
                1. Search
                2. Service Nos.
                3. Add name
                4. Erase
                5. Edit
                6. Assign tone
                7. Send b’card
                8. Options 
                9. Speed dials
                10. Voice tags                 
                0. Back
                """)
                pb_option = int(input("Enter an option: "))
                match(pb_option):   
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos.")
                    case 3:
                        print("Add name")
                    case 4:
                        print(" Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b’card")
                    case 8:
                        while True:
                            print("""
                            Options
                            1. Type of view
                            2. Memory status
                            0. Back
                            """)
                            op_option = int(input("Enter an option: "))
                            match(op_option):
                                case 1:
                                    print("Type of view")

                                case 2:
                                    print("Memory status")
                                case 0:
                                    break
                                case _:
                                    print("Invalid option")
                    case 9:
                        print("Speed dials")
                    case 10:
                        print("Voice tags")
                    case 0:
                        break  
                    case _:   
                        print("Invalid option")
                   
        case 2:
            while True:
                print("""
                Messages
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings
                8. Info service
                9. Voice mailbox number
                10.Service command editor
                0. Back
                """)
                me_option = int(input("Enter an option: "))
                match(me_option):
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        while True:
                            print("""
                            Messages settings
                            1.Set
                            2.Common
                            0.Back
                            """)
                            ms_option = int(input("Enter an option: "))
                            match(ms_option):
                                case 1:
                                    while True:
                                        print("""
                                        Set
                                        1. Message centre number
                                        2. Messages sent as
                                        3. Message validity
                                        0. Back
                                        """)
                                        se_option = int(input("Enter an option: "))
                                        match(se_option):
                                            case 1:
                                                print("Message centre number")
                                            case 2:
                                                print("Messages sent as")
                                            case 3:
                                                print("Message validity")
                                            case 0:
                                                break
                                            case _:
                                                print("Invalid option")
                                case 2:
                                    while True:
                                        print("""
                                        Common
                                        1. Delivery reports
                                        2. Reply via same centre
                                        3. Character support
                                        0. Back
                                        """)
                                        co_option = int(input("Enter an option: "))
                                        match(co_option):
                                            case 1:
                                                print("Delivery reports")
                                            case 2:
                                                print("Reply via same centre")
                                            case 3:
                                                print("Character support")
                                            case 0:
                                                break
                                            case _:
                                                print("Invalid option")
                    
                    case 8:
                        print("Info service")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
                    case 0:
                        break
                    case _:
                        print("Invalid option")
        case 3:
            print("Chat")
        case 4:
            while True:
                print("""
                Call register
                1. Missed calls
                2. Received calls
                3. Dialled numbers
                4. Erase recent call lists
                5. Show call duration
                6.Show call costs
                7.Call cost settings
                8.Prepaid credit
                0. Back
                """)
                cr_options = int(input("Enter an option: "))
                match(cr_options):                                   
                    case 1:
                        print("Missed calls")
                    case 2:
                        print("Received calls")
                    case 3:
                        print("Dialled numbers")
                    case 4:
                        print("Erase recent call lists")
                    case 5:
                        while True:
                            print("""
                            Show call duration
                            1.Last call duration
                            2.All calls’ duration
                            3. Received calls’ duration
                            4. Dialled calls’ duration
                            5. Clear timers  
                            0. Back                   
                            """)                       
                            cd_option = int(input("Enter an option: "))
                            match(cd_option):
                                case 1:
                                    print("Last call duration")  
                                case 2:
                                    print("All calls’ duration") 
                                case 3:
                                    print("Received calls’ duration")  
                                case 4:
                                    print("Dialled calls’ duration")                
                                case 5:
                                    print("Clear timers ")
                                case 0:         
                                    break
                                case _:
                                    print("Invalid option")
                    case 6:
                        while True:
                            print("""
                            Show call costs
                            1. Last call cost
                            2. All calls' cost
                            3. Clear counters
                            0. Back
                            """)
                            cc_option = int(input("Enter an option: "))
                            match(cc_option):
                                case 1:
                                    print("Last call cost")
                                case 2:
                                    print("All calls' cost")
                                case 3:
                                    print("Clear counters")
                                case 0:
                                    break
                                case _:
                                    print("Invalid option")

                    case 7:
                        while True:
                            print("""
                            Call cost settings
                            1. Call cost limit
                            2. Show costs in
                            0. Back
                            """)
                            ccs_option = int(input("Enter an option: "))
                            match(ccs_option):
                                case 1:
                                    print("Call cost limit")
                                case 2:
                                    print("Show costs in")

                                case 0:
                                    break
                                case _:
                                    print("Invalid option")

                    case 8:
                        print("Prepaid credit")  
                    case 0:
                        break
                    case _:
                        print("Invalid option")
             
        case 5:
            while True:
                print("""
                Tones
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                9. Screen saver
                0. Back
                """)

                tones_option = int(input("Enter an option: "))
                match(tones_option ):
                    case 1:
                        print("Ringing tone")
                    case 2:
                        print("Ringing volume")
                    case 3:
                        print("Incoming call alert")
                    case 4:
                        print("Composer")
                    case 5:
                        print("Message alert tone")
                    case 6:
                        print("Keypad tones")
                    case 7:
                        print("Warning and game tones")
                    case 8:
                        print("Vibrating alert")
                    case 9:
                        print("Screen saver")
                    case 0:
                        break
                    case _:
                        print("Invalid option")

        case 6:
            while True:
                print("""
                Settings
                1. Call settings
                2. Phone settings
                3. Security settings
                4. Restore factory settings
                0. Back
                """)
                settings_option = int(input("Enter an option: "))
                match(settings_option):
                    case 1:
                        while True:
                            print("""
                            Call settings
                            1. Automatic redial
                            2. Speed dialling
                            3. Call waiting options
                            4. Own number sending
                            5. Phone line in use
                            6. Automatic answer
                            0. Back
                            """)

                            call_settings_option = int(input("Enter an option: "))   
                            match(call_settings_option):
                                case 1:
                                    print("Automatic redial")
                                case 2:
                                    print("Speed dialling")
                                case 3:
                                    print("Call waiting options")
                                case 4:
                                    print("Own number sending")
                                case 5:
                                    print("Phone line in use")
                                case 6:
                                    print("Automatic answer")       
                                case 0 :
                                    break
                                case _:
                                    print("Invalid option")
                    case 2:
                        while True:
                            print("""
                            Phone settings
                            1. Language
                            2. Cell info display
                            3. Welcome note
                            4. Network selection
                            5. Lights
                            6. Confirm SIM service actions
                            0. Back
                            """)
                            phone_setting_option = int(input('Enter an option: '))
                            match(phone_setting_option):
                                case 1:
                                    print("Language")
                                case 2 :
                                    print("Cell info display")
                                case 3:
                                    print("Welcome note")
                                case 4:
                                    print("Network selection")
                                case 5:
                                    print("Lights")
                                case 6:
                                    print("Confirm SIM service actions")
                                case 0:
                                    break
                                case _:
                                    print("Invalid option")
                    case 3:
                        while True:
                            print("""
                            Security Setings
                            1. PIN code request
                            2. Call barring service
                            3. Fixed dialling
                            4. Closed user group
                            5. Phone security
                            6. Change access codes
                            0.Back
                            """)
                            security_option = int(input('Enter an option: '))
                            match(security_option):
                                case 1:
                                    print("PIN code request")
                                case 2:
                                    print("Call barring service")
                                case 3:
                                    print("Fixed dialling")
                                case 4:
                                    print("Closed user group")
                                case 5:
                                    print("Phone security")
                                case 6:
                                    print("Change access codes")
                                case 0:
                                    break
                                case _:
                                    print("Invalid option")
                    case 4:
                        print('Restore factory settings')
                    case 0:
                        break
                    case _:
                        print("Invalid option")
        case 7:
            print("Call divert")
        case 8:
            print("Games")
        case 9:
            print("Calculator")
        case 10:
            print("Reminders")
        case 11:
            while True:
                print("""
                Clock
                1. Alarm clock
                2. Clock settings
                3. Date setting
                4. Stopwatch
                5. Countdown timer
                6. Auto update of date and time
                0. Back
                """)
                
                clock_option = int(input("Enter an option: "))
                match(clock_option):
                    case 1:
                        print("Alarm clock")
                    case 2:
                        print("Clock settings")
                    case 3:
                        print("Date setting")
                    case 4:
                        print("Stopwatch")
                    case 5:
                        print("Countdown timer")
                    case 6:
                        print("Auto update of date and time")
                    case 0:
                        break
                    case _:
                        print("Invalid option")
        case 12:
            print("Profiles")
        case 13:
            print("SIM services")
        case 0:
            break
        case _:
            print("Invalid option")


                                                        
    


   






                










             
                          


                
            





                                                                                    
                                                





        
       

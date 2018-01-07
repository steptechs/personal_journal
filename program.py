def main():
    print_header()
    run_event_loop()


def print_header():
    print("-------------------------------")
    print("        JOURNAL APP")
    print("-------------------------------")


def run_event_loop():

    print("What do you want to do with your journal?")
    cmd = None

    while cmd != "X":
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        cmd = cmd.upper().strip()

        if cmd == "L":
            list_entries()
        elif cmd == "A":
            add_entry()
        elif cmd != "X":
            print("Sorry, we don't understand '{}'.".format(cmd))

    print("Done, goodbye.")


def list_entries():
    print("Listing...")


def add_entry():
    print("Adding...")


main()

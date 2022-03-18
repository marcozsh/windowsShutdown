import os
import sys

if len(sys.argv) < 3:
    print("\n [!] Bad call [!] \n")
    print("\n [*] usage: py shutdown.py -method (time to shutdown(sec)) [*] \n")
    print("\n [*] or [*] \n")
    print("\n [*] usage: py shutdown.py -method -minutes/hours (time to shutdown(min/hrs)) [*] \n")
    print("\n [!] help: -r 'restart' -s 'shutdown' [!]")
    print("\n [!] help: -m 'minutes' -h 'hours' [!]")
    print("\n [!] Example without second parameter: py shutdown.py -r 0 [!]")
    print("\n [!] Example with second parameter: py shutdown.py -r -h 3 [!]\n")
    sys.exit(-1)

def minutes_to_seconds(minutes):
    try:
        seconds = int(minutes)*60
    except:
        print("only integers")
        sys.exit(-1)
    return seconds

def hours_to_seconds(hours):
    try:
        seconds = int(hours)*3600
    except:
        print("only integers")
        sys.exit(-1)
    return seconds

def main(method, time, time_unit = ""):
    if method == "-r":
        if time_unit == "-h":
            os.system('shutdown /r /t {}'.format(hours_to_seconds(time)))
            print("restarting in {} hour".format(time))
        elif time_unit == "-m":
            os.system('shutdown /r /t {}'.format(minutes_to_seconds(time)))
            print("restarting in {} miuntes".format(time))
        elif time_unit == "":
            os.system('shutdown /r /t {}'.format(time))
            print("restarting in {} seconds".format(time))

    if method == "-s":
        if time_unit == "-h":
            os.system('shutdown /s /t {}'.format(hours_to_seconds(time)))
            print("shutdown in {} hour".format(time))
        elif time_unit == "-m":
            os.system('shutdown /s /t {}'.format(minutes_to_seconds(time)))
            print("shutdown in {} minutes".format(time))
        elif time_unit == "":
            os.system('shutdown /s /t {}'.format(time))
            print("shutdown in {} seconds".format(time))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.argv[1], sys.argv[3], sys.argv[2])

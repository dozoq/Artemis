import Artemis

def main():
    artemis = Artemis.Artemis("OPENAI_API_KEY","pl")
    artemis.Calibrate()
    artemis.WaitForCommand()
    print(f"Project Artemis: {'Initialized' if artemis.initialized else 'Not Initialized'}")



if __name__ == '__main__':
    main()

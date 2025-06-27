from Custum_messages import CustomMessages

def main():
    # Instantiate the logger
    CM = CustomMessages()
    # Write a test message
    CM.rtm("Test message")
    print("Test message logged to /artifacts/logs/CustomMessages.txt")

if __name__ == "__main__":
    main()
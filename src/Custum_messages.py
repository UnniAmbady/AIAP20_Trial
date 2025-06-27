# Custom Message to Track Progress during Train & Test Operations
import os
from datetime import datetime

class CustomMessages:
    def __init__(self):
        """
        Initialize the CustomMessages class.
        Ensures the directory for custom messages exists.
        """
        self.messages_dir = os.path.join("..", "Messages")
        os.makedirs(self.messages_dir, exist_ok=True)
    
    # Thank god..!! I discoverd this new technique today 7/12/2024 6PM......saves me too many dots  
    # I have not tested the side effects of making this as a static function
    # Sorry it failed miserably  
    # @staticmethod  
    def rtm(self, input_string):
        """
        rtm Stands for Run-Time Message
        Append the input string to a file with a timestamp.
        :param input_string: Message to be appended.
        """
        # File path for storing the custom message
        file_path = os.path.join(self.messages_dir, "Custummessage.txt")

        # Create a timestamp in the required format
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M")

        # Append the message with the timestamp to the file
        with open(file_path, "a") as file:
            file.write(f"{timestamp} - {input_string}\n")

        #print(f"Message appended to {file_path}")
        print("->>")
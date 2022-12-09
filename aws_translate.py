import boto3
import logging

#DateCreated: 12/4/2022
#THIS PROGRAM MAKES USE OF AWS TRANSLATE SERVICE TO TRANSLATE TEXT FROM ENGLISH TO FRENCH LANGUAGE.


client = boto3.client('translate')


# Set the log level in the basic configuration.  This means we will capture all our log entries and not just those at Warning or above.
logging.basicConfig(filename='log-aws-translate.log',level=logging.DEBUG)


#### Add the new text below this line ####

def translate_text(text, targetlang, sourcelang): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text=text, # Assigning the value of the string to the variable Text
        SourceLanguageCode=sourcelang, # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode=targetlang # We use a second two letter language code from the documentation (fr = French)
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response' 



if __name__ == "__main__":
    print("================================================")
    print("[X] Source Language: Default['EN']")
    print("================================================\n")
    text = str(input("Enter the Text you wish to Translate: "))
    targetlang = str(input("Enter your Target Language: "))
    sourcelang='en'
    # The if statement checks to see if the language code is the same as the source code
    if targetlang == sourcelang:
        logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping") # This will print to the console as the default level is warning
    else:
        logging.info("The Source Language and Target Language codes are different - proceeding") # This will not print to the console because it is lower than warning

    translate_text(text, targetlang, sourcelang) # This line will call our function. Without it, python will not do anything.
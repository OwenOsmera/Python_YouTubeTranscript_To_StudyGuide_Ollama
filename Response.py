"""
3/25/26
Response.py

"""

import ollama

DEFAULT_CONTEXT = """
    We need you a very smart IT specialist to create a detailed 
    study guide for specialist exams, using the infromation that 
    we provide.
    """

DEFAULT_MOD="phi3"

DEFUALT_FILE = "AI_file.txt"

# this function gets responses form the ai
def get_response_from_ollama(user_input, context=DEFAULT_CONTEXT, model=DEFAULT_MOD, filename= DEFUALT_FILE):
    # context for our purposes
    

    # get a response from the modle
    ollama.chat(model=model, messages=[{"role": "Computer", "content": context}])
    ai_response = ollama.chat(model=model, messages=[{"role": "user", "content": user_input}])

    # Checks if the AI gave the user output
    if 'message' in ai_response:

        # put the new infromation in a txt
        with open(filename, 'w') as f:
            f.write(ai_response['message']['content'])

        return "Success"
    else:
        return 'Sorry something went wrong.'
    
def main():
    # variables
    user_input = ""
    ai_response = ""
    model = "phi3"
    file_name="Working.txt"

    # loop for testing the ai
    while(True):


        # Get the user response
        user_input = input("Ask the AI [/bye to exit]: ")

        # See if the user wants to quit
        if user_input == "/bye":
            break

        # Run it through ollama and save the output
        ai_response = get_response_from_ollama(user_input, "teacher", model, file_name)

        # Return the output to the user
        print(ai_response)

        # print for space and split chats
        print()
        print("---------")
        print()


if __name__ == "__main__":
    main()
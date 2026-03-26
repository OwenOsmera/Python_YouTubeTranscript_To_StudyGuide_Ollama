"""
RunHere.py
3/26/26

"""

import PullURL
import Response
import transcript_1
import URL_ID

DEFAULT_CONTEXT = """
    We need you a very smart IT specialist to create a detailed 
    study guide for specialist exams, using the infromation that 
    we provide.
    """

DEFAULT_MOD="phi3"

def main():

    # use while to ask the user for multiple plalist links
    while(True):
        url_list = []
        id_list =[]

        try:
            # get the playlist url from the user
            user_url = input("Please enter the URL for the Playlist: ")

            # use the url with the pull url to get all video links
            url_list = PullURL.gen_link_list(user_url)

            # use the urls to get all ids
            for url in url_list:
                newitem = URL_ID.extract_video_id(url)
                id_list.append(newitem)

            # use the ids to generate txt files
            i=0
            file_names = []
            for item in id_list:
                print(item, url_list[i])
                name = transcript_1.gen_readable_file(item, url_list[i])
                file_names.append(name)
                i += 1

            # Check the file names and use the txt files as text for the ai
            for names in file_names:
                # opens the text file and makes its contents a string
                with open(names+".txt", "r") as file:
                    content = file.read()
                
                # put the text into ai
                Response.get_response_from_ollama(content, DEFAULT_CONTEXT, DEFAULT_MOD, "AI + "+names+".txt")


                file.close()

            # ask user to continue
            user_continue = input("Want to quit (y for yes): ")
            user_continue = user_continue.lower()

            if user_continue == "y":
                break

        except Exception as e:
            print("\nSomething went wrong Restarting \n" + e)

if __name__ == "__main__":
    main()


import string as str



def parse_email(f):
    """ Given an opened email file f, this function parse out all text
        below the metadata block (Message-ID, from, to, etc) at the top
        and return a string that contains all the words
        in the email text.
        """

    # Start at the beginning of the file and read ALL the text
    f.seek(0)
    all_text = f.read()

    # Everything above 'X-FileName is metadata, below is email text
    # This generates an array with 2 elements: content[0] = metadata
    # and content[1] = everything after 'X-FileName:'
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        # Remove punctuation from email text
        text_string = content[1].translate(content[1].maketrans("", "", str.punctuation))

        # Get words
        words = text_string
    return words



# def main():
#     ff = open("../data/test_email.txt", "r")
#     text = parse_email(ff)
#     print(text)
#
#
# if __name__ == '__main__':
#     main()
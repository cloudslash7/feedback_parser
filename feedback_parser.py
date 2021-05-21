import os
import requests

def parse_txt():
    labels = ("title", "name", "date", "feedback")
    all_feedback = []
    for f in os.listdir("./"):
        if f.endswith(".txt"):
            with open(f,"r") as open_file:
                i = 0
                feedback = {}
                for line in open_file:
                    line = line.strip()
                    try:
                        feedback[labels[i]] = line
                    except IndexError:
                        print("{} has more than four lines. Please fix formatting and try again.".format(open_file.name))
                        exit(1)
                    i += 1
                all_feedback.append(feedback)

    return all_feedback

def main():
    data = parse_txt()

if __name__ == "__main__":
    main()            

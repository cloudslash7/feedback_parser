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

def upload(data):
    for feedback in data:
        response = requests.post("http://<corpweb-external-IP>/feedback", json=feedback)
        print("{} completed with code - {}".format(response.request.body, response.status_code))

def main():
    data = parse_txt()
    upload(data)

if __name__ == "__main__":
    main()            

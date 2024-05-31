import ezgmail


def attachmentdownload(resulthreads):
    countofresults = len(resulthreads)
    try:
        for i in range(countofresults):
            if len(resulthreads[i].messages) > 1:
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[
                    j].downloadAllAttachments()
            else:
                resulthreads[i].messages[0].downloadAllAttachments()
        print("Download compelete. Please check your root directory.")
    except:
        raise Exception("Error occured while downloading attachments.")



if __name__ == '__main__':
    query = input(" Enter Search Query")
    newquery = query + " + has:attachment"
    resulthreads = ezgmail.search(newquery)

    if len(resulthreads) == 0:
        print("Result has no attachments:")
    else:
        print("Results with attachments:")
        for threads in resulthreads:
            print(f"Email Subject: {threads.messages[0].subject}")
            try:
                ask = input(
                    "Do you want to download attachments in results (Yes/No)?")
                if ask == "Yes":
                    attachmentdownload(resulthreads)
                else:
                    print("Program exited")
            except:
                print("Something went wrong")
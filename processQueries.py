import os
import WebPageIndex as wpi
import WebpagePriorityQueue as wppq

# I Can't figure out why my code doesn't run. Please help!!

def readFiles(folderpath):
    """
    Function to read the files of a folder path
    :param folderpath:
    :return:
    """
    directory = folderpath
    webpageindices = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            # Set up web page instances
            webpageindices.append(wpi.WebPageIndex(os.path.abspath(directory+"/"+filename)))
        else:
            continue
    return webpageindices

def startSearch():
    """
    Starter function to implement a search engine.
    :return:
    """
    print("-----------------Welcome to FOOGLE--------------------\n")
    path = input("Please enter a folder path of web pages to search from : ")
    queries = input("Please enter a file of queries to search: ")
    pages = readFiles(path)

    # Set up queue
    Queue = wppq.WebpagePriorityQueue(pages)
    with open(queries, "r") as file:

        # Search each query
        for query in file:
            stripped_query = query.strip()
            print("\nprocessing search for query... " + stripped_query)

            # Start by reheaping the queue
            Queue.reheap(query)
            # Find the highest priority
            rslt = Queue.peek()
            print("Search result: " + rslt)


if __name__ == "__main__":
    startSearch()

import requests
import threading

# A url that gives random images
url = 'https://picsum.photos/200'
# A function to download file
def download(
        NumOfFile: int = 1,  # number of files
        source: str = url,  # require a url
        name: str = "untitled"  # require a name
) -> None:
    response = requests.get(source)
    for i in range(NumOfFile - 1):
        with open(f"{name}{i}.jpg", "wb") as img:
            img.write(response.content)


if __name__ == '__main__':
    try:
        numsFile = int(input("Nums of File: "))
    except ValueError:
        print("Only Integers Allowed!")
    
    filename = input("Name of the files: ")
    th = threading.Thread(
        target=download,
        args=[numsFile, url, filename]
    )
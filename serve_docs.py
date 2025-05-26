import http.server
import os

def main():
    pwd = os.getcwd()
    try:
        os.chdir("./docs")
        http.server.test(http.server.SimpleHTTPRequestHandler)
    finally:
        os.chdir(pwd)

if __name__ == "__main__":
    main()

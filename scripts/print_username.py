import datetime
import getpass
import socket

def save_user_info_to_file(username, ip_address):
    try:
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('user_info.txt', 'a') as file:
            file.write(f"{current_datetime}|{username}|{ip_address}\n")
        print("User information saved to 'user_info.txt' successfully.")
    except Exception as e:
        print(f"Error saving user information: {str(e)}")

def main():
    try:
        # Get Windows username
        windows_username = getpass.getuser()

        # Get IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print(f"Current Date Time: {datetime.datetime.now()}")
        print(f"Windows Username: {windows_username}")
        print(f"IP Address: {ip_address}")

        # Save user information to a file
        save_user_info_to_file(windows_username, ip_address)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

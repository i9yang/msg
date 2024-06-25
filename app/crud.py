from imessage_reader import fetch_data

DB_PATH = "/Users/i9yang/Library/Messages/chat.db"

def get():
    fd = fetch_data.FetchData(DB_PATH)

    my_data = fd.get_messages()
    my_data = sorted(my_data, key=lambda data: data[2], reverse=True)
    return my_data[:5]

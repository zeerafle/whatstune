def read_current_obsession(file_path='current_obsession.txt'):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None


def write_current_obsession(track_title, file_path='current_obsession.txt'):
    with open(file_path, 'w') as f:
        f.write(track_title)

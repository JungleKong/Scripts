import zipfile
# import create_password


def extract_file(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        pass


def main():
    zip_file = zipfile.ZipFile('壁纸.zip')
    fp = open('passdict.txt', 'r')
    for password in fp.readlines():
        password = password.strip('\n')
        guess = extract_file(zip_file, password)
        if guess is not None:
            print(guess)
            break


if __name__ == '__main__':
    main()




def main():
    with open("code.txt",mode='r',encoding='utf8') as file:

        # use enumerate to show that second line is read as a whole
        lines = file.readlines();
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
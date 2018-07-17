import os
import re


class ReplaceWord:

    def __init__(self, list_dir, open_file , full_path):
        self.list_dir = list_dir
        self.open_file = open_file
        self.full_path = full_path


    def print_dir(self):
        print(os.listdir(self.list_dir))



    def open_doc(self):
       print(open(self.open_file).read(1000))
       open(self.open_file).read(1000)




    def change_word(self):

        file = "r" + open(self.open_file).read(1000)
        old_word_input = input("Enter word you want to change :")

        check_word = re.search(old_word_input, file)
        while not check_word:
            print(" { " + old_word_input + " } " + " does not Match any word. NOTE!!! your word needs to be Case sensitive")
            old_word_input = input("Enter word you want to change :")
            check_word = re.search(old_word_input, file)

        new_word_input = input("Enter new word : ")
        name_of_file = input("Enter the name of your file to be saved: ")

        pattern = old_word_input
        change_word = re.sub(pattern, new_word_input, file)
        print(change_word)

        # new file saved to desktop
        path_and_new_file = os.path.join(self.full_path, name_of_file + ".txt")
        # text color
        CSI = "\x1B["
        try:
            open(path_and_new_file, "w+").write(change_word)
            print(CSI + "31;40m" +"File Saved!!!!!==========================================="+ CSI + "0m")
            return True
        except Exception:
            print(CSI + "31;40m" + " File did'nt save!!!========="+ CSI + "0m")
            return False





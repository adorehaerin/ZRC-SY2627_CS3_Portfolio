class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")

class Book(Publication):
    def __init__(self, title, author, number_pages):
        Publication.__init__(self, title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if number_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = number_pages

    def display_info(self):
        Publication.display_info(self)
        print(f"Number of pages: {self.get_number_of_pages()}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        Publication.__init__(self, title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        Publication.display_info(self)
        print(f"Issue number: {self.get_issue_number()}")

pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
pub2 = Publication("A Brief History of Time", "Stephen Hawking")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Diary of a Wimpy Kid", "Jeff Kinney", 217)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Time Editors", 203)

print("Publication Information:")
pub1.display_info()

print("\nSecond Publication:")
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  #test invalid value
book1.display_info()

print("\nSecond Book:")
book2.display_info()

print("\nMagazine Information:")
mag1.set_issue_number(-202)  #test invalid value
mag1.display_info()

print("\nSecond Magazine:")
mag2.display_info()
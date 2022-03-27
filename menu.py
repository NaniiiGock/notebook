"""class menu. run the project"""

import sys
from notebook import Notebook
from note import Note

class Menu(object):
    def __init__(self):
        '''Initializes a menu'''
        self.notebook = Notebook()
        self.choices = {
            '1': self.display_notes,
            '2': self.search_notes,
            '3': self.add_new_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        '''Returns the choice'''
        print('''
    \t _______________________
    \t|     Notebook Menu     |
    \t|_______________________|  
    \t|    1. Display Notes   |
    \t|    2. Search Notes    |
    \t|    3. Add Note        | 
    \t|    4. Modify Note     |
    \t|    5. Quit            |
    \t|_______________________|             
        ''')
        return input('\tEnter a choice: ')
        
    def display_notes(self):
        for note in self.notebook.notes_list:
            print(f'\n\t{note}')
        
    def search_notes(self):
        '''Asks for a pattern.'''
        search_string = input('\n\tEnter the string to search for: ')
        matching_notes = self.notebook.search_notes(search_string)
        if len(matching_notes) == 0:
            print("sorry, but you haven't mached notes yes!")
            return
        print(f'\tThere are {len(matching_notes)} notes matching the string "{search_string}":')
        for note in matching_notes:
            print(f'\n\t{note}')

    def add_new_note(self):
        note_text = input('\n\tEnter the text for the note: ')
        note_tags = input('\tEnter tags for the note: ')
        self.notebook.add_new_note(note_text, note_tags)
        
    def modify_note(self):
        note_id = int(input('\n\tEnter a note id: '))
        try:
            print(f"current text: {self.notebook.get_note_text(note_id)}")
            print(f"current tag: {self.notebook.get_note_tags(note_id)}")
        except:
            print('sorry, you have not any notes with that id!')
            return
        note_text = input('\n\tEnter the text for the note: ')
        note_tags = input('\tEnter tags for the note: ')
        if note_text:
            self.notebook.replace_note_text(note_id, note_text)
        if note_tags:
            self.notebook.replace_note_tags(note_id, note_tags)

    def run(self):
        '''Display the menu and respond to choices'''
        while True:
            choice = self.display_menu()
            if choice in self.choices:
                action = self.choices[choice]
                print(f'\t-----{choice} is a valid choice-----')
                action()
            else:
                print(f'\t-----{choice} is not a valid choice-----')
            
    def quit(self):
        '''Exit from the notebook.'''
        print('\tGoodbye!')
        sys.exit(0)


if __name__ == '__main__':
    menu = Menu()   
    menu.run()

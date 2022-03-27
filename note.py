"""class Note"""

import datetime
available_id = 0

class Note(object):
    '''Represent a note in the notebook.'''

    def __init__(self, note_text, note_tags=''):
        '''Initialize a note, assign an id and creation date.'''
        global available_id
        self.note_text = note_text
        self.note_tags = note_tags
        self.note_id = available_id
        available_id += 1
        self.creation_date = datetime.date.today()
        return

    def contains(self, search_string):
        '''Determines if the note contains the search_string.'''
        return search_string in self.note_text or search_string in self.note_tags

    def __str__(self):
        return f'Note Id = {self.note_id}, Date = {self.creation_date},\
Text = {self.note_text}, Tags = {self.note_tags}'

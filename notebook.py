"""class Notebook"""

from note1 import Note

class Notebook(object):
    '''allows user to write into notebook'''
    def __init__(self):
        '''notebook with an empty list of notes'''
        self.notes_list = []
        
    def add_new_note(self, note_text, note_tags=''):
        '''Create a new note'''
        new_note = Note(note_text=note_text, note_tags=note_tags)
        self.notes_list.append(new_note)
        print(f'\tNote has been added. Id: {new_note.note_id}')
    
    def search_notes(self, search_string):
        '''Find notes by search string'''
        return [note for note in self.notes_list if note.contains(search_string)]

    def _find_note(self, note_id):
        '''Returns the note by id'''
        if type(note_id) == int and note_id<=len(self.notes_list):
            return self.notes_list[note_id]
        return None
    
    def get_note_text(self, note_id):
        '''Find note by id and return its text'''
        note = self._find_note(note_id)  
        return note.note_text
    
    def replace_note_text(self, note_id, note_text):
        '''Find note by id and replace its text'''
        note = self._find_note(note_id=note_id)  
        note.note_text = note_text
        
    def get_note_tags(self, note_id):
        '''Find note by id and return its text'''
        note = self._find_note(note_id=note_id)  
        return note.note_tags
    
    def replace_note_tags(self, note_id, note_tags):
        '''Find note by id and replace its tags'''
        note = self._find_note(note_id=note_id)  
        note.note_tags = note_tags
    
    def __str__(self):
        '''Print the notebook'''
        result = ''
        for note in self.notes_list:
            result += str(note)
            result += '\n'
        return result

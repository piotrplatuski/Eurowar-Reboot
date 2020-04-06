from Countries import France
from mimesis import Person
from mimesis.enums import Gender

person = Person(France['gen'])
person.full_name(gender=Gender.MALE)

"""
cs     da      de      de-at            de-ch         el     en       en-au               en-ca    
Czech  Danish  German  Austrian german  Swiss german  Greek  English  Australian English  Canadian English

en-gb            es       es-mx            et        fa     fi       fr      hu         is         it      
British English  Spanish  Mexican Spanish  Estonian  Farsi  Finnish  French  Hungarian  Icelandic  Italian                                        

ja        kk      ko      nl     nl-be          no         pl      pt          pt-br                                                       
Japanese  Kazakh  Korean  Dutch  Belgium Dutch  Norwegian  Polish  Portuguese  Brazilian Portuguese                                                                                             

ru       sv       tr       uk         zh                            
Russian  Swedish  Turkish  Ukrainian  Chinese                                                

"""

# Romania

Romanian_surnames = {'Popa', 'Popescu', 'Ionescu', 'Pop', 'Radu', 'Dumitru', 'Gheorghe', 'Stoica', 'Stan', 'Munteanu',
                     'Constantin', 'Andrei', 'Rusu', 'Anghel', 'Matei', 'Marin', 'Mihai', 'Ciobanu', 'Serban', 'Stefan',
                     'Lazar', 'Florea', 'Dumitrescu', 'Barbu', 'Stanciu', 'Vasile', 'Ilie', 'Cristea', 'Toma',
                     'Moldovan', 'Oprea', 'Dinu', 'Tudor', 'Ionita', 'Ion', 'Ungureanu', 'Constantinescu', 'Georgescu',
                     'Balan', 'Neagu', 'Dragomir', 'Badea', 'Cojocaru', 'Sandu', 'Mocanu', 'Enache', 'Nagy', 'Coman',
                     'Craciun', 'Lupu', 'Muresan', 'Vlad', 'Dobre', 'Tanase', 'Avram', 'Radulescu', 'Iordache',
                     'Grigore', 'Lungu', 'Ivan', 'Nicolae', 'Szabo', 'Bucur', 'Manea', 'Ene', 'Marinescu', 'Alexandru',
                     'Petre', 'Albu', 'Voicu', 'Preda', 'Iancu', 'Dragan', 'Olteanu', 'Stoian', 'David', 'Petrescu',
                     'Roman', 'Iacob', 'Filip', 'Diaconu', 'Costea', 'Baciu', 'Marcu', 'Rosu', 'Nistor', 'Kovacs',
                     'Pavel', 'Cretu', 'Stanescu', 'Anton', 'Simion', 'Luca', 'Nita', 'Calin', 'Rotaru', 'Nedelcu',
                     'Bogdan', 'Suciu', 'Crisan'}

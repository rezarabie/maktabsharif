import json

class notes:
 def displayNotes(self):
    with  open("noteBook.json","r") as nb:
        notes=json.load(nb)
        return(notes)

 def search(self,title):
        matchDicLoop=[]
        fetchNotes=self.displayNotes()
        for note in fetchNotes:
            if note["title"] in title:
                matchDicLoop.append(note)
                    
                return matchDicLoop

 def menu(self)->int:     
                print("1- add note..")
                print("2- see all notes..")
                print("3- search in notes..")
                print("4- delte notes .. ")
                print("5- exit..")
                menu_number=input()
                if(menu_number!=" "):
                    return (int(menu_number))
                else:
                    return 0
        
 def createNote(self,title,dates,content):
            note={"title":title,"dates":dates,"content":content}
            return (note)
 
 

while (True):
        dic_note={}
        list_notes=[]
        myNotes=notes()
        response=myNotes.menu()

        match response:
            case 1:
                title=input("plz input the title of notes")
                date=input("plz input the date of note")
                content=input("plz input your content")

                dic_note=myNotes.createNote(title,date,content)
                list_notes.append(dic_note)
                with  open("noteBook.json","a") as nb:
                    json.dump(list_notes,nb)
                    

            case 2:
                print (myNotes.displayNotes())
            case 3:
                searchValue=input("input your value to find ..")
                print(myNotes.search(searchValue))
                
            case 5:
                break
               



    
         
                
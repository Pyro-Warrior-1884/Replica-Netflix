
import random
class User_Node:
    def __init__(self,user_name,password,age):
        self.user_name = user_name
        self.password = password
        self.age = age
        self.Account = Entre(user_name, age)
        self.next = None
        
    def __str__(self):
        return self.user_name
        
class Users: 

    def __init__(self):
        self.head = None
        self.NumberOfAccounts = 0
        
    def new_user(self,user, pwd, age):
        new_user = User_Node(user, pwd, age)
        if self.head is None:
            self.head = new_user
            self.NumberOfAccounts += 1
            return
        present = self.head
        while present.next:
            present = present.next
        present.next = new_user
        self.NumberOfAccounts += 1
        return
    
    def search_user(self,search):
        if self.head is None:
            print("No Accounts Exist")
            return None
        
        present = self.head
        while present:
            if present.user_name == search:
                print("User has been found")
                
                while True:
                    passcode = input("Enter the Password: ")
                    if present.password == passcode:
                        print("Password Approved")
                        print()
                        return present
                    else:
                        print("Password Incorrect")
                        cont = input("Would You Like to Try Again(y/n): ")
                        if cont.upper() == 'N':
                            return None
            else:
                present = present.next
                        
        print("User Not Found")
        choice = input("Would You Like To Add New Account(y/n): ")
        if choice.upper() == 'Y':
            user = input("Enter User Name: ")
            pwd = input("Enter Password: ")
            age = int(input("Enter Age: "))
            self.new_user(user, pwd, age)
            print("New Account has Been Created")
            print()
            return None
        else:
            return None
        
    def delete_user(self):
        if self.head is None:
            print("No Acconts Exist")
            return
        username = input("Enter Username: ")
        Current_Account = self.head
        if self.head.user_name == username:
            present = self.head
            self.head = self.head.next
            present.next = None
            print("Account",username,"has been deleted")
            return
        Current_Account = self.head
        while Current_Account.next is not None:
            if Current_Account.next.user_name == username:
                break
            Current_Account = Current_Account.next
        if Current_Account.next is None:
            print("Account not Found")
            return
        else:
            print("Account",username,"has been deleted")
            Current_Account.next = Current_Account.next.next      
            return
        
    
    def PrintUsers(self):
        print()
        present = self.head
        while present:
            print(present.user_name,end=' ')
            present = present.next
        
class Media_Node:
    def __init__(self, media):
        self.Media = media
        self.Collection = []
        self.next = None
            
class Structure: 
    def __init__(self):
        self.head = None        
        
    def Insert(self, data):
        new_media = Media_Node(data)
        if self.head is None:
            self.head = new_media
            return 
        current_media = self.head
        while current_media.next:
            current_media = current_media.next
        current_media.next = new_media
        return
    
    def Display_Media(self):
        current_media = self.head
        while current_media:
            print(current_media.Media,end=' ')
            current_media = current_media.next
        print()
        return
    
    def Display_Content(self, media):
        print()
        current_media = self.head
        while current_media.Media != media and current_media:
            current_media = current_media.next
        for i in range(len(current_media.Collection)):
            print(current_media.Collection[i][1])        
        return 
    
    
    def Enter_Content(self, List, age):
        Store = []
        for i in range(len(List)):
            if List[i][0] not in Store:
                Store.append(List[i][0])
        
        for j in range(len(Store)):
            for i in range(len(List)):               
                if List[i][0] == Store[j] and age > List[i][4]:
                    current_media = self.head
                    while  current_media.next:
                        if current_media.Media == Store[j]:
                            break
                        current_media = current_media.next
                    current_media.Collection.append(List[i])
        return
    
    def Display_Specific_Content(self, media):
        current_media = self.head
        while current_media.next:
            if current_media.Media == media:
                break
            current_media = current_media.next
        
        Media_name = input("Enter the Media Name You Want to See: ")
        for i in range(len(current_media.Collection)):
            if current_media.Collection[i][1] == Media_name:
                print("The",current_media.Collection[i][0],current_media.Collection[i][1],"Released on",current_media.Collection[i][2],"and is available to watch in the Language",current_media.Collection[i][3],"\n")
                return
            
        print("Content not Found Please Write the Name Properly\n")
        return              

class Watch_List_Node:
    def __init__(self, content):
        self.prev = None
        self.Content = content
        self.next = None

class Watch_List: 
    def __init__(self, Storage):
        self.head = None
        self.Storage = Storage
        self.Size = 0
        
    def Insert_Content(self, content):
        for i in range(len(self.Storage)):
            if self.Storage[i][1] == content:
                self.Insert_Content_Node(content)
                print(content,"has been Added to The Watch List")
                return
        print("Content Not Found Please Re-Enter the Name Properly")
        return
    
    def Insert_Content_Node(self, content):
        WL_content = Watch_List_Node(content)
        if self.head is None:
            self.head = WL_content
            self.Size += 1
            return
        Present = self.head
        while Present.next:
            Present = Present.next 
        Present.next = WL_content
        WL_content.prev = Present
        self.Size += 1
        return
    
    def Display_Watch_List(self):
        Present = self.head
        while Present:
            print(Present.Content, end=' - ')
            Present = Present.next
        print()
        return
    
    def Display_Specific_Content(self, content):    
        Present = self.head
        while Present:
            if Present.Content == content:  
                
                for i in range(len(self.Storage)):
                    if self.Storage[i][1] == content:
                        print("The",self.Storage[i][0],self.Storage[i][1],"Released on",self.Storage[i][2],"and is available to watch in the Language",self.Storage[i][3],"\n")
                        return
                    
                print("Content not Found Please Write the Name Properly\n")
                return
            
            Present = Present.next
                        
        print("Content Not Present in Watch List Please ReWrite the Name")
        return 
    
    def Remove_Content(self, content):
        Present = self.head
        while Present:
            if Present.Content == content:
                if Present.prev:
                    Present.prev.next = Present.next
                else:
                    self.head = Present.next
                if Present.next:
                    Present.next.prev = Present.prev 
                else:
                    Present.prev.next = None
                print(content,"has been Removed From the Watch List")
                return            
            Present = Present.next
        print(content,"is not present in the Watch List")
        return          

class UserRecommendation: 
    def __init__(self):
        self.max_size = 5
        self.queue = [None] * self.max_size
        self.front = self.rear = -1
        
    def is_empty(self):
        return self.front == -1
        
    def Create_Random_CQ(self, Storage, age):
        List = []
        for i in range(len(Storage)):
            if Storage[i][4] <= age:
                List.append(Storage[i])
                
        AVG = []
        for i in range(5):
            num = random.randrange(len(List))
            while num in AVG:
                num = random.randrange(len(List))
            AVG.append(num)            
        
        for i in range(5):                       
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = List[AVG[i]]           
        return
    
    def Display_User_Recommendation(self):
        temp_front = self.front
        while temp_front != self.rear:
            print(self.queue[temp_front][1],end=" - ")
            temp_front = (temp_front + 1) % self.max_size
        print(self.queue[self.rear][1])
        return
     
class Search: 
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
            
    def __init__(self):            
        self.root = self.node()
            
    def Search_Level(self, content, age):
        v = self.root
        if v is None:
            return
        queue = [v]
        while queue:
            level_nodes = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.element[1].upper() == content.upper():
                    if node.element[4] > age:
                        print("\nYes", content, "is Available to Watch But You are not of Authorized Age to Watch it")
                        return
                    print("\nYes", content, "is Available to Watch")
                    print("\nThe", node.element[0], node.element[1], "Released on", node.element[2], "and is available to watch in the Language", node.element[3], "\n")
                    return                    
                
                if node.leftchild:
                    level_nodes.append(node.leftchild)
                if node.rightchild:
                    level_nodes.append(node.rightchild)
            
            queue.extend(level_nodes)
            
    def buildTree(self, eltlist):
        eltlist = [0] + eltlist
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[int(i/2)]
                        if (i % 2 == 0):
                            nodelist[int(i/2)].leftchild = tempnode
                        else:
                            nodelist[int(i/2)].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        return 

class Entre: #Albert
    def __init__(self,user_name, age):
        self.Storage = [["Movie", "Everything Everywhere All at Once", 2022, "English", 17]
                        ,["Movie", "Interstellar", 2014, "Engish", 13]
                        ,["Movie", "Leo", 2023, "Tamil",17]
                        ,["Movie", "C/O kancherakalam", 2018, "Telugu", 13]
                        ,["Movie", "Munjumunel Boys", 2024, "Malayalam", 0]
                        ,["Anime", "Fire Force", 2019, "English", 13]
                        ,["Anime", "Black Clover", 2019, "English", 13]
                        ,["Anime", "Jujutsu Kaisen", 2020, "Japanese", 17]
                        ,["Anime", "Naruto", 2002, "Japanese", 0]
                        ,["Anime", "Dragon Ball", 1989, "English", 0]
                        ,["Cartoon", "Adventure Time", 2010, "English", 0]
                        ,["Cartoon", "Steven Universe", 2013, "English", 0]
                        ,["Cartoon", "Avatar The Last Airbender", 2005, "English", 0]
                        ,["Cartoon", "Invincible", 2021, "English", 17]
                        ]
        self.Watchlist = Watch_List(self.Storage)       
        self.user_name = user_name        
        self.age = age
        self.User_Recommendation = UserRecommendation()
        self.Struct = Structure()
        
        
    def Create_Content_Structure(self):
        List = self.Storage
        Store = []
        for i in range(len(List)):
            if List[i][0] not in Store:
                Store.append(List[i][0])
        
        for i in range(len(Store)):
            self.Struct.Insert(Store[i])
        self.Struct.Enter_Content(self.Storage, self.age)        
        return       
        
    def Display_Content(self):
        self.Create_Content_Structure()
        
        while True:
            print("\n1. Movies \n2. Anime  \n3. Cartoon \n4. Search \n5. Watch List \n6. User Recommendation \n7. LogOut \n")
            Content_Choice = int(input("Enter Your Choice: "))
            if Content_Choice == 1:
                self.Struct.Display_Content("Movie")
                Suggestion = input("\nIs There Any Movie You Want Description on(y/n): ")
                while Suggestion.upper() == 'Y':
                    self.Struct.Display_Specific_Content("Movie")
                    Suggestion = input("\nIs There Any Movie You Want Description on(y/n): ")
                
                while True:
                    Watch_List_Entry = input("\nWould You Like to Add Some Movies To WatchList? Type the Name else Type None To Exit: ")
                    if Watch_List_Entry == "None":
                        print()
                        break
                    self.Watchlist.Insert_Content(Watch_List_Entry)
                
            elif Content_Choice == 2:
                self.Struct.Display_Content("Anime")
                Suggestion = input("\nIs There Any Anime You Want Description on(y/n): ")
                while Suggestion.upper() == 'Y':
                    self.Struct.Display_Specific_Content("Anime")
                    Suggestion = input("\nIs There Any Anime You Want Description on(y/n): ")
                
                while True:
                    Watch_List_Entry = input("\nWould You Like to Add Some Anime To WatchList? Type the Name else Type None To Exit: ")
                    if Watch_List_Entry == "None":
                        print()
                        break
                    self.Watchlist.Insert_Content(Watch_List_Entry)
                    
            elif Content_Choice == 3:
                self.Struct.Display_Content("Cartoon")
                Suggestion = input("\nIs There Any Cartoon You Want Description on(y/n): ")
                while Suggestion.upper() == 'Y':
                    self.Struct.Display_Specific_Content("Cartoon")
                    Suggestion = input("\nIs There Any Cartoon You Want Description on(y/n): ")
                                
                while True:
                    Watch_List_Entry = input("\nWould You Like to Add Some Cartoon To WatchList? Type the Name else Type None To Exit: ")
                    if Watch_List_Entry == "None":
                        print()
                        break
                    self.Watchlist.Insert_Content(Watch_List_Entry)
                    
            elif Content_Choice == 4:
                Content = input("Enter the Content Name: ")
                Find = Search()
                Find.buildTree(self.Storage)
                Find.Search_Level(Content, self.age)
                
            
            elif Content_Choice == 5:
                print("\nWatch List")
                self.Watchlist.Display_Watch_List()
                Interest = input("\nWould You Like a Description on any of the Contents(y/n): ")
                while Interest.upper() == 'Y':
                    content = input("\nPlease Enter the Name of the Interested Content: ")
                    self.Watchlist.Display_Specific_Content(content)
                    Interest = input("\nWould You Like a Description on any of the Contents(y/n): ")
                
                
                Remove = input("\nWould You Like to Remove Anything From Watch List(y/n): ")
                while Remove.upper() == 'Y':
                    content = input("\nPlease Enter the Name of the Content To be Removed: ")
                    self.Watchlist.Remove_Content(content)
                    self.Watchlist.Display_Watch_List()
                    Remove = input("\nWould You Like to Remove Anything From Watch List(y/n): ")             

                
            
            elif Content_Choice == 6:
                self.User_Recommendation.Create_Random_CQ(self.Storage, self.age)
                self.User_Recommendation.Display_User_Recommendation()
                choice = input("Do You Want To See Description of A Content(y/n): ")
                while choice.upper() == 'Y':
                    content = input("\nEnter the Content Name: ")
                    for i in range(len(self.Storage)):
                        if self.Storage[i][1] == content:
                            print("The",self.Storage[i][0],self.Storage[i][1],"Released on",self.Storage[i][2],"and is available to watch in the Language",self.Storage[i][3],"\n")
                    choice = input("Do You Want To See Description of A Content(y/n): ")
                
            elif Content_Choice == 7:
                print("Thank You", self.user_name)
                return 
            
            else:
                print("Invalid Choice Input")
                
            
User = Users()
User.new_user("Albert", "Albert123", 18)
User.new_user("Albi", "Albi123", 10)
 
while True:
    User.PrintUsers()
    Enter_Choice = int(input("\nWould you like to \n1. Log into Account \n2. Create New Account \n3. Delete an Account \n4. Exit \n: "))
    if Enter_Choice == 1:
        username = input("Enter Username: ")
        Account = User.search_user(username)
        if Account is not None:
            Account.Account.Display_Content()
            
    
    elif Enter_Choice == 2:
        user = input("Enter User Name: ")
        pwd = input("Enter Password: ")
        age = int(input("Enter Age: "))
        User.new_user(user, pwd, age)
        print("New Account Added")        
        
    elif Enter_Choice == 3:        
        User.delete_user()
        
    elif Enter_Choice == 4:
        print("Thank You")
        break
    
    else:
        print("Invalid Choice")
        


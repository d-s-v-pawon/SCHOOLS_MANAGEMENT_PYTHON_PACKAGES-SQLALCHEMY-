


#FUNCTIONS SHOULD ONLY USED WITH STUDENTS 




def read():
        class Invalidsubject(Exception):
            pass
        print(f"HI! {self.name} HAVE A GREAT READING SESSION")
        SUB=["TELUGU","HINDI","ENGLISH","MATHS","SCIENCE","SOCIAL"]
        SUBJECTS={"TELUGU":"యోగి వేమన, 17వ శతాబ్దంలో ప్రస్తుతం తెలుగు సాహిత్యంలో ఒక ప్రముఖ కవి-సేంట్‌పోయెట్‌. అతని పద్యాలు జీవితం, ప్రేమ, మరియు విశ్వాన్ని ప్రతినిధించే అంశాలను ప్రతిపాదిస్తాయి. అతని పద్యాలు సరళమైన భాషలో ఉంటాయి మరియు జీవితంలో అద్భుతమైన అంశాలను ప్రతిపాదిస్తాయి.",
                 "HINDI":'''प्रेमचंद, जिनका असली नाम मुंशी प्रेमचंद राय था, एक प्रमुख हिंदी कवि, उपन्यासकार, और समाजशास्त्री थे।उनके उपन्यास और कहानियाँ सामाजिक मुद्दों, जीवन की सच्चाई, और आध्यात्मिकता के मुद्दों पर आधारित थे।''',
                 "ENGLISH":"Elizabeth Alexander is an American poet, writer, and literary scholar. She has made significant contributions to both poetry and academia.",
                 "MATHS":"Calculus: The study of limits, derivatives, and integrals. It helps us understand rates of change and motion.",
                 "SCIENCE":'''Sulfur played a crucial role in the formation of Earth’s first water.Some deep-sea oxygen might be generated by metal-rich chunks on the seafloor.''',
                 "SOCIAL":''' Poverty persists worldwide, leading to unequal access to resources, education, and healthcare.Impact: Poverty perpetuates cycles of disadvantage and limits opportunities.'''}
        try:
            subject=input(f"ENTER THE SUBJECT {self.name} WANTS TO READ:")
            subject=subject.upper()
            if subject not in SUB:
                raise Invalidsubject
        except Invalidsubject:
            print("THE MAIN SUBJECTS NAMES ARE AS FOLLOWS")
            for i in SUB:
                if i!=SUB[len(SUB)-1]:
                    print(i,end=',')
                else:
                    print(i)
            while(True):
                subject=input(f"ENTER THE SUBJECT {self.name} WANTS TO READ IN THE ABOVE LIST:")
                subject=subject.upper()
                if subject in SUB:
                    self.subject=subject
                    break
            print(f"GOOD CHOICE! START READING THE {self.subject} SUBJECT")
            print(f"This is the content for {self.name} to read from the selected {self.subject} subject")
            print(SUBJECTS.get(self.subject))
            self.read_lines=SUBJECTS.get(self.subject)
        else:
            self.subject=subject
            print(f"GOOD CHOICE! START READING THE {self.subject} SUBJECT")
            print(f"This is the content for you to read of your selected {self.subject} subject")
            print(SUBJECTS.get(self.subject))
            self.read_lines=SUBJECTS.get(self.subject)
        finally:
            print("READING SESSION ENDED")

read()



def write(self):
    class Invalidcommand(Exception):
        pass
    class Invalidsubject(Exception):
        pass
    class notmatch(Exception):
        pass
    try:
        command=input("DO YOU WANT TO WRITE WHAT YOU HAVE READ(Y/N):")
        command=command.lower()
        if not re.match("^[y&n]",command):
            raise Invalidcommand
    except Invalidcommand:
        print("Error! Only letters Y AND N allowed!")
        print("PLEASE TRY AGAIN")
    else:
        self.command=command
        if(command=="n"):
            print(f"HI! {self.name} HAVE A GREAT WRITING SESSION")
            SUBJECTS={"TELUGU":"",
                      "HIINDI":"",
                      "ENGLISH":"",
                      "MATHS":"",
                      "SCIENCE":"",
                      "SOCIAL":""}
            try:
                subject=input("ENTER THE SUBJECT FOR WHICH YOU WANT TO WRITE THE NOTES:")                        
                subject=subject.upper()
                if subject not in SUBJECTS.keys():
                    raise Invalidsubject
            except Invalidsubject:
                 print("THE MAIN SUBJECTS NAMES ARE AS FOLLOWS")
                 print(SUBJECTS.keys())
                 while(True):
                     subject=input("ENTER THE SUBJECT FOR WHICH YOU WANT TO WRITE THE NOTES FROM THE ABOVE LIST:")                        
                     subject=subject.upper()
                     if subject in SUBJECTS.keys():
                         print(f"GOOD CHOICE! START WRITING THE {subject} SUBJECT")
                         SUBJECTS[subject]=input("WRITE WHAT YOU KNOW ABOUT THE SUBJECT:")
                         written_lines=SUBJECTS.get(subject)
                         print(f"THIS IS THE CONTENT YOU HAVE WRITTEN INTO THE {subject} SUBJECT NOTES")
                         print(f"{subject} : {written_lines}")
                         break                
            else:
                print(f"GOOD CHOICE! START WRITING THE {subject} SUBJECT")
                SUBJECTS[subject]=input("WRITE WHAT YOU KNOW ABOUT THE SUBJECT:")
                written_lines=SUBJECTS.get(subject)
                print(f"THIS IS THE CONTENT YOU HAVE WRITTEN INTO THE {subject} SUBJECT NOTES")
                print(f"{subject} : {written_lines}")
        else:
            print(f"HI! {self.name} HAVE A GREAT WRITING SESSION")
            try:
                self.written_lines=input("WRITE WHAT YOU HAVE READ:")
                if self.written_lines!=self.read_lines:
                    raise notmatch
            except notmatch:
                while(True):
                    print("NOT WRITTEN CORRECTLY")
                    command=input("DO YOU WANT TO WRITE AGAIN WHAT YOU HAVE READ(Y/N):")
                    command=command.lower()
                    if not re.match("^[y&n]",command):
                        print("Error! Only letters Y AND N allowed!")
                    else:
                        self.written_lines=input("WRITE AGAIN")
                        if self.written_lines==self.read_lines:
                            print("YOU ARE CORRECTLY WRITTEN WHAT YOU HAVE READ")
                            break
            else:
                print("YOU ARE CORRECTLY WRITTEN WHAT YOU HAVE READ")
    finally:
        print("WRITING SESSION ENDED")






def learn(self):
    class notwritten(Exception):
        pass
    try:
        if self.command!="y":
            raise notwritten
    except notwritten:
        print("PLEASE,WRITE THE READ CONTENT FIRST")
    else:
        if self.written_lines==self.read_lines:
            print(f"YOU HAVE SUCCESSFULLY LEARNT THE CONTENT IN THE SUBJECT {self.subject}")
        else:
            print(f"STILL YOU HAVE TO WORK HARD ON THIS {self.subject} SUBJECT")
    finally:
        print("LEARNING SESSION ENDED")






def play(self):
    play={"1":'04',
          "2":'05',
          "3":'02',
          "4":'07',
          "5":'08',
          "6":'10',
          "7":'06',
          "8":'03',
          "9":'09',
          "10":"NONE"}
    GAMES=["BADMINTON","BASKETBALL","CYCLING","TENNIS","CRICKET","CHESS","KABADDI","VOLLEYBALL","SWIMMING","KHOKHO"]
    if str(self.standard) in play.keys():
        print(f"THE GAMES PERIOD FOR CLASS {self.standard} STUDENT IS {play.get(str(self.standard))}")
    else:
        print("WRONG CLASS")
    if self.standard!=10:
        print(f"THESE ARE THE GAMES PLAYED BY THE STUDENTS IN THE SCHOOL")
        print(*GAMES,sep=",")
        T_GAME=random.choice(GAMES)
        print(f"NOW THE GAME PLAYED BY THE STUDENT {self.name} IN RANDOM CHOICE BY THE PET TEACHER IS {T_GAME}")




#FUNCTIONS SHOULD ONLY USED WITHIN STANDARDS

def SECT_STU(self):
    self.SECTS={}
    for i in self.CLASS:
        if i.section in self.SECTS.keys():
            self.SECTS[i.section].append(i)
        else:
            SECT_NAME=f"{i.section}"
            self.SECTS[SECT_NAME]=[]
            self.SECTS[i.section].append(i)
    for j in self.SECTS.keys():
        if self.SECTS[j]==[]:
            pass
        else:
            print(f"CLASS {self.name} SECTION_{j} STUDENTS ARE:")
            for k in self.SECTS[j]:
                print(f"{k.name}")





def GENDER(self):
    for i in self.SECTS.keys():         
        G1=[]
        G2=[]
        for j in self.SECTS.get(i):
            if j.gender=='MALE':
                G1.append(j)
            if j.gender=='FEMALE':
                G2.append(j)
        self.SECTS[i]=[]
        self.SECTS[i].append(G1)
        self.SECTS[i].append(G2)
        print()
        print(f"MALE STUDENTS OF CLASS {self.name} AND SECTION_{i} ARE AS FOLLOWS:")
        for k in self.SECTS[i][0]:
            print(k.name,k.gender)
        print()
        print(f"FEMALE STUDENTS OF CLASS {self.name} AND SECTION_{i} ARE AS FOLLOWS:")
        for k in self.SECTS[i][1]:
            print(k.name,k.gender)
        print()
        print()






def CLASSROOM(self):
    print("THE MALE STUDENTS SITS ON THE RIGHT SIDE BENCHES IN THE CLASSROOM")
    print("THE FEMALE STUDENTS SITS ON THE LEFT SIDE BENCHES IN THE CLASSROOM")
    RIGHT=[]
    LEFT=[]
    for i in self.SECTS.keys():
        for k in self.SECTS[i][0]:
            RIGHT.append(k)
        for k in self.SECTS[i][1]:
            LEFT.append(k)
    print(f"IT MEANS THE STUDENTS ON THE RIGHT BENCHES IN CLASS {self.name} ARE AS FOLLOWS:")
    for j in RIGHT:
        print(j.name,end=' ')
    print()
    print(f"THE STUDENTS ON THE LEFT BENCHES IN CLASS {self.name} ARE AS FOLLOWS:")
    for j in LEFT:
        print(j.name,end=' ')
    print()






def SUBJECTS(self):
    if self.name<=5:
        print("THE SUBJECTS FOR PRIMARY STUDENTS ARE")
        print("TELUGU","HINDI","ENGLISH","MATHS","EVS",sep=',')
    elif(self.name<=7):
        print("THE SUBJECTS FOR UPPER PRIMARY STUDENTS ARE")
        print("TELUGU","HINDI","ENGLISH","MATHS","SCIENCE","SOCIAL",sep=',')
    else:
        print("THE SUBJECTS FOR HIGHER CLASS STUDENTS ARE")
        print("TELUGU","HINDI","ENGLISH","MATHS","SCIENCE","SOCIAL",sep=",")
        print("HERE SCIENCE IS CLASSIFIED INTO TWO PARTS")
        print("SCIENCE=",["PHYSICAL SCIENCE","BIOLOGICAL SCIENCE"])
        print("PHYSICAL SCIECNE=",["PHYSICS","CHEMISTRY"])







#FUNCTIONS SHOULD ONLY USED FOR SCHOOLS

def promotion_status(self,stu_name):
    self.stu_name=stu_name.upper()
    for i in self.CY_SCHOOL:
        for j in i[1]:
            if self.stu_name==j.name:
                for k in self.NY_SCHOOL:
                    for l in k[1]:
                        if self.stu_name==l.name and l.standard==j.standard+1:
                            print(f'YES!THE STUDENT {self.stu_name} IS PROMOTED FROM THE CLASS {j.standard} TO THE NEXT CLASS {l.standard}')






def STU_TRANSFERS(self,stu_name):
    self.stu_name=stu_name.upper()
    print(f"THE STUDENT {self.stu_name} IS APPLIED FOR TRANSFER FROM THE SCHOOL {self.sch_name}")
    for i in self.NY_SCHOOL:
        for j in i[1]:
            if j.name==self.stu_name:
                i[1].remove(j)
                print(f"THE STUDENT IS TRANSFERRED SUCCESSFULLY FROM THE SCHOOL {self.sch_name}")
                break
            else:
                pass
    for i in self.NY_SCHOOL:
        if i[1][0].standard>self.no_stands:            
            print(f"THE STUDETNS WHO COMPLETED THEIR SCHOOL EDUCATION IN THE {self.sch_name} ARE AS FOLLOWS")
            for j in i[1]:
                print(j.name)
            self.NY_SCHOOL.remove(i)
            break
    print()
    print(f"THE ABOVE ALL STUDENTS CAN JOIN IN COLLEGES WITHOUT ANY FAIL")
    print(f"THESE STUDENTS ARE SUCCESFULLY TRANSFERRED FROM THE SCHOOL")
    print(f"THE NEXT YEAR INFO OF THE {self.sch_name} SCHOOL AFTER STUDENT TRANSFERS IS AS FOLLOWS")
    N_SCHOOL=[]
    for i in self.NY_SCHOOL:
        CLASS=[f"CLASS_{i[0]}",[],[]]
        for j in i[1]:
            CLASS[1].append(j.name)
            CLASS[2].append(j.percent)
        N_SCHOOL.append(CLASS)
    head=["CLASS NAME","STUDENTS","PERCENTAGES"]
    print(tabulate(N_SCHOOL,headers=head,tablefmt="rounded_grid"))






def NEW_ADMISSIONS(self,name,gender,age,sch_name,standard,section,r_no,c_no,percent):
    n_stu=STUDENTS(name,gender,age,sch_name,standard,section,r_no,c_no,percent)
    n_stu.stu_details()
    st_list=[]
    for i in self.NY_SCHOOL:
        st_list.append(i[1][0].standard)
    if n_stu.standard+1 in st_list:
        if n_stu.percent>60:
            for i in self.NY_SCHOOL:
                if i[0]==f"CLASS_{n_stu.standard+1}":                
                    i[1].append(n_stu)
                    print(f"THE STUDENT IS SUCCESSFULLY ADMITTED INTO THE CLASS {n_stu.standard+1} IN THE SCHOOL")
                    break
        else:
            print(f"THE STUDENT ANNUAL YEAR PERCENTAGE OF THE CLASS {n_stu.standard} IS VERY POOR(LESS THAN 60),HE WON'T BE ADMITTED INTO THE NEXT CLASS {n_stu.standard+1} DIRECTLY")
            command=input("DO YOU WANT HIS/HER ADMISSION INTO THEIR SAME CLASS(Y/N):")
            command=command.lower()
            if not re.match("^[y&n]",command):
                print("Error! Only letters Y AND N allowed!")
                print("PLEASE TRY AGAIN")
            else:
                if command=='y':
                    for i in self.NY_SCHOOL:
                        if i[0]==f"CLASS_{n_stu.standard}":                
                            i[1].append(n_stu)
                            print(f"THE STUDENT IS SUCCESSFULLY ADMITTED INTO THE CLASS {n_stu.standard} IN THE SCHOOL")
                            break
                else:
                    print("THANK YOU,BETTER LUCK NEXT TIME")
    else:
        if n_stu.percent>60:
            CLASS=[f"CLASS_{n_stu.standard+1}"]
            STU=[]
            STU.append(n_stu)
            CLASS.append(STU)
            for i in st_list:
                if i-1==n_stu.standard+1:
                    self.NY_SCHOOL.insert(0,CLASS)
                    break
                elif i+1==n_stu.standard+1:                    
                    INDEX=st_list.index(i)
                    self.NY_SCHOOL.insert(INDEX+1,CLASS)
                    break
                elif i+1 not in st_list:
                    INDEX=st_list.index(i)
                    self.NY_SCHOOL.insert(INDEX+1,CLASS)
                    break
                elif i<n_stu.standard+1 and i+2>n_stu.standard+1:
                    INDEX=st_list.index(i)
                    self.NY_SCHOOL.insert(INDEX+1,CLASS)
                    break
        else:
            print(f"THE STUDENT ANNUAL YEAR PERCENTAGE OF THE CLASS {n_stu.standard} IS VERY POOR(LESS THAN 60),HE WON'T BE ADMITTED INTO THE NEXT CLASS {n_stu.standard+1} DIRECTLY")
            command=input("DO YOU WANT HIS/HER ADMISSION INTO THEIR SAME CLASS(Y/N):")
            command=command.lower()
            if not re.match("^[y&n]",command):
                print("Error! Only letters Y AND N allowed!")
                print("PLEASE TRY AGAIN")
            else:
                if command=='y':
                    CLASS=[f"CLASS_{n_stu.standard}"]
                    STU=[]
                    STU.append(n_stu)
                    CLASS.append(STU)
                    for i in st_list:
                        if i-1==n_stu.standard:
                            self.NY_SCHOOL.insert(0,CLASS)
                            break
                        elif i+1==n_stu.standard:                    
                            INDEX=st_list.index(i)
                            self.NY_SCHOOL.insert(INDEX+1,CLASS)
                            break
                        elif i+1 not in st_list:
                            INDEX=st_list.index(i)
                            self.NY_SCHOOL.insert(INDEX+1,CLASS)
                            break
                        elif i<n_stu.standard and i+2>n_stu.standard:
                            INDEX=st_list.index(i)
                            self.NY_SCHOOL.insert(INDEX+1,CLASS)
                            break
                else:
                    print("THANK YOU,BETTER LUCK NEXT TIME")
    print(f"THE NEXT YEAR INFO OF THE {self.sch_name} SCHOOL AFTER NEW ADMISSIONS IS AS FOLLOWS")
    N_SCHOOL=[]
    for i in self.NY_SCHOOL:
        CLASS=[f"CLASS_{i[0]}",[],[]]
        for j in i[1]:
            CLASS[1].append(j.name)
            CLASS[2].append(j.percent)
        N_SCHOOL.append(CLASS)
    head=["CLASS NAME","STUDENTS","PERCENTAGES"]
    print(tabulate(N_SCHOOL,headers=head,tablefmt="rounded_grid"))








def FEE(self,stu_name):
    self.stu_name=stu_name.upper()
    for i in self.NY_SCHOOL:
        for j in i[1]:
            if j.name==self.stu_name:
                fee=j.standard*5000
                print(f'THE FEE OF {self.stu_name} FOR THE NEXT YEAR FOR THE CLASS {j.standard} is {fee}')
                break






def t_removals(self):
    TEACHERS=[['PRASAD','TELUGU',8],['RAMANA','HINDI',7],['SRINIVAS','ENGLISH',6],['MADHU','MATHS',8],['RASHIDA','PHYSICS',8],['RAJU','CHEMISTRY',5],['AHMAD','SOCIAL',8],['ARJUN','BIOLOGY',6],['PARVATHI','PET',8],['SARASWATHI','SANSKRIT',8]]
    self.N_TEACHERS=[]
    for i in TEACHERS:
        if i[2]>=7:
            self.N_TEACHERS.append(i)
    print('THE STAFF REMOVED FROM THE SCHOOL ARE')
    for i in TEACHERS:
        if i[2]<7:
            print(i[0],end=',')







def t_appoint(self,name,subject,t_points):
    self.name=name.upper()
    self.subject=subject.upper()
    self.t_points=t_points
    if self.t_points>=7:
        self.N_TEACHERS.append([self.name,self.subject,self.t_points])
    else:
        print("SORRY!BETTER LUCK MEXT TIME")
        print('THE STAFF LIST AFTER NEW APPOINTMENTS')
        print(self.N_TEACHERS)
    
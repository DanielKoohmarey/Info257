import httplib2
import MySQLdb
from scrapy.selector import Selector

h = httplib2.Http()
conn = MySQLdb.connect(host="localhost", user="root", passwd="berkeley", db="testcompsci")
cursor = conn.cursor()
tutor_page = h.request("https://hkn.eecs.berkeley.edu/tutor", "GET")[1]
sel = Selector(text=tutor_page)
cory_table, soda_table = sel.xpath("//table[@id='cory_schedule']")
tutors_classes = {}
for row in cory_table.xpath("tr")[1:]:
    time = row.xpath("td/text()")[0].extract()
    days = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday']
    tutors = [ x.extract() for x in row.xpath("td/div/@title")]
    classes = [ x.extract().lstrip("person ") for x in row.xpath("td/div[1]/@class")]
    for i in range(5):
        tutor = tutors[i]
        day = days[i]
        if tutor not in tutors_classes:
            tutor_skills = [ ele[:len(ele)-2] for ele in classes[i].split('\n') if ele]
            tutors_classes[tutor] = ','.join(tutor_skills)
        try:
            cursor.execute("""INSERT INTO Tutors ( Person_Name, Course_Codes, Day, Time, Building_Name, Room_No )  
                                               VALUES ("{}","{}","{}","{}","{}","{}")""".format( 
                                               tutor, tutors_classes[tutor],  day,time,
                                               'Cory',
                                               '290',
                                                )
                                           )
            conn.commit()
        except:
            pass
for row in soda_table.xpath("tr")[1:]:
    time = row.xpath("td/text()")[0].extract()
    days = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday']
    tutors = [ x.extract() for x in row.xpath("td/div/@title")]
    classes = [ x.extract().lstrip("person ") for x in row.xpath("td/div[1]/@class")]
    for i in range(5):
        tutor = tutors[i]
        day = days[i]
        if tutor not in tutors_classes:
            tutor_skills = [ ele[:len(ele)-2] for ele in classes[i].split('\n') if ele]
            tutors_classes[tutor] = ','.join(tutor_skills)
        try:
            cursor.execute("""INSERT INTO Tutors ( Person_Name, Course_Codes, Day, Time, Building_Name, Room_No )  
                                               VALUES ("{}","{}","{}","{}","{}","{}")""".format( 
                                               tutor,tutors_classes[tutor],days[i],time,
                                               'Soda',
                                               '345',
                                                )
                                           )
            conn.commit()
        except:
            pass

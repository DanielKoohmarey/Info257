import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MySQLCoursePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd="berkeley", db="testcompsci")
        self.cursor = self.conn.cursor()
        self.buildings = set()
        self.professors = set()
    def process_item(self, item, spider):    
        try:
            for key, value in item.items():
                if not value:
                    item[key] = None
            self.cursor.execute("""INSERT INTO Courses (CCN, Course_Code, Course_Title, Section_No, Description, Time, Room_No,           
                                    Building_Name, Course_Type, Units, Exam) VALUES ({}, "{}", "{}", {}, "{}", "{}", "{}", "{}", 
                               "{}", "{}", "{}")""".format(
                               item['ccn'],
                               item['course_code'],
                               item['course_title'], 
                               item['section_no'],
                               item['description'], 
                               item['time'],
                               item['room_no'], 
                               item['building_name'], 
                               item['course_type'],
                               item['units'],  
                               item['exam'])
                               )
            if False:            
                if item['assistant_name'] and item['ccn']:
                    self.cursor.execute("""INSERT INTO Assistants ( Person_Name, CCN )  
                                       VALUES ("{}",{})""".format( 
                                       item['assistant_name'],
                                       item['ccn'])
                                        )
                if 'professor_name' in item and item['professor_name']:
                    professor = item['professor_name'][0]
                    link = item['professor_link']
                    offset = 0     
                    if link and (professor not in self.professors):
                        self.cursor.execute("""INSERT INTO Professors ( Professor_Name, CCN, Homepage )  
                                           VALUES ("{}",{},"{}")""".format( 
                                           professor,
                                           item['ccn'],
                                           link)
                                       )
                        offset = 1
                    for professor in item['professor_name'][offset:]: 
                        if professor in self.professors:
                            continue       
                        self.cursor.execute("""INSERT INTO Professors ( Professor_Name, CCN )  
                                           VALUES ("{}",{})""".format( 
                                           professor,
                                           item['ccn'])
                                       )
                    for professor in item['professor_name']:
                        self.professors.add(professor)
                if item['building_name'] not in self.buildings:            
                    self.cursor.execute("""INSERT INTO Buildings ( Building_Name )  
                                       VALUES ("{}")""".format( 
                                       item['building_name'])
                                        )
                    self.buildings.add(item['building_name'])
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

import MySQLdb
from urllib import urlopen
import re

"""
The function extracts the names of the HKN officers
from the HKN website https://hkn.eecs.berkeley.edu/about/officers/.
"""
def HKN_tutor_parsing():
  # the regular expression to search for
  # example: <span class="name">Zeyu Liu</span>
  SPAN_NAME = '<span class="name">([a-zA-Z ]*)</span>'

  url = "https://hkn.eecs.berkeley.edu/about/officers/"   
  html = urlopen(url).read()    

  names = []
  for line in html.splitlines():
    m = re.search(SPAN_NAME, line)
    if (m != None):
      names.append(m.group(1))

  return names

"""
The function updates the "officer" attribute of the "Assistants" database.
It sets the "officer" attribute to 1 (true) if the "Person_Name" attribute matches
any of the names extracted from the HKN officer's web page.
"""
def assistants_HKN_officers_sql(myUsername, myPassword, myDatabase):
  names = HKN_tutor_parsing()

  conn = MySQLdb.connect(host = "localhost",
                      user = myUsername,
                      passwd = myPassword,
                      db = myDatabase)
  cursor = conn.cursor()

  for name in names:
    try:
      update_query = ("UPDATE Assistants SET Assistants.Officer = 1 "
                     "WHERE Assistants.Person_Name = %s")
      cursor.execute(update_query, name)
      conn.commit()
    except Exception, e:
      print e
      conn.rollback()

  cursor.close()
  conn.close()

"""
Set the following three arguments to modify your database:
your username, password, and database.
"""
myUsername = "ENTER_USERNAME_HERE"
myPassword = "ENTER_PASSWORD_HERE"
myDatabase = "ENTER_DATABASE_NAME_HERE"

assistants_HKN_officers_sql(myUsername, myPassword, myDatabase)

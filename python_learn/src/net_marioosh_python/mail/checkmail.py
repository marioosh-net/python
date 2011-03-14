import poplib
import sys
from email import parser
from symbol import except_clause
import MySQLdb

# klasa mail checkera
class Checker:
    def __init__(self, host, user, password, maker):
        # print 'Checker'
        self.checked_emails = [];
        self.password = password;
        self.user = user;
        self.host = host;
        self.maker = maker;
        try:
            self.p = poplib.POP3_SSL(host);
            self.p.user(user)
            self.p.pass_(password)
            print self.p.getwelcome();
        except Exception as (errno):
            print errno
            sys.exit(-1)
         
    def set_checked_emails(self, emails):
        self.checked_emails = emails;

    def count_message(self):
        try:
            return self.p.stat()[0]
        except:
            return "XXXX"
        
    def check(self):
        list = self.p.list();
        for msg in list[1]:
            msg_num = msg.split(' ')[0];
            top = self.p.top(msg_num, 0);
            h = top[1];
        
            # parsuje header   
            header = parser.HeaderParser().parsestr("\n".join(h));
           
            for e in self.checked_emails:
                if header['from'].find(e) != -1:
                   
                    # get content i body
                    r = self.p.retr(msg_num)[1];
                    content = parser.Parser().parsestr("\n".join(r));
                    body = [];
                    if content.is_multipart():
                        for part in content.get_payload():
                            body.append(part.get_payload())
                    else:
                        body.append(content.get_payload())

                    # dodaj buga
                    maker.add_bug(header['from'], header['subject'], body[0], header['to']);
                
            # tylko pierwszy mail        
            break;

    def disconnect(self):
        self.p.quit()


# klasa dostepu do bazy mantisa
class BugMaker:
    def __init__(self, host, user, password, db):
        self.conn = MySQLdb.connect(host, user, password, db);

    def list_texts(self):
        c = self.conn.cursor();
        c.execute("SELECT * FROM mantis_bug_text_table");
        rows = c.fetchall()
        for r in rows:
            print r

    def list_bugs(self):
        c = self.conn.cursor();
        c.execute("SELECT * FROM mantis_bug_table");
        rows = c.fetchall()
        for r in rows:
            print r

    def add_bug(self, email_from, subject, text, email_to):

        print "FROM:"+email_from
        print "SUBJ:"+subject
        print "TO  :"+email_to
        print "BODY:"
        print text
        return;

        # tabelka texty
        # mantis_bug_text_table.description = text
        c = self.conn.cursor();
        c.execute("INSERT INTO mantis_bug_text_table (description) VALUES('"+text+"')")
        self.conn.commit()


        # tabelka bugi
        # muntis_bug_table.summary = subject
        # mantis_bug_table.project_id = self.get_proj_id(email_to)
        # mantis_bug_table.handler_id = self.get_user_id(email_to)
        # mantis_bug_table.reporter_id = self.get_user_id(email_from)
        # mantis_bug_table.bug_text_id = mantis_bug_text_table.id

    def get_proj_id_by_user(self, email):
        return 11;  # LoogAPPS

    def get_proj_id_by_name(self, name):
        c = self.conn.cursor();
        c.execute("select id from mantis_project_table where name = '"+name+"'")
        return c.fetchone()[0]

    def get_user_id(self, email):
        c = self.conn.cursor();
        c.execute("select id from mantis_user_table where email = '"+email+"'")
        row_id = c.fetchone()[0]
        return row_id


maker = BugMaker("localhost", "bugtracker2", "AhFeiCh2", "bugtracker2");
checker = Checker('pop3.o2.pl', 'sp4my', 'zbc123', maker);
checker.set_checked_emails(['mario@marioosh.net','mario2@marioosh.net']);
print checker.count_message()
checker.check()
checker.disconnect()


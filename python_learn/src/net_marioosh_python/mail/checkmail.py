#!/usr/bin/python
# -*- coding: utf-8 -*-

import poplib
import sys
from email import parser
from symbol import except_clause
import MySQLdb
import hashlib
from datetime import datetime

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
        'ustawia liste adresow zrodlowych na ktore bedzie wrazliwy checker'
        'sprawdzal bedzie tylko te wiadomosci, ktore przyjda z maili wystepujacych w liscie'
        self.checked_emails = emails;

    def count_message(self):
        try:
            return self.p.stat()[0]
        except:
            return "XXXX"
      
    def prepare_bug(self, msg_num):
        r = self.p.retr(msg_num)[1];
        content = parser.Parser().parsestr("\n".join(r));
        body = [];
        att = [];
        for part in content.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            filename = part.get_filename()
            if filename:
                a = []
                a.append(filename)
                a.append(part.get_payload(decode=True))
                a.append(part.get_content_type())
                att.append(a)
            if part.get_content_maintype() == 'text':
                body.append(part.get_payload(decode=True))

        # dodaj buga
        maker.add_bug(content['from'], content['subject'], body[0], content['to'], att);
        # usun wiadomosc
        self.p.dele(msg_num);

    def check(self):
        list = self.p.list();
        for msg in list[1]:
            msg_num = msg.split(' ')[0];
            top = self.p.top(msg_num, 0);
            h = top[1];
        
            # parsuje header   
            header = parser.HeaderParser().parsestr("\n".join(h));
            print "---HEADER---"
            print header;
            print "---HEADER END---"
           
            if len(self.checked_emails) > 0:
                # tylko maile z listy
                for e in self.checked_emails:
                    if header['from'].find(e) != -1:
                        self.prepare_bug(msg_num);

            else:
                # przetwarzaj WSZYSTKIE maile
                # get content i body
                self.prepare_bug(msg_num);
               
            # tylko pierwszy mail        
            # break;

    def disconnect(self):
        self.p.quit()


# klasa dostepu do bazy mantisa
class BugMaker:
    def __init__(self, host, user, password, db):
        self.conn = MySQLdb.connect(host, user, password, db);
        self.log = False

    def set_log(self, log):
        self.log = log;

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

    def add_bug(self, email_from, subject, text, email_to, att):

        if self.log:
            print "FROM:"+email_from
            print "SUBJ:"+subject
            print "TO  :"+email_to
            print "ATT :"
            if len(att) > 0:
                for a in att:
                    print a[0]
            print "BODY:"
            print text

        # tabelka mantis_bug_text_table (opisy bugow)
        c = self.conn.cursor();
        sql = "INSERT INTO mantis_bug_text_table \
            (description, \
            steps_to_reproduce, \
            additional_information) VALUES \
            ('"+text+"', \
            '', \
            '[maildrop]')";
        print sql;
        c.execute(sql)
        textid = self.conn.insert_id()

        # tabelka mantis_bug_table (bugi)
        sql = "insert into mantis_bug_table \
            (project_id, \
            reporter_id, \
            handler_id, \
            bug_text_id, \
            summary, \
            date_submitted, last_updated) values \
            ("+str(self.get_proj_id_by_user(email_to))+", \
            "+str(self.get_user_id(email_from))+", \
            "+str(self.get_user_id(email_to))+", \
            "+str(textid)+", \
            '[maildrop] "+subject+"', \
            NOW(), NOW())";
        print sql;
        c.execute(sql);
        bugid = self.conn.insert_id()

        # tabelka mantis_bug_file_table (zalaczniki)
        if len(att) > 0:
            # print "attachments: "+str(len(att))
            for a in att:
                m = hashlib.md5()
                m.update(str(a[0])+str(datetime.today()))
                filesize = len(a[1]);
                blob = a[1];

                sql = "insert into mantis_bug_file_table \
                    (bug_id, \
                    diskfile, \
                    filename, \
                    filesize, \
                    file_type, \
                    date_added, \
                    content) values \
                    ("+str(bugid)+", \
                    '"+m.hexdigest()+"', \
                    '"+a[0]+"', \
                    "+str(filesize)+", \
                    '"+a[2]+"', \
                    NOW(), \
                    %s)"
                print sql
                c.execute(sql, blob);

        self.conn.commit()

    def get_proj_id_by_user(self, email):
        'zwraca id projektu, za ktory jest odpowiedzialny user o podanym emailu'
        # if email == 'mariusz@dandelion.com.pl':
        #    return 11; # LoogAPPS
        return 1;  # LBS

    def get_proj_id_by_name(self, name):
        'zwraca id projektu po nazwie'
        c = self.conn.cursor();
        c.execute("select id from mantis_project_table where name = '"+name+"'")
        return c.fetchone()[0]

    def get_user_id(self, email):
        'zwraca id usera po emailu, jesli nie znajdzie zwraca 0'
        try:
            c = self.conn.cursor();
            c.execute("select id from mantis_user_table where email = '"+email+"'")
            one = c.fetchone()
            if one != None:
                return one[0]
            else:
                c.execute("select id,email from mantis_user_table");
                rows = c.fetchall()
                for r in rows:
                    if email.find(r[1]) != -1:
                        return r[0];
                return 0;

        except Exception as (errno):
            print str(errno);
            return 0;

maker = BugMaker("localhost", "bugtracker2", "AhFeiCh2", "bugtracker2");
maker.set_log(True);

print datetime.today()
checker1 = Checker('loogberry.com', 'maildrop@loogberry.com', 'chosen12!', maker);
# checker1 = Checker('pop3.o2.pl', 'sp4my', 'zbc123', maker);

# checker1.set_checked_emails(['mario@marioosh.net','mario2@marioosh.net']);
print checker1.count_message()
checker1.check()
checker1.disconnect()


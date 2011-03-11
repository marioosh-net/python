import poplib
import sys
from email import parser
from symbol import except_clause

class Checker:
    def __init__(self, host, user, password):
        # print 'Checker'
        self.password = password;
        self.user = user;
        self.host = host;
        try:
            self.p = poplib.POP3_SSL(host);
            self.p.user(user)
            self.p.pass_(password)
            print self.p.getwelcome();
        except Exception as (errno):
            print errno
            sys.exit(-1)
         
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
            print header['from'];
            
            if header['from'].find('mario@marioosh.net') != -1 or True:
                r = self.p.retr(msg_num)[1];
                content = parser.Parser().parsestr("\n".join(r));
                # print content;
        
                body = [];
                if content.is_multipart():
                    for part in content.get_payload():
                        body.append(part.get_payload())
                else:
                    body.append(content.get_payload())
                    
                for b in body:
                    print "--------- BODY ---------- "
                    print b
                
            # tylko pierwszy mail        
            break;

    def disconnect(self):
        self.p.quit()

checker = Checker('pop3.o2.pl', 'sp4my', 'zbc123');
print checker.count_message()
# checker.check()
checker.disconnect()



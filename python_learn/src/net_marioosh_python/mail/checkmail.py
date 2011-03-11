import poplib
import sys
from email import parser

p = poplib.POP3_SSL('pop.gmail.com')
p.user('spam@marioosh.net')
p.pass_('zbc123')

print p.getwelcome();
print "MESSAGES: " + str(p.stat()[0]);

list = p.list();
for msg in list[1]:
    msg_num = msg.split(' ')[0];
    top = p.top(msg_num, 0);
    header = top[1];

    # parsuje header   
    m = parser.HeaderParser().parsestr("\n".join(header));
    print m['from'];
    
    if m['from'].find('mario@marioosh.net') != -1 or True:
        r = p.retr(msg_num)[1];
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

#Get messages from server:
# messages = [p.retr(i) for i in range(1, len(p.list()[1]) + 1)]
# Concat message pieces:
# messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
# messages = [parser.Parser().parsestr(mssg) for mssg in messages]
# for message in messages:
#     print message['subject']

p.quit()

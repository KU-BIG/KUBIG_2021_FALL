import copy
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class HtmlGen:
    def __init__(self, html):
        self.html = html

    def generate_html(self, titles, contents, hrefs):
        for i in range(len(contents)):
            self.html += '<div style = "margin-top: 20px">' \
                    '<h4 style = "font-family: sans-serif; text-align: left; width: 90%; margin: 20px auto">'
            self.html += '⬛️ '
            self.html += titles[i]
            self.html += '</h4>'
            self.html += '<h5 style = "font-family: sans-serif; text-align: left; width: 90%; margin: 20px auto">'
            self.html += '•  '
            self.html += contents[i]
            self.html += '<a href="'
            self.html += hrefs[i]
            self.html += '" style = "color = #FF9900"; text-decoration: none;> 원문 보기 </a><br></h5>' \
                '</div>'
            self.html += ' <hr style = "border: 10; border-top: solid 0.5px #F0EDCC; width: 80%; margin: 5px auto" class = "horizontal-line">'

        self.html += '<div style = "margin-top: 20px">'\
        '<h5 style = "font-family: sans-serif; text-align: right; width: 90%; margin: 20px auto">presented by… ASUM</h5></div>'
        self.html += '</body></html>'
        html = self.html

        return html

class EmailHTMLContent:
    def __init__(self, str_subject, template, template_params):
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        self.msg = MIMEMultipart()
        self.msg['Subject'] = str_subject
        str_msg = template.safe_substitute(**template_params)
        mime_msg = MIMEText(str_msg, 'html')
        self.msg.attach(mime_msg)

    def get_message(self, str_from_email_addr, str_to_eamil_addrs):
        mm = copy.deepcopy(self.msg)
        mm['From'] = str_from_email_addr
        mm['To'] = ",".join(str_to_eamil_addrs)
        return mm

class EmailSender:
    def __init__(self, str_host, email_id, app_pw,  num_port=25):
        self.str_host = str_host
        self.num_port = num_port
        self.ss = smtplib.SMTP(host=str_host, port=num_port)
        self.ss.starttls()
        self.ss.login(email_id, app_pw)

    def send_message(self, emailContent, str_from_email_addr, str_to_eamil_addrs):
        """e메일 발송 """
        cc = emailContent.get_message(str_from_email_addr, str_to_eamil_addrs)
        self.ss.send_message(cc, from_addr=str_from_email_addr, to_addrs=str_to_eamil_addrs)
        print("메일전송 완료!")
        del cc

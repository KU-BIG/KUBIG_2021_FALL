from datetime import datetime
from string import Template
from generate_sum import TextSummarize
from email_send import HtmlGen, EmailHTMLContent, EmailSender
from news_crawler import WebScraper
import pandas as pd
import argparse

class Main:
    def __init__(self):
        self.summaries = []
        self.titles = []
        self.hrefs = []
        self.msg = ""
        self.header ='<!DOCTYPE html> <html><body style = "margin: 0; padding: 0;"><center><img src = https://blogfiles.pstatic.net/MjAyMTA4MzBfNzkg/MDAxNjMwMzEzMTU3NTMx.GLGTmEeYBdCAxgg_lgmOMkglGm2_mFvtLtR213RxSy4g.8xz3NAgYIdYJHZqtZTwwl8kyfResjWhGYL-4W20HV4Ag.JPEG.yoon_hknmtt/asum.jpg style = "width: 500px; height: 135px"> </center><div><h2 style = "color = #02343F; font-family: sans-serif; text-align: center;"><strong>오늘의 최신 뉴스 요약본👀</strong></h2><hr style = "border: 10; border-top: solid 1px #F0EDCC; width: 90%; margin: 20px auto" class = "horizontal-line"></div>'

    def main(self, email_id, pw, news_num=None):
        scraper = WebScraper("https://news.naver.com/")
        summarizer = TextSummarize(model_name="result3_epoch5_batch8_config/checkpoint-112500")

        titles, articles, hrefs = scraper.main()

        if news_num is None:
            news_num = len(articles)

        i=0
        for i in range(news_num):
            i+=1
            try:
                text = summarizer.gen(articles[i])
                summarized = text.replace('"', '').replace("'", "")
                self.msg += f"{str(i)}\t{text}\n\n"
                
                print(i, ':', summarized)

                self.summaries.append(summarized)
                self.titles.append(titles[i])
                self.hrefs.append(hrefs[i])

            except:
                continue

        htmlgen = HtmlGen(self.header)
        html = htmlgen.generate_html(self.titles, self.summaries, self.hrefs)

        str_host = 'smtp.gmail.com'
        num_port = 587
        emailSender = EmailSender(str_host, email_id, pw, num_port)

        title = datetime.today().strftime('%Y-%m-%d')
        str_subject = title + " 오늘의 최신뉴스 요약본입니다!"
        template = Template(html)
        template_params = {'NAME': 'Keom'}
        emailHTMLContent = EmailHTMLContent(str_subject, template, template_params)

        str_from_email_addr = email_id

        f = open('email_list.txt')
        str_to_email_addrs = [x.strip() for x in f.readlines()]  # 수신자리스트
        emailSender.send_message(emailHTMLContent, str_from_email_addr, str_to_email_addrs)
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter your gmail address and app password. This should be yours (sender) not receiver's email.")
    parser.add_argument('--email', type=str, help='Your gmail address')
    parser.add_argument('--password', type=str, help='Application password from gmail.')
    args = parser.parse_args()

    email = args.email
    pswd = args.password
    
    main = Main()
    main.main(email, pswd)

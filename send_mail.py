__author__ = 'Vishal'

import click
import smtplib
import socket
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

addresses = ['tarunkodavati2797@gmail.com', 'prudhvipotnuru1998@gmail.com', 'saidinesh107289@gmail.com',
             'mounica2798@gmail.com', 'harinarayanabatta1997@gmail.com', 'abhivardhanavr@gmail.com',
             'kogantikrishnasree@gmail.com', 'susmithasanikommu@gmail.com', 'sameerkhanmd112@gmail.com',
             'vamshichennoju225@gmail.com', 'nagasitaram.ram@gmail.com', 'reddyshyam1997@gmail.com',
             'sunkara.satyasarika@gmail.com', 'cherubimpalukury@gmail.com', 'pavansai57@gmail.com',
             'shashankvidiyala@gmail.com', 'k.ramakrishna93@gmail.com', 'k.madhusudan12@gmail.com',
             'merlinmegha005@gmail.com', 'pranadeepreddy17@gmail.com', 'alkadevendargoud369@gmail.com',
             'syedazhartalha@gmail.com', 'dtejasrireddy@gmail.com', 'abhivardhanavr@gmail.com',
             'vishalreddy.k11@gmail.com', 'pranitha.jemmalla@gmail.com', 'shantanu4644@gmail.com',
             'prashanthganoji@gmail.com', 'pallavireddy.palwai@gmail.com', 'saicharancherry593@gmail.com',
             'durgaprasadrangavajjala@gmail.com', 'pothurihariprasad9972@gmail.com', 'raazapadala@gmail.com',
             'aditya.bulusu168@gmail.com', 'm.vema.5298@gmail.com', 'medisettirajesh123@gmail.com',
             'anjantatavarthi1997@gmail.com', 'ramdeepakpedapati@gmail.com', 'jayanthsai1998@gmail.com',
             'ashokkumar.201198@gmail.com', 'bhanuteja2696@gmail.com', 'padmasowgandhika77@gmail.com',
             'mounikakedarisetti997@gmail.com', 'majaykumar51@gmail.com', 'kollarevanth@gmail.com',
             'irfanahmed.511.ia@gmail.com', 'vasisai128@gmail.com', 'a.d.g.sankar@gmail.com',
             'aslambasha95016@gmail.com', 'sheetansh123@gmail.com', 'naveenrock38@gmail.com', 's.meena9874@gmail.com',
             'mrudula.nudurupati1997@gmail.com', 'saibharath15.gutti@gmail.com', 'c.samudrudu333@gmail.com',
             'priyankailluri.98@gmail.com', 'akhil.7stars@gmail.com', 'ysashwini55@gmail.com',
             'ramya.reddy161@gmail.com', 'anushapolaki0618@gmail.com', 'ujwalhanuman@gmail.com',
             'sreekar.mouli1998@gmail.com', 'sunnysonu582@gmail.com', 'krishna.5053@gmail.com',
             'avinashravula1@gmail.com', 'achyuthmadala@gmail.com', 'sriakhilasri@gmail.com', 'msvsr11297@gmail.com',
             'supriyakommisetti111@gmail.com', 'mohinipriya1998@gmail.com', 'mksnehaal@gmail.com',
             'krushiraj123@gmail.com', 'abhinav071197@gmail.com', 'shiva.sairam97@gmail.com', 'hanish2760@gmail.com',
             'anuhyareddy9999@gmail.com', 'someshthakur33@gmail.com', 'abhijithchndr8@gmail.com',
             'abishekvanam@gmail.com', 'pravalikavis@gmail.com', 'chakradhar51.p@gmail.com', 'karthikvg1998@gmail.com',
             'saikishan2008@gmail.com', 'jayasaishankar@gmail.com', 'arpitgupta820@gmail.com']


def send_mail():
    """Sends the college report to the given mail id"""

    for to_add in addresses:

        click.echo("Sending mail ...")

        from_address = "mrndconfession2018@gmail.com"
        to_address = to_add
        password = "chakradharbro69"

        msg = MIMEMultipart("Alternative")

        with open("message.txt") as f:
            msg = MIMEText(f.read())

        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Official Mission RnD Summer 2018 WhatsApp Group Link"

        # html = convert_to_html()
        # part2 = MIMEText(html, 'html')

        # msg.attach(part1)
        # msg.attach(part2)

        try:
            smtp_client = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_client.starttls()
            smtp_client.login(from_address, password)
            text = msg.as_string()
            smtp_client.sendmail(from_address, to_address, text)
            smtp_client.quit()
        except socket.error:
            click.echo("Mail id %s: Couldn't connect to the server." % to_add)
        except smtplib.SMTPNotSupportedError:
            click.echo("Mail id %s: SMTP AUTH extension not supported by server." % to_add)
        except smtplib.SMTPAuthenticationError:
            click.echo("Mail id %s: Invalid Credentials entered." % to_add)
        except smtplib.SMTPException:
            click.echo("Mail id %s: Unknown Error" % to_add, sys.exc_info()[0])
        else:
            click.echo("Mail sent successfully to %s" % to_add)


if __name__ == '__main__':
    send_mail()

def correoContainer(correoEmisor,passwords,email_content,destinatario):
    # -*- coding: utf8 -*-
    print(email_content)
    import smtplib
    import email.message
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    print(f'correo enviado a:{destinatario}')
    msg = email.message.Message()
    msg['Subject'] = 'Imobiliaria Huertas'
    msg['From'] = correoEmisor
    msg['To'] = destinatario
    password = passwords
    print(msg['From'])
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content, 'utf-8')
    s.starttls()
    s.login(msg['From'], password)
    
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

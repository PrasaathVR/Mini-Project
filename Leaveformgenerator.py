from xml.dom import DomstringSizeErr


Name=input("Student name:")
Course=input("Course name:")
Date=str(input("Enter the date:"))
Place=input("Enter the place:")
Instructor=input("Instructor name:")
Site=input("Site used to learn:")
Reason=input("Enter the reason for taking leave:")
Sub=input("Subject:")
Leaveday=str(input("How many days of leave:"))
Result= f'''
From
    {Name}
    {Course}
    {Site}

To
  {Instructor}
  Instructor in {Course}
  {Site}

Respected Sir,
        Sub:{Sub}
              Hai sir,I am {Name} currently I'm pursuing in {Course} and I'm writing this to inform you that {Reason} so I humbly request you to grant me a leave for {Leaveday} and I hope you understand my situation.

                                                                Yours Sincerely
                                                                   {Name}

Date:{Date}
Place:{Place}
'''
print(Result)
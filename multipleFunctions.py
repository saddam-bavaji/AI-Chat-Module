class multipleFunctions():
     def Subfields():
        list = ['Machine Learing','Neutral Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print('Subfields in AI are:')
        for temp in list:
            print(temp)
         
     def OddEven():
        num1 = int(input("Enter a number"))
        if num1%2==0:
            print(num1,'is Even number')
        else:
            print(num1,'is Odd number')
            
     def Eligible():
        gender = input('Your Gender:')
        age = int(input('Your Age:'))
        if(gender=='Male'):
            if(age>=21):
                print('Eligible')
            else:
                print('Not Eligible')
        else:
            if(age>=18):
                print('Eligible')
            else:
                print('Not Eligible')
                
     def percentage():
        Subj1 = int(input('Subject1='))
        Subj2 = int(input('Subject2='))
        Subj3 = int(input('Subject3='))
        Subj4 = int(input('Subject4='))
        Subj5 = int(input('Subject5='))
        addSubj = Subj1+Subj2+Subj3+Subj4+Subj5
        percent = addSubj/5
        print("total:",addSubj)
        print("Percentatge:",percent)
        
     def triangle():
        Height = int(input('Height:'))
        Breadth = int(input('Breadth:'))
        Area = (Height*Breadth)/2
        print('Area formula: (Height*Breadth)/2')
        print('Area of Triangle:',Area)
        Height1 = int(input('Height1:'))
        Height2 = int(input('Height2:'))
        Breadth = int(input('Breadth:'))
        print('Perimeter formula: Height1+Height2+Breadth')
        perimeter = Height1+Height2+Breadth
        print('Perimeter of Triangle:',perimeter)
        
import mysql.connector

def signin():
    a = input("USER NAME: ")
    b = input("PASSWORD: ")
    s = "SELECT user_name FROM user_accounts WHERE password=%s"
    cursor.execute(s, (b,))
    data = cursor.fetchone()
    if data and data[0] == a:
        print("\t\t\t\t\t..................................................")
        print("\t\t\t LOGIN SUCCESSFULLY")
        print("\t\t\t\t\t..................................................")
        main()
        return
    else:
        print("ACCOUNT DOES NOT EXIST OR WRONG ENTRY")

def signup():
    f = input("FIRST NAME: ")
    l = input("LAST NAME: ")
    a = input("USER NAME: ")
    b = input("PASSWORD: ")
    c = input("RE-ENTER YOUR PASSWORD: ")
    ph = input("PHONE NUMBER: ")
    print("M=MALE\nF=FEMALE\nN=NOT TO MENTION")
    gen = input("ENTER YOUR GENDER: ")
    print("ENTER YOUR DATE OF BIRTH")
    d = input("DD: ")
    o = input("MM: ")
    p = input("YYYY: ")
    dob = d + "/" + o + "/" + p
    age = input("YOUR AGE: ")
    v = {"M": "MALE", "F": "FEMALE", "N": "NOT TO MENTION"}
    if b == c:
        c1 = "INSERT INTO user_accounts VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (f, l, a, b, ph, v[gen], dob, age)
        cursor.execute(c1, values)
        print("\t\t\t\t\t..................................................")
        print("\t\t\t SIGN UP SUCCESSFULLY")
        print("\t\t\t\t\t..................................................")
        main()
        return
    else:
        print("BOTH PASSWORDS ARE NOT MATCHING")

def ticket_booking():
    nm = input("ENTER YOUR NAME: ")
    phno = input("ENTER YOUR PHONE NUMBER: ")
    age = int(input("ENTER YOUR AGE: "))
    print("M=MALE\nF=FEMALE\nN=NOT TO MENTION")
    gender = input("ENTER YOUR GENDER: ").upper()
    fr = input("ENTER YOUR STARTING POINT: ")
    to = input("ENTER YOUR DESTINATION: ")
    date1 = input("ENTER DATE(dd): ")
    date2 = input("ENTER MONTH(mm): ")
    date3 = input("ENTER YEAR(yyyy): ")
    date = date1 + "/" + date2 + "/" + date3
    a = {"M": "MALE", "F": "FEMALE", "N": "NOT TO MENTION"}
    v = a[gender]
    q = "SELECT * FROM train WHERE departure = %s AND destination = %s"
    cursor.execute(q, (fr, to))
    trains=cursor.fetchall()
    if not trains:
            print("No trains found for this route.")
    for row in trains:
            print(row)
    tnumber=int(input("Enter train number you want to book:"))
    s1 = "INSERT INTO railway (name, phno, age, gender, from_f, to_t, date_d, tnumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nm, phno, age, v, fr, to, date, tnumber)
    cursor.execute(s1, values)
    booking_id = cursor.lastrowid
    print("\t\t\t\t\t..................................................")
    print("\t\t\t TICKET BOOKED SUCCESSFULLY")
    print(f"\t\t\t YOUR BOOKING ID IS: {booking_id}")
    print("\t\t\t\t\t..................................................")

def ticket_checking():
    phno = input("Enter phone number: ")
    s1 = "SELECT * FROM railway WHERE phno = %s"
    cursor.execute(s1, (phno,))
    bookings = cursor.fetchall()

    if bookings:
        for data in bookings:
            print("\n----- TICKET DETAILS -----")
            labels = ["NAME", "PHONENO", "AGE", "GENDER", "FROM", "TO", "DATE"]
            for i in range(7):
                print(f"{labels[i]} ::: {data[i]}")
            
            tnum = data[7]  # Assuming tnumber is the 8th item
            cursor.fetchall()  # 👈 Ensures previous result is cleared
            cursor.execute("SELECT tname, timeofdep FROM train WHERE tnumber = %s", (tnum,))
            train_data = cursor.fetchone()
            if train_data:
                print(f"TRAIN ::: {train_data[0]}")
                print(f"DEPARTURE TIME ::: {train_data[1]}")
            else:
                print("TRAIN INFO NOT FOUND")
    else:
        print("No ticket found for this phone number.")


def ticket_cancelling():
    try:
        phno = input("ENTER YOUR PHONE NUMBER: ")
        booking_id = int(input("ENTER YOUR BOOKING ID: "))

        # Check if the booking exists for that phone number and ID
        s = "SELECT * FROM railway WHERE booking_id = %s AND phno = %s"
        cursor.execute(s, (booking_id, phno))
        data = cursor.fetchone()

        if data:
            s1 = "DELETE FROM railway WHERE booking_id = %s"
            cursor.execute(s1, (booking_id,))
            print("\t\t\t\t\t..................................................")
            print("\t\t\t TICKET CANCELLED")
            print("\t\t\t\t\t..................................................")
            main()
        else:
            print("NO MATCHING BOOKING FOUND FOR THIS PHONE NUMBER AND BOOKING ID.")
    except ValueError:
        print("INVALID BOOKING ID FORMAT.")


def display():
    a = input("USER NAME: ")
    b = input("PASSWORD: ")
    try:
        s1 = "SELECT user_name FROM user_accounts WHERE password = %s"
        c1 = "SELECT fname, lname FROM user_accounts WHERE password = %s"
        cursor.execute(c1, (b,))
        data1 = cursor.fetchone()
        name = data1[0] + " " + data1[1]
        cursor.execute(s1, (b,))
        data = cursor.fetchone()
        if data and data[0] == a:
            x = ["FIRSTNAME", "LASTNAME", "PHONENUMBER", "GENDER", "DATE OF BIRTH", "AGE"]
            s1 = "SELECT fname, lname, phno, gender, dob, age FROM user_accounts WHERE password = %s"
            cursor.execute(s1, (b,))
            data = cursor.fetchone()
            for i in range(len(x)):
                print(f"{x[i]} ::: {data[i]}")
        else:
            print("INVALID USERNAME OR PASSWORD")
    except:
        print("ACCOUNT DOES NOT EXIST")

def main():
    while True:
        print("\t\t\t\t\t..................................................")
        print("\t\t\t 1. TICKET BOOKING")
        print("\t\t\t 2. TICKET CHECKING")
        print("\t\t\t 3. TICKET CANCELLING")
        print("\t\t\t 4. ACCOUNT DETAILS")
        print("\t\t\t 5. LOG OUT")
        print("\t\t\t\t\t..................................................")
        ch = int(input("ENTER YOUR CHOICE: "))
        if ch == 1:
            ticket_booking()
        elif ch == 2:
            ticket_checking()
        elif ch == 3:
            ticket_cancelling()
        elif ch == 4:
            display()
        elif ch == 5:
            print("THANK YOU")
            break
        else:
            print("ENTER 404: ERROR PAGE NOT FOUND")

# Database connection
mycon = mysql.connector.connect(host="localhost", user="root", passwd="1234")
cursor = mycon.cursor()
mycon.autocommit = True
cursor.execute("USE railway")

cursor.execute("""CREATE TABLE IF NOT EXISTS railway (
    name VARCHAR(100),
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    phno VARCHAR(15),
    age INT(4),
    gender VARCHAR(50),
    from_f VARCHAR(100),
    to_t VARCHAR(100),
    date_d VARCHAR(20),
    tnumber int
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_accounts (
    fname VARCHAR(100),
    lname VARCHAR(100),
    user_name VARCHAR(100),
    password VARCHAR(100) PRIMARY KEY,
    phno VARCHAR(15),
    gender VARCHAR(50),
    dob VARCHAR(50),
    age VARCHAR(4)
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS train(
    tname VARCHAR(100),
    tnumber INT Primary key,
    seat VARCHAR(20),
    departure VARCHAR(20),
    destination VARCHAR(20),
    timeofdep varchar(20)
    )""")
cursor.execute("""INSERT IGNORE INTO train (tname, tnumber, seat, departure, destination, timeofdep) VALUES
('Rajdhani Express', 12301, '800', 'New Delhi', 'Mumbai', '7:00 am'),
('Shatabdi Express', 12025, '500', 'Chandigarh', 'New Delhi', '6:15 am'),
('Duronto Express', 12213, '600', 'Pune', 'Nagpur', '5:45 am'),
('Gatimaan Express', 12049, '400', 'New Delhi', 'Agra', '8:10 am'),
('Vande Bharat Express', 22436, '600', 'Lucknow', 'Delhi', '6:00 am'),
('Howrah Mail', 12809, '750', 'Mumbai', 'Howrah', '21:45 pm'),
('Garib Rath', 12909, '700', 'Mumbai', 'Delhi', '16:20 pm'),
('Karnataka Express', 12627, '850', 'New Delhi', 'Bengaluru', '8:20 pm'),
('Tamil Nadu Express', 12621, '780', 'New Delhi', 'Chennai', '10:30 pm'),
('Goa Express', 12779, '620', 'Hazrat Nizamuddin', 'Vasco da Gama', '3:00 pm'),
('Sealdah Express', 12314, '700', 'New Delhi', 'Sealdah', '7:10 am'),
('Jammu Tawi Express', 13151, '550', 'Kolkata', 'Jammu Tawi', '11:45 am'),
('Deccan Queen', 12123, '500', 'Mumbai', 'Pune', '5:10 pm'),
('Nanda Devi Express', 12205, '480', 'New Delhi', 'Dehradun', '11:50 pm'),
('Chhattisgarh Express', 18237, '650', 'Saharanpur', 'Amritsar', '12:05 am'),
('Golden Temple Mail', 12904, '700', 'Saharanpur', 'Mumbai Central', '12:20 am'),
('Jhelum Express', 11078, '620', 'Saharanpur', 'Pune', '2:45 pm'),
('Dehradun Express', 19020, '580', 'Saharanpur', 'Mumbai Bandra', '10:30 pm'),
('Utkal Express', 18478, '600', 'Saharanpur', 'Puri', '3:10 pm'),
('Ganga Sutlej Express', 13307, '550', 'Saharanpur', 'Firozpur', '3:00 am'),
('Begampura Express', 12237, '720', 'Saharanpur', 'Jammu Tawi', '2:30 am'),
('Vande Bharat Express', 22457, '700', 'Saharanpur', 'Dehradun', '6:00 am'),
('Shatabdi Express', 12017, '650', 'Saharanpur', 'Dehradun', '10:15 am'),
('Amritsar-Dehradun Express', 14632, '600', 'Saharanpur', 'Dehradun', '4:55 am'),
('Golden Temple Mail', 12904, '720', 'Saharanpur', 'Ghaziabad', '12:20 am'),
('Chhattisgarh Express', 18238, '680', 'Saharanpur', 'Ghaziabad', '12:35 am'),
('Dehradun Shatabdi', 12018, '750', 'Saharanpur', 'Ghaziabad', '7:55 pm'),
('Ujjaini Express', 14310, '620', 'Saharanpur', 'Ghaziabad', '9:55 am')
""")

 

print("................................................................")
while True:
    print("\t\t\t\t\t WELCOME TO ONLINE RESERVATION SYSTEM")
    print("\t\t\t\t\t..................................................")
    print("\t\t\t 1. SIGN IN")
    print("\t\t\t 2. SIGN UP")
    print("\t\t\t 3. EXIT")
    print("\t\t\t\t\t..................................................")
    ch = int(input("\t\t\t ENTER YOUR CHOICE: "))
    if ch == 1:
        signin()
    elif ch == 2:
        signup()
    elif ch == 3:
        print("\t\t\t\t\t..................................................")
        print("\t\t\t Thank you")
        print("\t\t\t\t\t..................................................")
        break

    

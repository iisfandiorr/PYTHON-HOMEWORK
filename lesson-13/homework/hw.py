import datetime

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
today = datetime.date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days_in_prev_month = (datetime.date(prev_year, prev_month % 12 + 1, 1) - datetime.date(prev_year, prev_month, 1)).days
    days += days_in_prev_month

if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")

import datetime

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
today = datetime.date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days_in_prev_month = (datetime.date(prev_year, prev_month % 12 + 1, 1) - datetime.date(prev_year, prev_month, 1)).days
    days += days_in_prev_month

if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")

next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)

if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)

days_until_birthday = (next_birthday - today).days

months_until = days_until_birthday // 30
days_remainder = days_until_birthday % 30

print(f"Your next birthday is in {days_until_birthday} days (~{months_until} months and {days_remainder} days).")
print(f"Next birthday date: {next_birthday.strftime('%A, %B %d, %Y')}")

import datetime

year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))
hour = int(input('Enter hour: '))
minute = int(input('Enter minutes: '))
second = int(input('Enter seconds: '))

current_time = datetime.datetime(year, month, day, hour, minute, second)

duration_hours = int(input('Enter meeting duration (hours): '))
duration_minutes = int(input('Enter meeting duration (minutes): '))

duration = datetime.timedelta(hours=duration_hours, minutes=duration_minutes)
end_time = current_time + duration

print("\nMeeting start time:", current_time.strftime("%H:%M:%S %A, %B %d, %Y"))
print("Meeting end time:  ", end_time.strftime("%H:%M:%S %A, %B %d, %Y"))

import pytz
tz_ny = pytz.timezone('America/New_York')
tz_msk = pytz.timezone('Europe/Moscow')
datetimeNY = datetime.datetime.now(tz_ny)
datetimeMSK = datetime.datetime.now(tz_msk)
datetimeLocal = datetime.datetime.now()
print(datetimeNY)
print(datetimeMSK)
print(datetimeLocal)

import datetime
import pytz

print("Example timezones: America/New_York, Europe/Moscow, Asia/Tokyo, UTC\n")

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
src_tz_name = input("Enter your current timezone (e.g. Europe/Moscow): ")
dst_tz_name = input("Enter target timezone (e.g. America/New_York): ")

naive_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

src_tz = pytz.timezone(src_tz_name)
dst_tz = pytz.timezone(dst_tz_name)

src_dt = src_tz.localize(naive_dt)
dst_dt = src_dt.astimezone(dst_tz)

print("\nOriginal time:", src_dt.strftime("%Y-%m-%d %H:%M (%Z)"))
print("Converted time:", dst_dt.strftime("%Y-%m-%d %H:%M (%Z)"))

import re

pattern = '[a-zA-Z0-9!@#$%^&*()_+=-]+@[a-zA-Z0-9-]+[a-zA-Z]{2,5}'

email = input('Enter email')

result = re.match(pattern, email)

if result:
    print("valid email")
else:
    print('Invalid email')

a = input("Enter your 10-digit mobile number: ")

if len(a) == 10 and a.isdigit():
    formatted = f"({a[0:3]}) {a[3:6]}-{a[6:10]}"
    print("Formatted number:", formatted)
else:
    print("Invalid number! Please enter exactly 10 digits.")

a = input("Enter password: ")

has_upper = any(ch.isupper() for ch in a)
has_lower = any(ch.islower() for ch in a)
has_digit = any(ch.isdigit() for ch in a)

if len(a) > 8 and has_upper and has_lower and has_digit:
    print("Your password is valid")
else:
    print("Your password is invalid")

import re

pattern_text = '''From the moment the brand was founded, Dior became synonymous with elegance, sophistication, and innovation in fashion. Christian Dior, the visionary behind the name Dior, revolutionized the world of haute couture with his “New Look” in 1947, instantly capturing the attention of the global fashion scene. Dior has always been more than a brand; it represents a lifestyle, a statement, and a standard of excellence that continues to inspire designers, artists, and fashion enthusiasts around the world.

The legacy of Dior is rooted in its ability to blend tradition with modernity. Each collection that bears the Dior name tells a story, reflecting not only the era it is created in but also the timeless values of style, elegance, and creativity. From the iconic dresses to the meticulously crafted suits, Dior clothing is a testament to precision, artistry, and vision. The influence of Dior reaches far beyond runways, shaping trends, inspiring photography, and defining the way people perceive fashion globally.

One cannot discuss luxury fashion without mentioning Dior perfumes. Fragrances such as Jadore, Miss Dior, and Sauvage have become legendary, each capturing the essence of sophistication and allure that the brand Dior represents. Every bottle, every scent is a reflection of the meticulous attention to detail that Dior applies to all aspects of its work. These perfumes are not just products; they are cultural icons, bearing the name Dior and leaving a lasting impression on anyone who experiences them.

Accessories are another realm where Dior excels. Handbags, shoes, and jewelry designed by Dior are instantly recognizable for their elegance, quality, and innovation. Celebrities and fashion enthusiasts alike covet items with the Dior logo, understanding that they represent a combination of style, status, and heritage. The timeless appeal of Dior accessories lies in their ability to elevate any outfit, making the wearer feel confident, sophisticated, and unique.

Fashion shows by Dior are celebrated events in themselves. Each runway presentation is not only a showcase of clothing but also a display of creativity, storytelling, and artistry. When Dior unveils a new collection, the world watches, knowing that every piece carries the signature elegance and meticulous craftsmanship that the brand is famous for. The impact of Dior on global fashion cannot be overstated, as the brand continues to influence trends, inspire emerging designers, and set new standards for luxury.

The influence of Dior extends into art and culture. Collaborations with contemporary artists, photographers, and creative directors have allowed Dior to continually reinvent itself while maintaining its core identity. These partnerships result in limited-edition collections that merge fashion with art, turning everyday items into collectible masterpieces. Dior proves that fashion is not merely about clothing; it is about expression, identity, and creativity.

Dior has also embraced innovation and sustainability, understanding that modern luxury must evolve responsibly. From eco-conscious materials to sustainable production methods, Dior balances elegance with ethical responsibility. The brand’s commitment to excellence is reflected not only in its products but also in its forward-thinking approach, ensuring that Dior remains relevant and admired in a rapidly changing world.'''

search_word = input('Enter your word: ')
pattern = rf'\\b{re.escape(search_word)}\\b'
result = re.findall(pattern, pattern_text, flags=re.IGNORECASE)
print(f'The word "{search_word}" was found {len(result)} times.')

import re

pattern_text = '''On 12.03.1995, the city hosted its first international art festival, attracting artists from all over the world. Just three years later, on 05.07.1998, a new museum opened, showcasing modern art and historical exhibitions. On 21.11.2002, the museum organized a special event commemorating local painters. Then, on 14.02.2010, a rare collection of sculptures was unveiled, drawing record crowds. Another significant day was 30.08.2015, when the city celebrated its 200th anniversary with parades and concerts. On 01.01.2020, a major renovation project began for the city’s cultural center. Each of these dates, like 12.06.2023, marks milestones that shaped the city’s artistic and historical legacy.'''

date_pattern = r'\\b\\d{2}\\.\\d{2}\\.\\d{4}\\b'
dates_found = re.findall(date_pattern, pattern_text)
print("Found dates:", dates_found)
print(f"Total dates found: {len(dates_found)}")

# resume_parser.py



# Ask user for data
name = input("Enter your name: ")
bio = input("Enter your bio: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")
address = input("Enter your address: ")
headline = input("Enter your headline: ")
photo_url = input("Enter your photo image URL: ")
resume_url = input("Enter your resume URL: ")

# Print the collected data
print("\n" + "="*40)
print("RESUME")
print("="*40)
print(f"Name: {name}")
print(f"Headline: {headline}")
print(f"Bio: {bio}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Address: {address}")
print(f"Photo URL: {photo_url}")
print(f"Resume URL: {resume_url}")

from sys import argv
script, user_name, password= argv
prompt = '>>> '

print(f'Hi {user_name}')
print(f'the script name is {script}')
print(f'do you like the {script}?')
like = input(prompt)

print(f'what OS are you running {user_name}')
os = input(prompt)

print(f'your password is {password} retype to confirm')
password = input (prompt)

print(f"""
So you said that you {like} the script
You are running {os}
and as mentioned your password is {password}
""")

import os

filepath = 'README.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '[YOUR_NAME]': 'Rutab Aziz',
    '[YOUR_USERNAME]': 'Sy-hash-collab',
    '[YOUR_EMAIL]': 'rutabaziz2004@gmail.com',
    '[YOUR_TAGLINE_1]': 'Developer',
    '[YOUR_TAGLINE_2]': 'Open Source Enthusiast',
    '[YOUR_TAGLINE_3]': 'Lifelong Learner',
    '[YOUR_INTERESTS]': 'web development and open-source',
    '[YOUR_CURRENT_WORK]': 'innovative projects',
    '[YOUR_HOBBY_1]': 'Coding',
    '[YOUR_HOBBY_2]': 'Reading',
    '[YOUR_HOBBY_3]': 'Exploring new tech',
    '[INTEREST_1]': 'JavaScript',
    '[INTEREST_2]': 'Python',
    '[INTEREST_3]': 'React',
    '[YOUR_LINKEDIN]': 'in/rutabaziz',
    '[YOUR_QUOTE]': 'Hello, World!'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

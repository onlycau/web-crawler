import re

content='54akyr5oir54ix5l'
content=re.sub('\d+', '', content)
print(content)
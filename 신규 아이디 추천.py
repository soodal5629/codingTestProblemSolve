import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    special = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in special:
        new_id = new_id.replace(i, '')
    new_id = re.sub('\.+', '.', new_id)
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    if len(new_id) <3:
        temp = new_id[-1]
        while len(new_id) <3:
            new_id += temp
    answer = new_id
    return answer

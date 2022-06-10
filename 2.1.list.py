characters = [
    'jonatan jostar ',
    'joseph jostar ',
    'dio grande ',
    'kujo jotaro ',
    'joske higashikata',
    'jorno jovana '
]
print('jojo:')
for x in characters:
    if x.count('jo') == 2:
        print(x)

# список написать можно быстрее,
# искать по списку проще, т.к. список терпим к сокращениям и к обращению к номерам элементов
# не получится использовать ключ, как в словаре
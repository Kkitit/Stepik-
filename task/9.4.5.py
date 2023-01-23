mail_list = input().split(' ')
out = list(filter(lambda x: '.' in x[x.index('@'):] and x[0].isalpha(), mail_list))

print(*out)




def messages(tag):
    summary = []
    lines = tag.splitlines()
    for line in lines:
        person = line.split('|')[1]
        data = line.split('|')[6].replace('@cabin', '').strip()
        summary.append(person + ': ' + data)
    return "\n".join(summary)

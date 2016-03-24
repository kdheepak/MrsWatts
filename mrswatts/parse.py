try:
    import android
except:
    pass

import sys


def messages(tag):
    summary = []
    lines = tag.splitlines()
    for line in lines:
        person = line.split('|')[1]
        data = line.split('|')[6].replace('@cabin', '').strip()
        summary.append(person + ': ' + data)
    return "\n".join(summary)

if __name__ == "__main__":
    try:
        droid = android.Android()
    except:
        pass
    try:
        lines = droid.getIntent().result[u'extras'][u'%lines']
    except:
        droid.makeToast('data missing')
        sys.exit(1)

    try:
        line_number = droid.getIntent().result[u'extras'][u'%line_number']
    except:
        line_number = 0

    try:
        position = droid.getIntent().result[u'extras'][u'%position']
    except:
        position = 0

    print(lines.splitlines()[line_number].split('|')[position].strip())

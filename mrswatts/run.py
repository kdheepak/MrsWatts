import sys
import android

import parse

if __name__ == '__main__':
    droid = android.Android()
    try:
        tag = droid.getIntent().result[u'extras'][u'%tag']
        contacts = droid.getIntent().result[u'extras'][u'%contacts']
    except:
        droid.makeToast('data missing')
        sys.exit(1)

    droid.makeToast(parse.messages(tag, contacts))
    droid.setClipboard(parse.messages(tag, contacts))

    sys.exit(1)

import sys

if __name__ == '__main__':
    print(sys.argv)
    import android
    droid = android.Android()
    droid.makeToast(str(sys.argv))

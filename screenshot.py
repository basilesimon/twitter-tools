# Run me with 'nosetests screenshot.py --with-save-baseline --nocapture'

import MySQLdb
from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS

db = MySQLdb.connect(host="",
                     user="",
                     passwd="",
                     db="")


class captureTweetScreenshots(NeedleTestCase):

    @classmethod
    def get_web_driver(cls):
        return NeedlePhantomJS()

    def test_masthead(self):
        self.list_to_screenshot()

    def writeSuccess(self, path):

        cur = db.cursor()
        try:
            cur.execute("""UPDATE Tweets \
                      SET Screenshot=1 \
                      WHERE Tweet_Id=%s""", [path])
            db.commit()
            print "Screenshot OK. Tweet id ", path
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)

            print "Error", e.args[0], e.args[1]
            print "Warning:", path, "not saved to database"
        return True

    def markDeleted(self, path):

        cur = db.cursor()
        try:
            cur.execute("""UPDATE Tweets \
                      SET Deleted=1 \
                      WHERE Tweet_Id=%s""", [path])
            db.commit()
            print "Tweet marked as deleted ", path
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)

            print "Error", e.args[0], e.args[1]
            print "Warning:", path, "not saved to database"
        return True

    def list_to_screenshot(self):
        logFile = open('logfile.txt', 'w')
        cur = db.cursor()
        cur.execute("SELECT Url, Tweet_Id FROM Tweets WHERE Screenshot=0 AND Deleted=0 ")
        for (Url, Tweet_Id) in cur:
            try:
                self.driver.get(Url)
            except:
                print "Url doesnt exist ", Url
                logFile.write("Url doesnt exist \n")
                continue
            try:
                self.assertScreenshot('.tweet', Tweet_Id)

            except:
                print "Tweet deleted ", Url
                self.markDeleted(Tweet_Id)
                message = "Tweet deleted %s \n" % Url
                logFile.write(message)
                continue
            self.writeSuccess(Tweet_Id)
            message = "Tweet screenshotted %s \n" % Url
            logFile.write(message)
        logFile.close()
# if __name__ == '__main__':
#     list_to_screenshot(db)

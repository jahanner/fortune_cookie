import random
import webapp2

def getRandomFortune():
    fortunes = [
    "I see much code in your future",
    "Eat mo chickn",
    "You have tamed Python"
    ]
    index = random.randint(0, 2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        number_sentence = 'Your lucky number is: ' + lucky_number
        num_paragraph = "<p>" + number_sentence + "</p>"

        cookie_button = "<a href='.'><button>Another fortune please!</button></a>"

        content = header + fortune + num_paragraph + cookie_button
        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for nothing...")

app = webapp2.WSGIApplication([
('/', MainHandler),
], debug=True)

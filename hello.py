# importing the main event loop
import tornado.ioloop
#for HTTP requestHandlers(to map the requests to request handlers)
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Tornado !')

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>This is Post 1 </h1>")

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

# http://localhost:8080/weather?degree=18        
class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "Hot !!" if degree > 20 else "Cold !!"
        drink = "Have some ice coffee!!" if degree > 20 else "You need hot beverage"
        self.render("weather.html", output = output, drink = drink)

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/home", HomeHandler),
        (r"/weather", WeatherHandler)
    ],
    debug = True,
    autoreload = True)

if __name__ == "__main__":
    app = make_app()
    port = 8080
    app.listen(port)
    print(f'Server is listening on port {8080}')
    # to start the server on the current thread
    tornado.ioloop.IOLoop.current().start()
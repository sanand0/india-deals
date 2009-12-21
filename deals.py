import wsgiref.handlers
from google.appengine.ext                 import webapp, db
from google.appengine.ext.webapp          import template




class Deal(db.Model):
    start_date  = db.DateProperty   ()
    end_date    = db.DateProperty   ()
    brand_image = db.StringProperty ()
    summary     = db.TextProperty   ()
    
class ShowDeals(webapp.RequestHandler):
    def get(self):
        deals = Deal.all().fetch(1000)
        self.response.out.write(template.render('show-deals.html', locals()))

class SingleDeal(webapp.RequestHandler):
    def get(self, id):
        deal = Deal.get_by_id(int(id))
        self.response.out.write(template.render('single-deal.html', locals()))
    
application = webapp.WSGIApplication([
        ('/',       ShowDeals),
        ('/(\d+)',  SingleDeal)
    ],
    debug=True)

wsgiref.handlers.CGIHandler().run(application)

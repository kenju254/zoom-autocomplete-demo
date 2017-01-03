#This initialized the application when app engine is initialized.

#TODO Remember to recheck if this part is still working and link it to the app
import zoomautocomplete
import config

app = zoomautocomplete.createapp(config)

##This only runs locally  and when in production it is run by gunicorn
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

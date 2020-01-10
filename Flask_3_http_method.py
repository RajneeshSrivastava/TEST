from flask import Flask, request

app=Flask(__name__)

@app.route('/')  # / defines the root directory
def index ():    #here index refers to root dir
    return 'Method used: %s' % request.method  # Default GET


@app.route('/Raj')#, methods=['GET','POST']) 
def Raj ():    
    if request.method == "GET":
        return 'My method is POST'
    else:
        return 'My method is GET'    

if __name__=="__main__":
    app.run(debug=True)


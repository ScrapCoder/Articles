from flask import Flask,render_template

app=Flask(__name__)




@app.route('/')
def home():
    posts=[{'title':"Fifa worldCup",'Content':"World Cup hosts Qatar were humbled by Ecuador on Sunday in the tournament opener as an Enner Valencia brace lifted Gustavo Alfaro's squad to a deserved 2-0 victory.",'Image':"img1.png" },
            {'title':"Expo re-opening",'Content':"Open since 1 October 2022, Expo City brings back many of the entertainment offerings that delighted visitors during the world-class exposition, including the flagship Al Wasl Plaza, Garden in the Sky observation tower and famed Surreal water feature.",'Image':"img2.webp"},
            {'title':"Antarctia News",'Content':"an underwater ecosystem was discovered in a river beneath the Larsen Ice Shelf in Antarctica. This discovery was made by New Zealand scientists when they drilled through the shelf and filmed the icy water below.",'Image':"img3.webp"},
            {'title':"Ronaldo’s love affair with Manchester United ends in messy divorce",'Content':"Dubai: The plan has worked. Cristiano Ronaldo – a serial winner everywhere he has played – has got his way and has won yet again. The Portuguese superstar had been rumoured to be seeking an exit from Manchester United ever since Erik Ten Hag was appointed the new coach in June. His situation at the club was like a ticking timebomb. That bomb has exploded but I don’t think it is United that are picking up the pieces.",'Image':"img4.jpg" }
    ]
    return render_template("home.html",posts=posts)

@app.route("/aboutme")
def aboutme():
    return render_template("about.html")

app.run(debug=True)
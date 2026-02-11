from flask import Flask, render_template_string

app = Flask(__name__)

# HTML for Page 1: Thanks for opening, ask if interested to go ahead
page1_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thanks for Opening!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #ffe6f2, #ffffff);
            color: #d63384;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 90%;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #ff1493;
        }
        p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .buttons {
            display: flex;
            justify-content: space-around;
            gap: 20px;
        }
        button {
            padding: 15px 30px;
            font-size: 1.2em;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.5s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        #yes-btn {
            background: linear-gradient(45deg, #ff69b4, #ffb6c1);
            color: white;
            transform: scale(1);
        }
        #no-btn {
            background: #f8f9fa;
            color: #d63384;
        }
        button:hover {
            transform: scale(1.1);
        }
        .heart {
            font-size: 3em;
            color: #ff1493;
            margin-bottom: 20px;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>Thanks for Opening!</h1>
        <p>It means the world to me. Are you interested to go ahead?</p>
        <div class="buttons">
            <button id="yes-btn">Yes 💕</button>
            <button id="no-btn">No</button>
        </div>
    </div>

    <script>
        let yesScale = 1;
        const yesBtn = document.getElementById('yes-btn');
        const noBtn = document.getElementById('no-btn');

        noBtn.addEventListener('click', () => {
            yesScale += 0.2;
            yesBtn.style.transform = `scale(${yesScale})`;
        });

        yesBtn.addEventListener('click', () => {
            window.location.href = '/next';
        });
    </script>
</body>
</html>
"""

# HTML for Page 2: Ask "Will you be my Valentine?" (with added heart animation on Yes)
page2_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Will You Be My Valentine?</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #ffe6f2, #ffffff);
            color: #d63384;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            animation: fadeIn 2s ease-in;
            overflow: hidden; /* Prevent scrolling during animation */
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 90%;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #ff1493;
        }
        p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .buttons {
            display: flex;
            justify-content: space-around;
            gap: 20px;
        }
        button {
            padding: 15px 30px;
            font-size: 1.2em;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.5s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        #yes-btn {
            background: linear-gradient(45deg, #ff69b4, #ffb6c1);
            color: white;
            transform: scale(1);
        }
        #no-btn {
            background: #f8f9fa;
            color: #d63384;
        }
        button:hover {
            transform: scale(1.1);
        }
        .heart {
            font-size: 3em;
            color: #ff1493;
            margin-bottom: 20px;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        .heart-anim {
            position: absolute;
            font-size: 30px;
            color: #ff1493;
            animation: floatUp 3s ease-in-out forwards;
        }
        @keyframes floatUp {
            0% {
                bottom: -50px;
                opacity: 1;
            }
            100% {
                bottom: 100vh;
                opacity: 0;
            }
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container" id="proposal">
        <div class="heart">❤️</div>
        <h1>Will You Be My Valentine?</h1>
        <p>I'm so glad you're here. What do you say?</p>
        <div class="buttons">
            <button id="yes-btn">Yes 💕</button>
            <button id="no-btn">No</button>
        </div>
    </div>
    <div class="container hidden" id="response">
        <h1 id="message"></h1>
    </div>

    <script>
        let yesScale = 1;
        const yesBtn = document.getElementById('yes-btn');
        const noBtn = document.getElementById('no-btn');
        const proposal = document.getElementById('proposal');
        const response = document.getElementById('response');
        const message = document.getElementById('message');

        noBtn.addEventListener('click', () => {
            yesScale += 0.2;
            yesBtn.style.transform = `scale(${yesScale})`;
        });

        yesBtn.addEventListener('click', () => {
            // Hide proposal and show response
            proposal.classList.add('hidden');
            response.classList.remove('hidden');
            message.textContent = "Yay! You're my Valentine! ❤️";

            // Trigger heart animation
            for (let i = 0; i < 20; i++) { // Create 20 hearts
                setTimeout(() => {
                    const heart = document.createElement('div');
                    heart.classList.add('heart-anim');
                    heart.textContent = '❤️';
                    heart.style.left = Math.random() * 100 + 'vw'; // Random horizontal position
                    heart.style.bottom = '-50px'; // Start from bottom
                    document.body.appendChild(heart);

                    // Remove heart after animation
                    setTimeout(() => {
                        heart.remove();
                    }, 3000);
                }, i * 100); // Stagger creation for flow effect
            }

            // Redirect to final page after animation (3 seconds)
            setTimeout(() => {
                window.location.href = '/final';
            }, 3000);
        });
    </script>
</body>
</html>
"""

# HTML for Page 3: Final "Yay!" page with thank you note, continue question, and scaling Yes button
final_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yay! You're My Valentine!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #ffe6f2, #ffffff);
            color: #d63384;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 90%;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #ff1493;
        }
        p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .buttons {
            display: flex;
            justify-content: space-around;
            gap: 20px;
        }
        button {
            padding: 15px 30px;
            font-size: 1.2em;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.5s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        #yes-btn {
            background: linear-gradient(45deg, #ff69b4, #ffb6c1);
            color: white;
            transform: scale(1);
        }
        #no-btn {
            background: #f8f9fa;
            color: #d63384;
        }
        button:hover {
            transform: scale(1.1);
        }
        .heart {
            font-size: 3em;
            color: #ff1493;
            margin-bottom: 20px;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>Yay! You're My Valentine! 💖</h1>
        <p>Thanks for choosing me. I'm grateful to have a partner like you in my life.</p>
        <p>Do you want to continue?</p>
        <div class="buttons">
            <button id="yes-btn">Yes 💕</button>
            <button id="no-btn">No</button>
        </div>
    </div>

    <script>
        let yesScale = 1;
        const yesBtn = document.getElementById('yes-btn');
        const noBtn = document.getElementById('no-btn');

        noBtn.addEventListener('click', () => {
            yesScale += 0.2;
            yesBtn.style.transform = `scale(${yesScale})`;
        });

        yesBtn.addEventListener('click', () => {
            window.location.href = '/continue';
        });
    </script>
</body>
</html>
"""

# HTML for Page 4: Continue page with updated note
continue_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Let's Continue!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #ffe6f2, #ffffff);
            color: #d63384;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 90%;
        }
        h1 { color: #ff1493; }
        .heart { font-size: 3em; animation: pulse 1.5s infinite; }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>Let's Continue Our Journey! 💕</h1>
        <p>Let's restart our journey as before with the same love and respect for each other 💕</p>
        <!-- Placeholder: Add images, text, or embeds here -->
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(page1_html)

@app.route('/next')
def next_page():
    return render_template_string(page2_html)

@app.route('/final')
def final_page():
    return render_template_string(final_page_html)

@app.route('/continue')
def continue_page():
    return render_template_string(continue_page_html)

if __name__ == '__main__':
    app.run(debug=True)
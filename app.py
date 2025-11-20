from flask import Flask, render_template_string

app = Flask(__name__)

THEME_BG = """
<div class="bg-anim-layer">
    <div class="gradient"></div>
</div>
<script>
    const bgLayer = document.querySelector('.bg-anim-layer') || document.body;
    const particleCount = 30;
    for (let i = 0; i < particleCount; i++) {
        let p = document.createElement("div");
        p.className = "particle";
        p.style.left = (Math.random() * 99) + "vw";
        p.style.width = p.style.height = (2 + Math.random()*4) + "px";
        p.style.animationDuration = (4 + Math.random() * 6) + "s";
        p.style.opacity = 0.28 + Math.random()*0.13;
        bgLayer.appendChild(p);
    }
    const objects = [
        { type: "emoji", char: "🚀" },
        { type: "emoji", char: "🟩" },
        { type: "emoji", char: "⛏️" },
        { type: "svg", svg: `<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect x='2' y='2' width='60' height='60' rx='11' fill='#5865F2'/><text x='50%' y='56%' font-size='29' text-anchor='middle' fill='white' font-family='Arial' dy='.3em'>N</text></svg>` }
    ];
    const flyCount = 12;
    for (let i = 0; i < flyCount; i++) {
        let obj = objects[Math.floor(Math.random() * objects.length)];
        let el = document.createElement("div");
        el.className = "flyobj";
        let x = Math.random();
        el.style.left = (x < 0.5 ? (Math.random()*18) : (82 + Math.random()*16)) + "vw";
        el.style.animationDelay = (Math.random() * 6) + "s";
        el.style.animationDuration = (7.5 + Math.random()*9) + "s";
        if (obj.type === "emoji") {
            el.innerText = obj.char;
        } else if (obj.type === "svg") {
            el.innerHTML = obj.svg;
        }
        bgLayer.appendChild(el);
    }
</script>
"""

THEME_CSS = """
<style>
    html, body {
        margin: 0;
        padding: 0;
        overflow: hidden;
        background: #06080f;
        font-family: Arial, sans-serif;
        height: 100%;
        width: 100vw;
    }
    .bg-anim-layer {
        position: fixed;
        left: 0; top: 0;
        width: 100vw; height: 100vh;
        pointer-events: none;
        z-index: 0;
    }
    .gradient {
        position: absolute;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #121a3a, #240046, #0e0d21);
        animation: bgshift 12s infinite alternate ease-in-out;
        opacity: 0.45;
    }
    @keyframes bgshift {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(40deg); }
    }
    @keyframes popFlyIn {
        0% { opacity:0; transform: scale(0.4) translateY(120px);}
        60% { opacity: 1; transform: scale(1.08) translateY(-20px);}
        80% { opacity: 1; transform: scale(0.95) translateY(0px);}
        100% { opacity: 1; transform: scale(1) translateY(0);}
    }
    .title {
        position: absolute;
        top: 22%;
        width: 100%;
        text-align: center;
        font-size: 80px;
        font-weight: bold;
        letter-spacing: 2px;
        color: white;
        opacity: 0;
        transform: scale(0.7) translateY(40px);
        animation: popFlyIn 1.2s cubic-bezier(.47,1.64,.41,.84) forwards;
        z-index: 2;
        animation-delay: 0.15s;
    }
    .nitro {
        color: #ff3b3b;
        text-shadow: 0 0 20px #ff3b3b, 0 0 40px #ff6969;
    }
    .express {
        color: #b66cff;
        text-shadow: 0 0 20px #b66cff, 0 0 40px #d5a6ff;
    }
    .tagline {
        position: absolute;
        top: 35%;
        width: 100%;
        text-align: center;
        font-size: 26px;
        color: #dcdcff;
        letter-spacing: 1px;
        opacity: 0;
        transform: scale(0.7) translateY(40px);
        animation: popFlyIn 1.2s cubic-bezier(.47,1.64,.41,.84) forwards;
        animation-delay: 0.75s;
        text-shadow: 0 0 12px #6a2cff50;
        z-index: 2;
    }
    .button-row {
        position: absolute;
        top: 48%;
        width: 100%;
        display: flex;
        justify-content: center;
        gap: 40px;
        opacity: 0;
        transform: scale(0.7) translateY(40px);
        animation: popFlyIn 1.2s cubic-bezier(.47,1.64,.41,.84) forwards;
        animation-delay: 1.3s;
        z-index: 2;
    }
    .btn {
        padding: 15px 45px;
        font-size: 20px;
        border-radius: 14px;
        backdrop-filter: blur(10px);
        background: rgba(255,255,255,0.05);
        border: 2px solid rgba(255,255,255,0.3);
        color: white;
        text-decoration: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .btn:hover {
        transform: scale(1.12);
        box-shadow: 0 0 25px rgba(255,255,255,0.7);
    }
    .discord-btn { border-color: #7289da; box-shadow: 0 0 12px #7289da50; }
    .buy-btn     { border-color: #00eaff; box-shadow: 0 0 12px #00eaff50; }
    .info-row {
        position: absolute;
        top: 65%;
        width: 100%;
        display: flex;
        justify-content: center;
        gap: 40px;
        opacity: 0;
        transform: scale(0.7) translateY(40px);
        animation: popFlyIn 1.2s cubic-bezier(.47,1.64,.41,.84) forwards;
        animation-delay: 1.85s;
        z-index: 2;
    }
    .info-box {
        width: 230px;
        padding: 18px 0;
        text-align: center;
        font-size: 20px;
        color: white;
        border-radius: 14px;
        backdrop-filter: blur(10px);
        background: rgba(255,255,255,0.04);
        border: 2px solid rgba(255,255,255,0.2);
        box-shadow: 0 0 15px #7a5cff40;
        transition: 0.3s;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 14px;
    }
    .info-box img {
        height: 30px; width: auto; margin-right: 4px;
        border-radius: 6px;
        background: #17062a;
        box-shadow: 0 0 5px #3c1d47;
    }
    .info-box:hover {
        transform: scale(1.09);
        box-shadow: 0 0 25px #b88cff80;
    }
    .particle {
        position: absolute;
        background: rgba(255,255,255,0.45);
        border-radius: 50%;
        animation: float linear infinite;
        z-index: 1;
    }
    @keyframes float {
        0% { transform: translateY(-10vh); }
        100% { transform: translateY(110vh); }
    }
    .flyobj {
        position: absolute;
        pointer-events: none;
        z-index: 1;
        animation: flyobjmove linear infinite;
        will-change: transform;
        font-size: 32px;
        user-select: none;
        opacity: 0.38;
        line-height: 1;
    }
    .flyobj svg {
        width: 28px; height: 28px;
        display: block;
    }
    @keyframes flyobjmove {
        0%   { transform: translateY(98vh) scale(0.96) rotate(-15deg); opacity: 0.36;}
        15%  { opacity: 0.42;}
        85%  { opacity: 0.42;}
        100% { transform: translateY(-101vh) scale(0.92) rotate(15deg); opacity:0.23;}
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .offers-page {
        position: relative;
        z-index: 3;
        max-width: 700px;
        margin: 60px auto 0 auto;
        background: rgba(35, 25, 66, 0.80);
        border-radius: 26px;
        border: 2px solid #b66cff22;
        box-shadow: 0 0 24px #06080fbb;
        padding: 30px 28px 34px 28px;
    }
    .offers-title {
        text-align: center;
        font-size: 2.5rem;
        color: #e0cbff;
        margin-bottom: 30px;
        letter-spacing: 1px;
        text-shadow: 0 0 8px #b66cff80;
    }
    .offers-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 1.15rem;
        color: #fff;
        margin-bottom: 32px;
    }
    .offers-table th, .offers-table td {
        padding: 16px 8px;
        text-align: left;
        font-family: inherit;
    }
    .offers-table th {
        background: #2b145d77;
        color: #ffb2fc;
        font-size: 1.1rem;
    }
    .offers-table tr {
        border-bottom: 1px solid #6a48b555;
    }
    .offers-table tr:last-child { border-bottom: none; }
    .offers-table td.price {
        font-weight: bold;
        color: #7bfc98;
        font-size: 1.18rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .offers-table .money-img {
        height: 25px; width: 25px; vertical-align: middle; margin-left: 2px;
        filter: drop-shadow(0 0 5px #7bfc9870);
    }
    .home-link {
        display: block;
        width: max-content;
        margin: 32px auto 0 auto;
        background: #b66cff25;
        color: #d6b4ff;
        text-decoration: none;
        font-size: 1.18rem;
        padding: 14px 36px;
        border-radius: 12px;
        border: 2px solid #7a5cff44;
        box-shadow: 0 0 8px #b66cff40;
        transition: 0.18s;
        text-align: center;
    }
    .home-link:hover {
        background: #d5a6ff65;
        color: #2a004d;
        box-shadow: 0 0 19px #b66cff55;
        border: 2px solid #b66cff88;
    }
</style>
"""

@app.route("/")
def index():
    return render_template_string(f"""
    <html>
    <head>
        {THEME_CSS}
    </head>
    <body>
        {THEME_BG}
        <audio id="bgmusic" autoplay loop>
          <source src="/static/phonk-music-phonk-2025-432208.mp3" type="audio/mpeg">
        </audio>
        <script>
            const music = document.getElementById('bgmusic');
            function startMusic() {{
                music.play();
                document.removeEventListener('click', startMusic);
                document.removeEventListener('keydown', startMusic);
            }}
            document.addEventListener('click', startMusic);
            document.addEventListener('keydown', startMusic);
        </script>
        <div class="title">
            <span class="nitro">Nitro</span><span class="express">Express</span>
        </div>
        <div class="tagline">Fast • Affordable • Reliable</div>
        <div class="button-row">
            <a class="btn discord-btn" href="https://discord.gg/Yyst4YhtSa" target="_blank">Our Discord</a>
            <a class="btn buy-btn" href="https://nitroexpressshop.mysellauth.com/" target="_blank">Auto Buy</a>
            <a class="btn" style="border-color:#ff99ec;box-shadow:0 0 12px #ffb6fc50;" href="/offers">Products</a>
        </div>
        <div class="info-row">
            <div class="info-box">
                <img src="/static/vouches.png" alt="Vouches"> 200+ Vouches
            </div>
            <div class="info-box">
                <img src="/static/customers.png" alt="Customers"> 99% Satisfied Customers
            </div>
            <div class="info-box">
                <img src="/static/trusted.png" alt="Trusted"> Trusted & Premium
            </div>
        </div>
    </body>
    </html>
    """)

@app.route("/offers")
def offers():
    return render_template_string(f"""
    <html>
    <head>
        {THEME_CSS}
    </head>
    <body>
        {THEME_BG}
        <div class="offers-page">
            <div class="offers-title">Products</div>
            <table class="offers-table">
                <tr>
                    <th>Product</th>
                    <th>Duration/Type</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <td>Discord Nitro Account</td>
                    <td>1 Month</td>
                    <td class="price">$0.60 <img src="/static/money.png" class="money-img" alt="Money"></td>
                </tr>
                <tr>
                    <td>Discord Nitro Account</td>
                    <td>3 Months</td>
                    <td class="price">$2.00 <img src="/static/money.png" class="money-img" alt="Money"></td>
                </tr>
                <tr>
                    <td>Discord Nitro Gift Link</td>
                    <td>3 Months</td>
                    <td class="price">$4.80 <img src="/static/money.png" class="money-img" alt="Money"></td>
                </tr>
                <tr>
                    <td>Minecraft Premium Full Access Account</td>
                    <td>Lifetime</td>
                    <td class="price">$6.00 <img src="/static/money.png" class="money-img" alt="Money"></td>
                </tr>
            </table>
            <a class="home-link" href="/">← Back to Home</a>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)

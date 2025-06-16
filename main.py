from fasthtml.common import *
import josh

# Create the FastHTML app
app, rt = fast_app()

# Custom CSS for colorful styling
css = """
<style>
    body {
        background:#000;
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        min-height: 100vh;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .header {
        text-align: center;
        color: white;
        margin-bottom: 40px;
        animation: fadeInDown 1s ease-out;
    }

    .header h1 {
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .colorful-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }

    .color-box {
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .color-box:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }

    .red { background: linear-gradient(45deg, #ff6b6b, #ee5a52); }
    .blue { background: linear-gradient(45deg, #4ecdc4, #44a08d); }
    .purple { background: linear-gradient(45deg, #a8edea, #fed6e3); color: #000; }
    .orange { background: linear-gradient(45deg, #ffa726, #ff7043); }
    .green { background: linear-gradient(45deg, #66bb6a, #43a047); }
    .pink { background: linear-gradient(45deg, #f06292, #e91e63); }

    .button {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 10px;
    }

    .button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }

    .stats {
        display: flex;
        justify-content: space-around;
        text-align: center;
        margin: 30px 0;
    }

    .stat-item {
        color: white;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        display: block;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .pulse {
        animation: pulse 2s infinite;
    }
</style>
"""


@rt("/joshua")
def get():
    return Titled("Joshua's first Website",
        Head(
            NotStr(css),
            Meta(name="viewport", content="width=device-width, initial-scale=1")
        ),
        Div(
            Div(
                H1("Welcome to My Colorful Website!", cls="pulse"),
                P("Built with FastHTML - Modern Python Web Development"),
                cls="header"
            ),

            Div(
                H2("About This Site", style="color: #66bb6a; text-align: center;"),
                P("This is a one of the best websites ever! Using FastHTML, to format make my website the abosolute best. "
                  "FastHTML combines the power of Python with modern web development practices.", 
                  style="font-size: 1.1rem; line-height: 1.6; color: #290;"),
                cls="card"
            ),
            H2("More About Me😎", style="color: #66bb6a; text-align: center; margin-top: 2rem;"),
            Div(
                Div("Josh is 🔥", cls="color-box red"),
                Div("A real 💎 in the rough", cls="color-box blue"),
                Div("insanely fast 😵‍💫", cls="color-box purple"),
                Div("A real piece of 🎨", cls="color-box orange"),
                Div("✨ Best to try ✨", cls="color-box pink"),
                cls="colorful-grid"
            ),

            Div(
                H2("Quick Stats", style="color: #ffa726; text-align: center;"),
                Div(
                    Div(
                        Span("100%", cls="stat-number"),
                        Span(" Python Powered")
                    , cls="stat-item"),
                    Div(
                        Span("1", cls="stat-number"),
                        Span(" Joshua")
                    , cls="stat-item"),
                    Div(
                        Span("∞", cls="stat-number"),
                        Span(" Possibilities")
                    , cls="stat-item"),
                    cls="stats"
                ),
                cls="card"
            ),

            Div(
                H2("You've reached the End", style="color: #89CFF0; text-align: center;"),
                P("Goodbye for Now 🤓", 
                  style="text-align: center; font-size: 1.1rem; color: #6F8FAF;"),
                Div(
                    A("View Source", href="#", cls="button"),
                    A("Learn More", href="#", cls="button"),
                    A("Deploy Now", href="#", cls="button"),
                    style="text-align: center;"
                ),
                cls="card"
            ),

            cls="container"
        )
    )

@rt("/api/colors")
def get_colors():
    """API endpoint that returns color data"""
    colors = [
        {"name": "Vibrant Red", "hex": "#ff6b6b", "rgb": "255, 107, 107"},
        {"name": "Ocean Blue", "hex": "#4ecdc4", "rgb": "78, 205, 196"},
        {"name": "Sunset Orange", "hex": "#ffa726", "rgb": "255, 167, 38"},
        {"name": "Forest Green", "hex": "#66bb6a", "rgb": "102, 187, 106"},
        {"name": "Royal Purple", "hex": "#a8edea", "rgb": "168, 237, 234"},
        {"name": "Pink Rose", "hex": "#f06292", "rgb": "240, 98, 146"}
    ]
    return colors

if __name__ == "__main__":
    serve()
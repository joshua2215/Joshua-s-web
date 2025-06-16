from fasthtml.common import *
app, rt = FastHTML()
def joshPage():
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
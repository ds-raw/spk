from dash import html
import dash_bootstrap_components as dbc



def create_navbar():
    navbar = dbc.NavbarSimple(
        
        children=[
            dbc.NavItem(dbc.NavLink("Dataset", href="/Dataset")),  # Additional menu item 1
            dbc.NavItem(dbc.NavLink("Distribution", href="/Distribution")),  # Additional menu item 2
            dbc.NavItem(dbc.NavLink("Geospatial", href="/Geospatial")),
            dbc.NavItem(dbc.NavLink("Relationship", href="/Relationship")),
            dbc.NavItem(dbc.NavLink("Cluster Count", href="/Cluster")),
            dbc.NavItem(dbc.NavLink("Prediction", href="/Prediction")),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-github"),  # Font Awesome Icon
                        " "  # Text beside icon
                    ],
                    href="[YOUR GITHUB PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-medium"),  # Font Awesome Icon
                        " "  # Text beside icon
                    ],
                    href="[YOUR MEDIUM PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-linkedin"),  # Font Awesome Icon
                        " "  # Text beside icon
                    ],
                    href="[YOUR LINKEDIN PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Dataset", href='/Dataset'),
                    dbc.DropdownMenuItem("Page 3", href='/page3'),
                ],
            ),
            
        ],
      
        brand='Home',
        brand_href="/",
        sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar

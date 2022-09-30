from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render
from dataclasses import dataclass
from typing import Dict, List
from shutil import ReadError
@dataclass
class Team:
    name: str
    people: list[str]
    description: str

def bcca_view(request,):
    pear = {
        "teams": ["Community", "Documentation", "Procurement", "Management"],
    }
    return render(request, "bcca.html", pear)

def bcca_team(request,input):
    mango = {
        "orange": input,
        "Community": Team(
            "Community Team",
            ["Amber", "JW", "Eric", "Angela", "Joshua", "Malcolm"], 
            "The BCCA Community Team is responsible for coordinating with businesses and other students to plan events."
        ),
        "Documentation": Team(
            "Documentation Team",
            ["Cannon", "Gabbi", "Antonio", "Cooper", "Colt", "Isaiah"],
            "The BCCA Documentation Team is responsible for taking pictures and running the program's social media"
        ),
        "Management": Team(
            "Management Team",
            ["Kevin", "Chevy", "Lukas", "Brooks", "Errin", "Andrew"],
            "The BCCA Management Team is responsible for coordinating with other students and staff to get things needed or planned to keep the program running."
        ),
        "Procurement": Team(
            "Procurement Team",
            ["River", "Dylan", "Anna", "Zual", "Mike", "Luke"],
            "The BCCA Procurement Team is responsible for planning, buying, cooking, and serving lunch to the other students."
        ),
    }
    return render(request, "stuff.html", mango)
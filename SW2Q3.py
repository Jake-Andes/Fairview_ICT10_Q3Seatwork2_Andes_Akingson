from pyscript import document  # type: ignore

def adding_numbers(e=None):
    out = document.getElementById("output1")
    grade = document.getElementById("num1").value
    section = document.getElementById("num2").value

    clinic_el = document.querySelector('input[name="clinic"]:checked')
    online_el = document.querySelector('input[name="online"]:checked')
    clinic = clinic_el.value if clinic_el else "no"
    online = online_el.value if online_el else "no"

    if grade == "":
        out.innerText = "Please select a grade level."
        return
    if section == "":
        out.innerText = "Please select a section."
        return

    # simple team assignment (based on section)
    if section == "Topaz":
        team = "Blue Bears"
    elif section == "Ruby":
        team = "Yellow Tigers"
    elif section == "Emerald":
        team = "Green Hornets"
    elif section == "Sapphire" or section == "Jade":
        team = "Red Bulldogs"
    else:
        team = "Unassigned"

    # eligibility logic (simple if / else)
    if clinic == "yes" and online == "yes":
        status = "Eligible for intramurals."
    elif clinic == "yes" and online == "no":
        status = "Clinic slip OK — online registration missing."
    elif clinic == "no" and online == "yes":
        status = "Online registration OK — clinic slip missing."
    else:
        status = "Not eligible — clinic slip and online registration missing."

    # image per team
    team_images = {
        "Blue Bears": "https://cdn.discordapp.com/attachments/1146819570447962162/1466262644762869953/Screenshot_2026-01-29_at_10.00.47_AM.png?ex=697c1b00&is=697ac980&hm=a68a16561f3635b152b96997e0c7285c7da6012a918a6c0ef08d2e83fce16575&",
        "Yellow Tigers": "https://cdn.discordapp.com/attachments/1273757083979878461/1466262276180017253/Screenshot_2026-01-29_at_10.00.23_AM.png?ex=697c1aa8&is=697ac928&hm=3432957c9514d4c7b37acfb71f2cb877945d593f8f93b9bc4b23f0ce47f15823&",
        "Green Hornets": "https://cdn.discordapp.com/attachments/1146819570447962162/1466262644515279022/Screenshot_2026-01-29_at_10.00.39_AM.png?ex=697c1b00&is=697ac980&hm=342ddeaca2322d87f1998b6e9a5abc0f6b2b6bf01e6c59a9714c1fc7b106c5cb&",
        "Red Bulldogs": "https://cdn.discordapp.com/attachments/1146819570447962162/1466262644267680078/Screenshot_2026-01-29_at_10.00.32_AM.png?ex=697c1b00&is=697ac980&hm=c3645583a726a48c0595a2a5c9da250d27100723b0f5872603a8161b99caa970&",
        "Unassigned": "https://via.placeholder.com/160x100.png?text=No+Team"
    }
    img = team_images.get(team, team_images["Unassigned"])

    # display image and text
    out.innerHTML = (
        f"<div style='display:flex;flex-direction:column;align-items:center;gap:8px;'>"
        f"<img src=\"{img}\" alt=\"{team}\" style='max-width:200px;border-radius:8px;border:1px solid rgba(0,0,0,0.06);'>"
        f"<div style='font-weight:700;color:var(--gold);'>Grade {grade} - {section} ({team})</div>"
        f"<div>{status}</div>"
        f"</div>"
    )

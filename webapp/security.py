USERS = {
    "editor": "editor",
    "viewer": "viewer"
}

GROUPS = {"editor": ['group:editor']}


def groupfinder(user_id, request):
    if user_id in USERS:
        return GROUPS.get(user_id, [])
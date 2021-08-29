from pwd import getpwall

def fetch_users():
    users = []

    for user in getpwall():
        # restrict to users which are not system accounts
        # see: https://www.redhat.com/sysadmin/user-account-gid-uid
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:
            users.append({
                'home': user.pw_dir,
                'id': user.pw_uid,
                'name': user.pw_name,
                'shell': user.pw_shell
            })

    return users


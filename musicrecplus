'''
Name: Abhishek Desai,Jianfei Li
CWID: 10464843,10479299
CS515 - Music Recommendation System
'''
constant_file_name = "musicrecplus.txt"
# Written by Jianfei Li
def main():
    """The file's main purpose. The users are loaded from the musicrecplus.txt file first, and then the user is prompted for his or her name. If the user is new, it is then asked for their preferences."""
    usermap = load_users(constant_file_name)
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if username not in usermap:
        enter_preferences(username, usermap, constant_file_name)
    menu(username, usermap)
# Written by Jianfei Li
def load_users(file_name):
    """The users and their preferences are loaded from a text document"""
    try:
        file = open(constant_file_name, 'r')
    except:
        file = open(constant_file_name, 'w')
        usermap = {}
        file.close
        return usermap
    usermap = {}   
    for line in file:
        username, artists = line.strip().split(':')
        artists = artists.split(',')
        usermap[username] = artists
    file.close()
    return usermap
# Written by Abhishek Desai
def enter_preferences(name, usermap, file_name):
    """Gets the user's preferences and saves them. Will rewrite any user preferences in the database."""
    preferences = []
    new_pref = input("Enter an artist that you like (Enter to finish):")
    while new_pref != '':
        preferences.append(new_pref)
        new_pref = input("Enter an artist that you like (Enter to finish):")
    preferences.sort()
    save(name, usermap, file_name, preferences)
# Written by Abhishek Desai
def save(name, usermap, file_name, prefs):
    """Users and their preferences are saved in a text document"""
    usermap[name] = prefs
    file = open(file_name, 'w')
    new_user_list = []
    for name in usermap:
        new_user_list.append(name)
        new_user_list.sort()
    for user in new_user_list:
        new_line = str(user) + ':' + ','.join(usermap[user]) + '\n'
        file.write(new_line)
    file.close
# Written by Jianfei Li
def menu(name, usermap):
    """This is a function for the program's menu. Prints the menu and then moves on to the next step based on the user's selection"""
    while True:
        print('Enter a letter to choose an option:' + '\n' +
            'e - Enter preferences' + '\n' + 
            'r - Get recommendations' + '\n' +
            'p - Show most popular artists' + '\n' +
            'h - How popular is the most popular' +'\n' +
            'm - Which user has the most likes' + '\n' + 
            'q - Save and quit')
        choice = input()
        if choice == 'e':
            enter_preferences(name, usermap, constant_file_name)
        elif choice == 'r':
            recs = get_recommendations(name, usermap)
            print_recommendations(recs, name)
            prefs = usermap[name]
            save(name, usermap, constant_file_name, prefs)
        elif choice == 'p':
            best_artists(usermap)
        elif choice == 'h':
            how_popular(usermap)
        elif choice == 'm':
            most_likes(usermap)
        elif choice == 'q':
            try:
                save(name, usermap, constant_file_name, usermap[name])
                break
            except:
                break  
# Written by Abhishek Desai
def num_matches(L1, L2):
    """Returns the amount of entries that are shared across the two lists"""
    L1.sort()
    L2.sort()
    matches = i = j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            matches += 1
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1
    return matches
# Written by Abhishek Desai
def drop_matches(L1, L2):
    """Returns a new list containing only the elements from list 2 that do not appear in list 1"""
    L1.sort()
    L2.sort()
    i = j = 0
    result = []
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            result.append(L2[j])
            j += 1
    while j < len(L2):
        result.append(L2[j])
        j += 1
    return result
# Written by Abhishek Desai
def remove_duplicates(L):
    """Creates a new list without any duplicates"""
    new_list = []
    for i in L:
        if i not in new_list:
            new_list.append(i)
    return new_list
# Written by Abhishek Desai
def get_recommendations(name, usermap):
    """Provides the user with a list of artist recommendations""" 
    users = usermap.keys()
    best_users = []
    best_score = 0
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        if usermap[user] != usermap[name]:
            current_prefs = usermap[user]
            main_prefs = usermap[name]
            matches = num_matches(current_prefs, main_prefs)
            if matches > best_score:
                best_score = matches
                best_users = [user]
            elif matches == best_score:
                best_users.append(user)
    new_list = []
    for user in best_users:
        new_list += drop_matches(usermap[name], usermap[user])
    rec_list = remove_duplicates(new_list)
    rec_list.sort()
    return rec_list
# Written by Abhishek Desai
def print_recommendations(recs, name):
    """Output each artist from the list of recommendations"""
    if len(recs) == 0:
        print('No recommendations available at this time')
    else:
        for artist in recs:
            print(artist)
# Written by Jianfei Li
def count_occurences(name, L):
    """Counts the number of times an artist appears in a list"""
    count = 0
    for artist_name in L:
        if name == artist_name:
            count += 1
    return count
# Written by Jianfei Li
def best_artists(usermap):
    """Returns the most popular artist among users"""
    all_artists = []
    users = usermap.keys()
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        all_artists += usermap[user]
    all_artists.sort()
    top_likes = 0
    top_artist = []
    for artist in all_artists:
        likes = count_occurences(artist, all_artists) 
        if likes > top_likes:
            top_likes = likes
            top_artist = [artist]
        elif likes == top_likes:
            top_artist.append(artist)
    top_artist.sort()
    best_artist = remove_duplicates(top_artist)
    if len(best_artist) == 0:
        print('Sorry, no artists found')
    else: 
        for artist in best_artist:
            print(artist)
# Written by Jianfei Li
def how_popular(usermap):
    """Output the number of likes the most popular artist received"""
    all_artists = []
    users = usermap.keys()
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        all_artists = all_artists + usermap[user]
    all_artists.sort()
    top_likes = 0
    for artist in all_artists:
        likes = count_occurences(artist, all_artists) 
        if likes > top_likes:
            top_likes = likes
    if top_likes == 0:
        print('Sorry, no artists found')
    else: 
        print(top_likes)
# Written by Jianfei Li
def most_likes(usermap):
    """Output the name of the user who likes the most artists"""
    users = usermap.keys()
    top_prefs = 0
    best_users = []
    for user in users:
        if user[-1] == '$':
            continue
        if usermap[user] == ['']:
            continue
        if len(usermap[user]) > top_prefs:
            top_prefs = len(usermap[user])
            best_users = [user]
        elif len(usermap[user]) == top_prefs:
            best_users.append(user)
    most_likes_users = remove_duplicates(best_users)
    if top_prefs == 0 or len(most_likes_users) == 0:
        print('Sorry, no user found')
    else:
        for user in most_likes_users:
            print(user)
    
if __name__ == '__main__':
    main()
    

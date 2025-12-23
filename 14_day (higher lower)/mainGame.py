import random
import os

# FUNCTION TO CLEAR SCREEN
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# DATA
celebrities = [
    {"name": "Selena Gomez", "follower_count": "417000000", "description": "Musician", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": "392000000", "description": "Reality TV personality", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": "354000000", "description": "Reality TV personality", "country": "United States"},
    {"name": "Kendall Jenner", "follower_count": "285000000", "description": "Model", "country": "United States"},
    {"name": "Beyonce", "follower_count": "309000000", "description": "Musician", "country": "United States"},
    {"name": "Taylor Swift", "follower_count": "281000000", "description": "Musician", "country": "United States"},
    {"name": "LeBron James", "follower_count": "158000000", "description": "Basketball Player", "country": "United States"},
    {"name": "Lionel Messi", "follower_count": "511152298", "description": "Football Player", "country": "Argentina"},
    {"name": "Cristiano Ronaldo", "follower_count": "669000000", "description": "Football Player", "country": "Portugal"},
    {"name": "Neymar Jr", "follower_count": "232000000", "description": "Football Player", "country": "Brazil"},
    {"name": "Tom Cruise", "follower_count": "15000000", "description": "Actor", "country": "United States"},
    {"name": "Elon Musk", "follower_count": "224000000", "description": "Businessman", "country": "United States"},
    {"name": "Bill Gates", "follower_count": "12000000", "description": "Businessman", "country": "United States"},
    {"name": "Jeff Bezos", "follower_count": "5000000", "description": "Businessman", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": "274000000", "description": "Cricketer", "country": "India"},
    {"name": "Ariana Grande", "follower_count": "373000000", "description": "Musician", "country": "United States"},
    {"name": "Khloe Kardashian", "follower_count": "300000000", "description": "TV Personality", "country": "United States"},
    {"name": "Narendra Modi", "follower_count": "100000000", "description": "Politician", "country": "India"},
    {"name": "Donald Trump", "follower_count": "39000000", "description": "Politician", "country": "United States"},
    {"name": "Barack Obama", "follower_count": "40000000", "description": "Politician", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": "396000000", "description": "Actor & Wrestler", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": "293000000", "description": "Musician", "country": "Canada"},
    {"name": "Katy Perry", "follower_count": "206000000", "description": "Musician", "country": "United States"},
    {"name": "Zendaya", "follower_count": "189000000", "description": "Actress", "country": "United States"},
    {"name": "Robert Downey Jr.", "follower_count": "110000000", "description": "Actor", "country": "United States"},
    {"name": "Chris Hemsworth", "follower_count": "110000000", "description": "Actor", "country": "Australia"},
    {"name": "Emma Watson", "follower_count": "75000000", "description": "Actress", "country": "United Kingdom"},
    {"name": "Shah Rukh Khan", "follower_count": "45000000", "description": "Actor", "country": "India"},
    {"name": "Salman Khan", "follower_count": "65000000", "description": "Actor", "country": "India"},
    {"name": "Akshay Kumar", "follower_count": "70000000", "description": "Actor", "country": "India"},
    {"name": "Chris Evans", "follower_count": "60000000", "description": "Actor", "country": "United States"},
    {"name": "Tom Holland", "follower_count": "70000000", "description": "Actor", "country": "United Kingdom"},
    {"name": "MrBeast", "follower_count": "57000000", "description": "YouTuber & Philanthropist", "country": "United States"},
    {"name": "Messi Jr Fan Page", "follower_count": "35000000", "description": "Fan Page", "country": "Argentina"},
    {"name": "David Beckham", "follower_count": "88000000", "description": "Football Legend", "country": "United Kingdom"},
    {"name": "Kylian Mbappe", "follower_count": "120000000", "description": "Football Player", "country": "France"},
    {"name": "Erling Haaland", "follower_count": "45000000", "description": "Football Player", "country": "Norway"},
    {"name": "Snoop Dogg", "follower_count": "85000000", "description": "Rapper", "country": "United States"},
    {"name": "Nicki Minaj", "follower_count": "230000000", "description": "Rapper", "country": "United States"},
    {"name": "Cardi B", "follower_count": "170000000", "description": "Rapper", "country": "United States"},
    {"name": "BLACKPINK Lisa", "follower_count": "102000000", "description": "Musician", "country": "Thailand"},
    {"name": "Jennie Kim", "follower_count": "82000000", "description": "Musician", "country": "South Korea"},
    {"name": "Virat Kohli Fanpage", "follower_count": "25000000", "description": "Fan Page", "country": "India"},
    {"name": "Hrithik Roshan", "follower_count": "50000000", "description": "Actor", "country": "India"},
    {"name": "Kriti Sanon", "follower_count": "55000000", "description": "Actress", "country": "India"},
    {"name": "Alia Bhatt", "follower_count": "93000000", "description": "Actress", "country": "India"},
    {"name": "Kareena Kapoor", "follower_count": "110000000", "description": "Actress", "country": "India"},
    {"name": "Rashmika Mandanna", "follower_count": "45000000", "description": "Actress", "country": "India"},
    {"name": "Allu Arjun", "follower_count": "40000000", "description": "Actor", "country": "India"},
    {"name": "Thalapathy Vijay", "follower_count": "35000000", "description": "Actor", "country": "India"},

]

# GAME FUNCTION
def play_game():
    score = 0
    game_running = True

    while game_running:
        celebA, celebB = random.sample(celebrities, 2)

        print(f"Side A: {celebA['name']}, a {celebA['description']} from {celebA['country']}")

        print('''
____   _________________________  _____________ ___  _________
\\   \\ /   /\\_   _____/\\______   \\/   _____/    |   \\/   _____/
 \\   Y   /  |    __)_  |       _/\\_____  \\|    |   /\\_____  \\ 
  \\     /   |        \\ |    |   \\/        \\    |  / /        \\
   \\___/   /_______  / |____|_  /_______  /______/ /_______  /
                   \\/         \\/        \\/                 \\/ 
        ''')

        print(f"Side B: {celebB['name']}, a {celebB['description']} from {celebB['country']}")

        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        a_followers = int(celebA["follower_count"])
        b_followers = int(celebB["follower_count"])

        if (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers):
            score += 1
            clear_screen()
            print(f"Correct! 🎯 Your Score: {score}\n")
        else:
            clear_screen()
            print(r"""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗
██║   ██║██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝
██║   ██║██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   
██║   ██║██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   
╚██████╔╝╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   
 ╚═════╝  ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   
            """)
            print(f"You Lost! ❌ Final Score: {score}\n")
            game_running = False

    again = input("Do you want to play again? (yes/no): ").lower()
    if again == "yes":
        clear_screen()
        play_game()
    else:
        print("\nThanks for playing 😊")

# START GAME
clear_screen()
play_game()


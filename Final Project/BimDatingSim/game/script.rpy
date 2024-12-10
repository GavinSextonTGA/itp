# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Bim"), color="#c858ff")
define f = Character(_("Me"), color="#2bd339")
define g = Character(_("Cheerleader"), color="#c858ff")
define h = Character(_("Nerd"), color="#c858ff")
define i = Character(_("School President"), color="#c858ff")
default meanie_bim = 0


# The game starts here.


label start:  
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
  
    play music backgroundtest volume 0.5

    scene placeholder_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "Its the day you've been waiting for, after years of applying you finally got into the college of your dreams: Kingsford College"
    "You've heard that the school is so prestegious that the prince himself even attends there"
    "You thought you would mostly keep to yourself and focus on your education, but for once you decided to try and go out and meet some people, who knows maybe you could find a date for the homecoming dance"
    "In the halls of Klingsford College you nervously wander the halls looking for anything to do as you weirdly haven't seen anyone to talk to, and you start wondering why a college hosts a homecoming dance anyway"
    "You hear some rather clumsy sounding footsteps growing closer"
    show  bim normal 
    with moveinright 
    e "HEYOOOOOOO!."
    f "..."
    f "... "
    f "... um hi-" 
   
    e "YOOOO! Its been a while since I've seen another student around here!"
    f "Yeah I'm new and I've kind of been looking for some people to talk to"
    "You take a second to catch your breath as you look at the handsome being in front of you. "
    "His mighty stature"
    "His strong Chin"
    "That impressive outfit he's wearing"
    "And of course that smile that instantly charms everyone it must show itself to"
    e "YOOOO thats so cool!"
    show bim_neutral
    e "Yeah all the orientation stuff they do is pretty lame, though the Bim coloring books are the best! They never quite get my hair right though"
    f "Wait I'm sorry you're THE Bim?" 
    show bim_kiss 
    with hpunch 
    e "The one and only"
    f "Wow um, guess its my lucky day!"
    menu:
        "What do you do?"
        "Make small talk":  
            $ meanie_bim += -1   
            jump enthusiasm
        "Question his... hair?":
            $ meanie_bim += 1
            jump insult
label insult:
    "You notice the pink leaf that encompasses his head and it confuses you"
    f "What even is that thing on you're head supposed to be?" 
    e "Oh you mean my luchious hair?"
    f "..."
    hide bim_neutral
    hide bim_kiss    
    show bim normal
    e "Many have been known to be buffudled at it but I assure you its harmless"
    f "...ok?"
    jump main1
label enthusiasm: 
    f "Wow tell me more about you" 
    e "Its a well kept secret but I'm a masterful sportsball player"
    f "Oh really?"
    hide bim_neutral
    hide bim_kiss
    show  bim normal 
    e "Yep! I bowl touchdowns almost every inning"
    f "Um how does that game work exacly?"
    e "I don't know tbh, but its SOOOOO much fun!"
    "you are enamored at his brilliant confidence"
    
    jump main1
label main1:
    menu:
        "What do you want to"
        "Ask about that fascinating jersey":
            $ meanie_bim += -1
            jump jersey 
        "Question why his shirt appears to be in... quite bad shape":
            $ meanie_bim += 1
            jump shirt
label jersey:
    f "Oh is that your Jersey?"
    e "YEEEP, always gotta rep the swag"
    e "My favorite thing about Sportsball is the team man"
    hide bim normal
    show bim_neutral
    e "well right now its only me.. but uh..."
    hide bim_neutral
    show bim normal
    e "We'll get some new guys in soon!"
    e "Would you do the great favor of playing some sportsball?"

    jump main2

label shirt:
    f "That shirt is it... ok??"
    show bim normal
    e "OK? This shirt is better than ever man, good as the year I got it"
    f "You've washed it at least right?"
    hide bim normal 
    show bim_neutral
    e "... whats that?"
    f "..."
    jump main2

label main2:
    "BEEEEEEEEEEEEEEP"
    hide bim bim_neutral
    hide bim_kiss 
    show bim normal
    e "Yo thats the bell, you got any orientation activities to do?"
    f "Yeah they're doing some tours of the outside courts. I figured I should show up"
    e "THATS RAD LITTLE GUY (gender neutral), Ima head to the caf to get some GRUB! IM HUNGRYYYY"
    hide bim normal 
    "You hurry outside to get to the tour"
    jump outside
    
label outside:
    scene black
    "Hurrying through the hall you think of the character you had encountered, he was certainly very unlike any person you had encountered before in your life"
    if meanie_bim <= 0:
        "you couldn't wait to see him again"
    else:
        "you felt uncomfortable with the interaction you had, but you hope maybe you could find someone more... normal"
    scene outside
    "You make it outside just on time, but again you are concerned as you didn't really see anyone in the hallway"
    show bimcheer_shadow
    "You do see someone who seems to be waiting by the court, with their back turned"
    "You decide to tap their shoulder"
    hide bimcheer_shadow

    show bimcheer
    g "OH MY GAWSH u like startled me little guy! How are you doing? I don't think we've met have we?"
    f "... uh I'm doing good... I think?"
    g "Its ok you can talk a little louder, you don't got to use your inside voice"
    if meanie_bim <= 0:
        menu:
            "What will you do?"
            "Oh um, sorry, whats your name?":
                $ meanie_bim += -1
                jump nicecheer
            "Is that you bim?":
                jump isthatbim
    else:
        menu:
            "What will you do?"
            "Oh um, sorry, whats your name?":
                $ meanie_bim += -1
                jump nicecheer
            "Ugh, is that you Bim? Why the hell are you here":
                jump meancheer
label nicecheer:
    e "OHHH, ma name is Biiim!!! Whats your name cutie?"
    f "Oh well my name is---"
    jump outside2
label isthatbim:
    "YEAH, ... wait how'd you know that I don't know you cutie---}"
    jump outside2
label meancheer:
    show bimcheer_neutral
    e "... yeah, ... wait how'd you know that I don't know you---"
    jump outside2
label outside2:
    scene black
    "THUNK"
    scene outside 
    show bimcheer_nobat
    e "OH MY GAWSH I'M SORRYZ, I dropped my baseball bat!"
    "Bim's massive bat fell to the floor and it shook the planet! ... how were they holding that up...?"
    f "Its no problem it just scared me a bit "
    if meanie_bim < 0:
        "He sure is clumsy but Bim must be jacked in order to carry such an impressibe club"
    f "so... you're on the sportsball team right?"
    e "Oh god no!! With my clumsy fists I could neverrr, I just cheer"
    if meanie_bim > 0:
        "What in gods name is going on here?"
    menu: 
        "What will you do?"
        "Ask Bim about cheer":
            $ meanie_bim += -1
            jump cheercheer
        "Insult bim":
            $ meanie_bim += 1
            jump insultcheer
label cheercheer:
    f "What do you do in cheer?"
    e "Oh I just kinda throw this here pom pom thing aroud as you do! Luckily it aint as heavy as that there bat I was holdin'"
    f "Thats cool! Do you know when I can see you next"
    show bimcheer_nobat_kiss
    e "Well the big game of course ya silly!"
    f "Oh right I forgot, and there's the dance after as well"
    hide bimcheer_nobat_kiss
    show bimcheer_nobat
    e "Right! I don't really go nobody for that right now but I'm sure I'll find somebody to go with me"
    f "Yeah, good luck with that!"
    jump outside3
label insultcheer:
    f "That outfit doesn't fit bim, you look gross"
    e "GROSS AS HELL MAN! I gotta keep up with all of this slang yall have been using it's really confusin me"
    f "uhuh"
    jump outside3
label outside3:
    "BEEEEEEEEP"
    f "Wait its time for the next thing already? Why does this place have 5 minute periods?"
    e "I don't know many they got a lot to do I guess"
    e "I'll see ya tho!"
    scene black 
    "You try to hurry on to your next activity, but your schedule doesn't make sense."
    "It doesn't say you have anything to do for the rest of the day, but the day ends in an hour"
    "confused you find yourself in a random classroom to pass the time"

    jump studyhall

label studyhall:
    scene studyhall
    f "This place should do I guess"
    show bimnerd
    if meanie_bim > 0:
        "you've gotta be kidding me"
    else:
        "huh?"
    h "YOOOO WHASSUP GAMER!"
    if meanie_bim <= 0:
        menu:
            "What will you do?"
            "Hi! You startled me there!":
                $ meanie_bim += -1
                jump nerdhi
            "Is that you again bim?":
                jump nerdbim
    else:
        f "WHAT ARE YOU DOING HERE?"
        h "erm what do you mean frie-----{nw}"
        f "Were you following me??? It doesn't make sense why is EVERYONE Bim!!!!"
        "..."
        h "Hey how'd you know my name, have we met before?"
        f "How many Bim's are there??? What is this school?"
        e "I don't think theres any other me's than just me haha"
        f "LIES, NONE OF THIS MAKES ANY SENSE"
        "Attention students, it has come to my attention that the new student has been harassing the current students, New student, could you please make your way to the principal's office immediately, thank you"
        e "Uhm, I guess you should go..."
        f "Yeah whatever Bim"
        scene black
        "You stomp over to the Principal's office enraged, surely something strange has been going on and you are going to tell this principal whats what"
        "Before today you had only dreamed of meeting the famed prince, but after today you hope that this nightmare will end"
        "You make yourself to the office and open the door"
        jump office 
label nerdhi:
    e "Sup, name's Bim, I'm hiding in here working on my new video game since there's nothing left for orientation"
    jump main3
label nerdbim:
    e "Yep, thats my name, I'm hiding in here working on my new video game since there's nothing left for orientation"
    jump main3
label main3:
    f "Yeah I had the same problem with the schedule, it's really confusing"
    e "Its so weeeird man, luckily I have this to keep me busy"
    f "Whats the game you're working on about?"
    e "Oh its a sportsball batting simulator, you see I'm a massive sportsball fan!"
    f "Thats cool! Is that thing on your back a bat from it?"
    e "YEAH, I see you've noticed it, Its pretty rad right!?!"
    "His great confidence"
    "His awesome collection"
    "His amazing intellect"
    "This is definitely the famed prince!"
    "BEEEEEEEEEP"
    f "I swear those bells are getting faster!"
    e "Yeah this school makes no sense ngl, super cool seing you tho!!"
    f "Same, I'll see you around!"
    jump thechoice
label thechoice:
    scene black 
    "You head home with thoughts swirling your head"
    "All of the attractive people you met throughout today"
    "The hunk, Bim"
    "The cheerleader, Bim"
    "And that super smart guy, Bim"
    "You've decided to make your choice now, you're going to ask someone out for the Homecoming dance after the Big Game"
    menu:
    
        "Who will you ask out to the dance?"
        "Bim":
            jump Bim
        "Bim":
            jump Bim
        "Bim":
            jump Bim
label Bim:
    "You decide to ask Bim out, he was the clear choice after all"
    "The following day goes without fail, after watching him star in the game demolishing the opposing college, you muster up your courage and ask the notorious Bim out on a date to the dance"
    "He says yes and Bim hits sick dance moves"
    "The End"
    return

label office:
    scene office
    i "Please, take a seat"
    "You look where the Principal's voice came from"
    f "It can't be"
    show bimprincipal
    e "Yes it is I, Bim, the principal of this fine school. I have called you here today for your rude behavior, do you have anything to say on your behalf?"
    "how...?"
    f "What has been going on here?"
    e "I see you won't answer my question, but I shall answer yours"
    e "You see my name is Bim"
    f "...uhuh"
    e "And I have this awesome baseball bat that I use for Sportsball"
    f "God Damn it "
    f "I give up"
    return

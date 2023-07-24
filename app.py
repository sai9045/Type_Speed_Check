from flask import Flask, render_template, url_for, request, redirect
import random
import time

global start, stop, l_list, text, l,t_len,p_len


L =['When a lion was resting in the jungle, a mouse began racing up and down his body for amusement. The lion’s sleep was interrupted, and he awoke enraged. The lion was going to eat the mouse when the mouse begged him to let him go. “I assure you, if you save me, I will be of immense help to you in the future.” The lion laughed at the mouse’s self-assurance and freed him.A group of hunters arrived in the forest one day and captured the lion. They had him tied to a tree. The lion began to roar as he struggled to get out. Soon, the mouse passed by and spotted the lion in distress. He dashed off, biting on the ropes to free the lion, and the two hurried off into the woods.', 'One day a wolf was eating the flesh of an animal it had killed. A little bone got stuck in his throat, and he was unable to swallow it. He soon felt severe pain in his throat and raced up and down, trying to find a way to ease it. He begged everyone he saw to help him. Finally, the wolf came face to face with the crane.“Please help me,” the wolf pleaded. “I’ll give you exactly what you want.The crane agreed to give it a shot and instructed the Wolf to lie down on its side with its jaws spread as wide as it could. The crane then inserted its long neck into the Wolf’s throat and pulled out the bone. The crane then requested its reward.', 'Probably the most popular English story for kids ever, Cinderella narrates the story of a beautiful orphaned girl. She lives with her step mother and step sisters who make her do all household chores. Till one day, there is a ballroom party to which Cinderella manages to go with little help from her fairy godmother. Host of the party, a prince, is smitten by her beauty and uses the glass shoe that she leaves behind to track her down and makes her his queen. Scroll down to enjoy the next story with moral in English. The villagers went muttering under their breath about how the boy had wasted their time when they discovered there was no wolf. The boy shouted out again the next day, “Wolf! Wolf!” and the villagers hurried over to chase the wolf away.', 'A boy and his father lived in a village. While the sheep grazed in the fields, the boy’s father instructed him to keep an eye on them. He had to take the sheep to the grassy fields every day. The boy, on the other hand, was dissatisfied and wanted to run and play.\xa0 He decided to have a good time. “Wolf! Wolf!” he yelled, and the entire village came storming with stones to chase the wolf away before it could eat any of the sheep. The villagers walked away enraged this time. On the third day, as the boy climbed the tiny hill, he came face to face with a wolf attacking his sheep. “Wolf! Wolf! Wolf!” he screamed as loudly as he could, yet not a single person came to his aid. The villagers assumed he was trying to trick them once more and did not come. That day, the small boy lost a lot of sheep due to his folly.', 'Once upon a time, there was a Greek King, Midas.He was very rich and had lots of Gold. He had a daughter, who he loved a lot.One day, Midas found an angel in need of help. He helped her and in return she agreed to grant a wish.Midas wished that everything he touched would turn into gold. His wish was grantedOn his way home, he touched rocks and plants and they turned into gold.As he reached home, in excitement he hugged his daughter, who turned into gold.Midas was devastated and he had learnt his lesson. Upon learning his lesson, Midas asked the angel to take his wish away.', 'This is an extremely popular story about a hare and a tortoise.The hare is an animal that is known to move quickly, while atortoise is one to move slowly.One day, the hare challenged the tortoise to a race simply to prove that he was the best. The tortoise agreed.Once the race began the hare was easily able to get a head start. Upon realizing that the tortoise is far behind. The overconfident hare decided to take a nap.Meanwhile the tortoise, who was extremely determined and dedicated to the race was slowly nearing the finish line.The tortoise won the race while the hare napped. Most importantly he did it with humility and without arrogance.', 'We stopped leaving the garage door open when we were cooking because I told my mom the police were saying criminals had been stealing equipment from garages. My dad was away on an engineering work contract in Dubai like half the Uncles I knew, so we kids were left to help our moms with everything from house maintenance to legal compliance. Back then there was no internet and overseas phone calls to Dubai were expensive, so there were a great many things left unreported to the dads. To compensate for this lack of communication, my mom and...', 'Alice was everywhere, until she wasn’t. Just like at first, she was nowhere until she was. The absence of her before I knew she existed, was nothing. Now, the absence of her shrouds everything. Like a guest who never came to dinner; a stormy sky that didn’t deliver. Nothing can wash away the void where she used to be. This is what I’m thinking about the first time I take The Walk without her.', 'A week later, on my morning run with Copper, I ran into Alice again and now we knew. This is where I see you! We both exclaimed it as we came into each other’s space on the trail, the wide, flat former track bed for trains. Copper panted at my side, not used to the interruption in our run. Alice was delighted. Although she didn’t run, I agreed to slow it to a power walk and changed direction, pulling a confused Copper along. The winds shifted: the weather and my life, simultaneously.', 'The Walk is so important, she’d tell me, but she didn’t have to tell me. I stopped running, and my knees responded with finally! For the love of God stop trying to break us, you aren’t young anymore! Alice, who I had flown by in summers before, barely noticing her, became my near daily companion and without the run, The Walk became essential. My knees, at age forty, were dissolving like broken concrete, but I still needed the exercise, and, as it turns out, the companionship.', 'But he doesn’t really have friends, you know? Alice observed, and I agreed. Richard was a perpetuator of vanity posting and humble brags, king of the selfie with #nofilter. In person, you could see the ruddy undertones of his skin and his bleached hair wasn’t quite so effervescent. His need to be complimented was painfully obvious, like a giant cut that oozed blood and begged for stitches.', 'But it wasn’t just work and Richard. We soon realized that we had both been at the wedding of Cassidy and Brian, who had also attended Richard’s party. Brian was a colleague of mine; I had known him for years. Cassidy was Alice’s neighbor before she married Brian. Both of us had frequently double-dated with them. Alice and the Zen husband who was placid like a golden retriever on tranquilizers. Me and David, before he died.'] 
l=""
test_list=[]
app = Flask(__name__)

@app.route('/')
def home():
    global start, stop, l_list, l
    start = time.time()
    l = random.choice(L)
    l_list = l.split(' ')
   
    return render_template("home.html")

@app.route('/play', methods=['POST', 'GET'])
def play():
    global stop, start, L, text, l,t_len,p_len

    text = request.form.get('text_typed')
    
    stop = time.time()
    if text is not None:
        return redirect(url_for('check_results'))
    return render_template("play.html", l=l)

@app.route('/Check_the_results')
def check_results():
    global start, stop, l_list, text,t_len,p_len

    text_list = text.split()
    count = 0
    for i in text_list:
        if i in l_list:
            count = count + 1
    accuracy = count / len(l_list)
    total_time_taken = stop - start
    total_time_taken_min = total_time_taken / 60
    total_time_taken_min_round = round(total_time_taken_min)
    speed = len(text_list) / total_time_taken_min
    speed_round = round(speed)
    accuracy_100 = accuracy * 100
    accuracy_100_round=round(accuracy_100,1)
 d)

    return render_template("check_r.html", accuracy=accuracy_100_round, total_time_taken=total_time_taken_min_round,
                           speed=speed_round,)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 30
data = [
	{
		"id": 1,
		"title": "Affinity",
		"author": "Sarah Waters",
		"num_fans":20599,
		"topics":{"fiction": True, "Victorian":True , "England":True, "prison":True}, 
		"summary":"An upper-class woman recovering from a suicide attempt, Margaret Prior has begun visiting the women’s ward of Millbank prison, Victorian London’s grimmest jail, as part of her rehabilitative charity work. Amongst Millbank’s murderers and common thieves, Margaret finds herself increasingly fascinated by an apparently innocent inmate, the enigmatic spiritualist Selina Dawes. Selina was imprisoned after a séance she was conducting went horribly awry, leaving an elderly matron dead and a young woman deeply disturbed. Although initially skeptical of Selina’s gifts, Margaret is soon drawn into a twilight world of ghosts and shadows, unruly spirits and unseemly passions, until she is at last driven to concoct a desperate plot to secure Selina’s freedom, and her own.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/71w8Y4fGQZL.jpg"
	},
	{
		"id": 2,
		"title": "The Sweetest Fruits",
		"author": "Monique Truong",
		"num_fans":2340,
		"topics":{"fiction": True, "Hearn": True, "writer": True, "Japan": True}, 
		"summary": "A Greek woman tells of how she willed herself out of her father's cloistered house, married an Irish officer in the British Army, and came to Ireland with her two-year-old son in 1852, only to be forced to leave without him soon after. An African American woman, born into slavery on a Kentucky plantation, makes her way to Cincinnati after the Civil War to work as a boarding house cook, where in 1872 she meets and marries an up-and-coming newspaper reporter. In Matsue, Japan, in 1891, a former samurai's daughter is introduced to a newly arrived English teacher, and becomes the mother of his four children and his unsung literary collaborator.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/91VFglFE3yL.jpg"
	},
	{
		"id": 3,
		"title": "A Gentleman in Moscow",
		"author": "Amor Towles",
		"num_fans":228633,
		"topics":{"fiction": True, "Metropol": True, "waiter": True}, 
		"summary": "In 1922, Count Alexander Rostov is deemed an unrepentant aristocrat by a Bolshevik tribunal, and is sentenced to house arrest in the Metropol, a grand hotel across the street from the Kremlin. Rostov, an indomitable man of erudition and wit, has never worked a day in his life, and must now live in an attic room while some of the most tumultuous decades in Russian history are unfolding outside the hotel's doors. Unexpectedly, his reduced circumstances provide him entry into a much larger world of emotional discovery.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/A1fs-ErenkL.jpg"
	},
	{
		"id": 4,
		"title": "Little Women",
		"author": "Louisa May Alcott",
		"topics":{"fiction": True, "Massachusetts": True, "girlhood": True}, 
		"num_fans":1568802,
		"summary": "Generations of readers young and old, male and female, have fallen in love with the March sisters of Louisa May Alcott’s most popular and enduring novel, Little Women. Here are talented tomboy and author-to-be Jo, tragically frail Beth, beautiful Meg, and romantic, spoiled Amy, united in their devotion to each other and their struggles to survive in New England during the Civil War.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51CbUZ70s1L._SX355_BO1,204,203,200_.jpg"
	},
	{
		"id": 5,
		"title": "Villette",
		"author": "Charlotte Bronte",
		"num_fans":57357,
		"topics":{"fiction": True, "romance": True, "school": True}, 
		"summary": "With her final novel, Villette, Charlotte Brontë reached the height of her artistic power. First published in 1853, Villette is Brontë's most accomplished and deeply felt work, eclipsing even Jane Eyre in critical acclaim. Her narrator, the autobiographical Lucy Snowe, flees England and a tragic past to become an instructor in a French boarding school in the town of Villette. There she unexpectedly confronts her feelings of love and longing as she witnesses the fitful romance between Dr. John, a handsome young Englishman, and Ginerva Fanshawe, a beautiful coquette. The first pain brings others, and with them comes the heartache Lucy has tried so long to escape. Yet in spite of adversity and disappointment, Lucy Snowe survives to recount the unstinting vision of a turbulent life's journey - a journey that is one of the most insightful fictional studies of a woman's consciousness in English literature.", 
		"cover": "https://images2.penguinrandomhouse.com/cover/9780679409885"
	},
	{
		"id": 6,
		"title": "Severance",
		"author": "Ling Ma",
		"num_fans":23423,
		"topics":{"fiction": True, "apocalypse": True, "disease": True}, 
		"summary": "Candace Chen, a millennial drone self-sequestered in a Manhattan office tower, is devoted to routine. With the recent passing of her Chinese immigrant parents, she’s had her fill of uncertainty. She’s content just to carry on: She goes to work, troubleshoots the teen-targeted Gemstone Bible, watches movies in a Greenpoint basement with her boyfriend. So Candace barely notices when a plague of biblical proportions sweeps New York. Then Shen Fever spreads. Families flee. Companies halt operations. The subways squeak to a halt. Her bosses enlist her as part of a dwindling skeleton crew with a big end-date payoff. Soon entirely alone, still unfevered, she photographs the eerie, abandoned city as the anonymous blogger NY Ghost.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81A9dFqIEEL.jpg"
	},
	{
		"id": 7,
		"title": "Normal People",
		"author": "Sally Rooney",
		"num_fans":161016,
		"topics":{"fiction": True, "England": True, "youth": True, "romance": True}, 
		"summary": "At school Connell and Marianne pretend not to know each other. He’s popular and well-adjusted, star of the school soccer team while she is lonely, proud, and intensely private. But when Connell comes to pick his mother up from her housekeeping job at Marianne’s house, a strange and indelible connection grows between the two teenagers—one they are determined to conceal.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/71wD4yYUqyL.jpg"
	},
	{
		"id": 8,
		"title": "Sense & Sensibility",
		"author": "Jane Austen",
		"num_fans":907851,
		"topics":{"fiction": True, "romance": True, "marriage": True}, 
		"summary": "Marianne Dashwood wears her heart on her sleeve, and when she falls in love with the dashing but unsuitable John Willoughby she ignores her sister Elinor's warning that her impulsive behaviour leaves her open to gossip and innuendo. Meanwhile Elinor, always sensitive to social convention, is struggling to conceal her own romantic disappointment, even from those closest to her. Through their parallel experience of love—and its threatened loss—the sisters learn that sense must mix with sensibility if they are to find personal happiness in a society where status and money govern the rules of love.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81Vxq4Qu19L.jpg"
	},
	{
		"id": 9,
		"title": "Kafka on the Shore",
		"author": "Haruki Murakami",
		"num_fans":274769,
		"topics":{"fiction": True, "journey": True, "Japan": True}, 
		"summary": "Kafka on the Shore, a tour de force of metaphysical reality, is powered by two remarkable characters: a teenage boy, Kafka Tamura, who runs away from home either to escape a gruesome oedipal prophecy or to search for his long-missing mother and sister; and an aging simpleton called Nakata, who never recovered from a wartime affliction and now is drawn toward Kafka for reasons that, like the most basic activities of daily life, he cannot fathom. Their odyssey, as mysterious to them as it is to us, is enriched throughout by vivid accomplices and mesmerizing events. ", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81zvseHim4L.jpg"
	},
	{
		"id": 10,
		"title": "I Owe You One",
		"author": "Sophie Kinsella",
		"num_fans":35451,
		"topics":{"fiction": True, "romance": True, "cheesy": True}, 
		"summary": "Fixie Farr has always lived by her father’s motto: “Family first.” But since her dad passed away, leaving his charming housewares store in the hands of his wife and children, Fixie spends all her time picking up the slack from her siblings instead of striking out on her own. The way Fixie sees it, if she doesn’t take care of her father’s legacy, who will? It’s simply not in her nature to say no to people.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81h65eG8M1L.jpg"
	},
	{
		"id": 11,
		"title": "Pachinko",
		"author": "Min Jin Lee",
		"num_fans":160255,
		"topics":{"fiction": True, "epic": True, "Korea": True, "WWII": True}, 
		"summary": "In the early 1900s, teenaged Sunja, the adored daughter of a crippled fisherman, falls for a wealthy stranger at the seashore near her home in Korea. He promises her the world, but when she discovers she is pregnant--and that her lover is married--she refuses to be bought. Instead, she accepts an offer of marriage from a gentle, sickly minister passing through on his way to Japan. But her decision to abandon her home, and to reject her son's powerful father, sets off a dramatic saga that will echo down through the generations.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51JltMChbpL._SX324_BO1,204,203,200_.jpg"
	},
	{
		"id": 12,
		"title": "My Life in France",
		"author": "Julia Child",
		"num_fans": 74849,
		"topics":{"memoir": True, "France": True, "chef": True}, 
		"summary": "Although she would later singlehandedly create a new approach to American cuisine with her cookbook Mastering the Art of French Cooking and her television show The French Chef, Julia Child was not always a master chef. Indeed, when she first arrived in France in 1948 with her husband, Paul, who was to work for the USIS, she spoke no French and knew nothing about the country itself. But as she dove into French culture, buying food at local markets and taking classes at the Cordon Bleu, her life changed forever with her newfound passion for cooking and teaching. Julia's unforgettable story--struggles with the head of the Cordon Bleu, rejections from publishers to whom she sent her now-famous cookbook, a wonderful, nearly fifty-year long marriage that took the Childs across the globe--unfolds with the spirit so key to Julia's success as a chef and a writer, brilliantly capturing one of America's most endearing personalities.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51b-FaszfiL._SX322_BO1,204,203,200_.jpg"
	},
	{
		"id": 13,
		"title": "On Such a Full Sea",
		"author": "Chang Rae Lee",
		"num_fans": 9882,
		"topics":{"fiction": True, "dystopia": True, "USA": True, "Asian": True}, 
		"summary": "In a future, long-declining America, society is strictly stratified by class. Long-abandoned urban neighborhoods have been repurposed as highwalled, self-contained labor colonies. And the members of the labor class - descendants of those brought over en masse many years earlier from environmentally ruined provincial China - find purpose and identity in their work to provide pristine produce and fish to the small, elite, satellite charter villages that ring the labor settlement.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51zbKP1b3WL._SX329_BO1,204,203,200_.jpg"
	},
	{
		"id": 14,
		"title": "Dogeaters",
		"author": "Jessica Hagedorn",
		"num_fans":2142,
		"topics":{"fiction": True, "Asian": True, "ensemble": True, "Philippines": True, "dictators": True}, 
		"summary": "In Dogeaters, Jessica Hagedorn has transformed her best-selling novel about the Philippines during the Marcos reign into an equally powerful theatrical piece that is a multilayered, operatic tour de force. As Harold Bloom writes \"Hagedorn expresses the conflicts experienced by Asian immigrants caught between cultures...she takes aim at racism in the U.S. and develops in her dramas the themes of displacement and the search for belonging.\"", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51zhTz%2Bi1qL.jpg"
	},
	{
		"id": 15,
		"title": "Homegoing",
		"author": "Yaa Gyasi",
		"num_fans":139975,
		"topics":{"fiction": True, "migration": True, "Africa": True}, 
		"summary": "Two half-sisters, Effia and Esi, are born into different villages in eighteenth-century Ghana. Effia is married off to an Englishman and lives in comfort in the palatial rooms of Cape Coast Castle. Unbeknownst to Effia, her sister, Esi, is imprisoned beneath her in the castle's dungeons, sold with thousands of others into the Gold Coast's booming slave trade, and shipped off to America, where her children and grandchildren will be raised in slavery.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/91KLuKxFuOL.jpg"
	},
	{
		"id": 16,
		"title": "Never Let Me Go",
		"author": "Kazuo Ishiguro",
		"num_fans":432583,
		"topics":{"fiction": True, "dystopia": True, "England": True, "clones": True}, 
		"summary": "Hailsham seems like a pleasant English boarding school, far from the influences of the city. Its students are well tended and supported, trained in art and literature, and become just the sort of people the world wants them to be. But, curiously, they are taught nothing of the outside world and are allowed little contact with it.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81EmWm90b6L.jpg"
	},
	{
		"id": 17,
		"title": "Crazy Rich Asians",
		"author": "Kevin Kwan",
		"num_fans": 288445,
		"topics":{"fiction": True, "romance": True, "Singapore": True, "money": True}, 
		"summary": "When Rachel Chu agrees to spend the summer in Singapore with her boyfriend, Nicholas Young, she envisions a humble family home, long drives to explore the island, and quality time with the man she might one day marry. What she doesn't know is that Nick's family home happens to look like a palace, that she'll ride in more private planes than cars, and that with one of Asia's most eligible bachelors on her arm, Rachel might as well have a target on her back.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/7144OITcNML.jpg"
	},
	{
		"id": 18,
		"title": "Sourdough",
		"author": "Robin Sloan",
		"num_fans":36744,
		"topics":{"fiction": True, "technology": True, "bread": True}, 
		"summary": "Lois Clary, a software engineer at a San Francisco robotics company, codes all day and collapses at night. When her favourite sandwich shop closes up, the owners leave her with the starter for their mouthwatering sourdough bread. Lois becomes the unlikely hero tasked to care for it, bake with it and keep this needy colony of microorganisms alive.  Soon she is baking loaves daily and taking them to the farmer's market, where an exclusive close-knit club runs the show. When Lois discovers another, more secret market, aiming to fuse food and technology, a whole other world opens up. But who are these people, exactly?", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/41YhhUr7iXL._SX332_BO1,204,203,200_.jpg"
	},
	{
		"id": 19,
		"title": "Hadji Murad",
		"author": "Leo Tolstoy",
		"num_fans":7886,
		"topics":{"short(ish) story": True, "Russia": True, "leader": True, "tragedy": True}, 
		"summary": "In 1851 Leo Tolstoy enlisted in the Russian army and was sent to the Caucasus to help defeat the Chechens. During this war a great Avar chieftain, Hadji Murád, broke with the Chechen leader Shamil and fled to the Russians for safety. Months later, while attempting to rescue his family from Shamil’s prison, Hadji Murád was pursued by those he had betrayed and, after fighting the most heroic battle of his life, was killed.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/41CGVnwDhkL._SX331_BO1,204,203,200_.jpg"
	},
	{
		"id": 20,
		"title": "The Winter's Tale",
		"author": "William Shakespeare",
		"num_fans":24261,
		"topics":{"play": True, "tragedy": True, "comedy": True, "Perdita": True}, 
		"summary": "The New Cambridge Shakespeare appeals to students worldwide for its up-to-date scholarship and emphasis on performance. The series features line-by-line commentaries and textual notes on the plays and poems and an extensive introduction. The Winter's Tale is one of Shakespeare's most varied, theatrically self-conscious, and emotionally wide-ranging plays. Much of the play's copiousness inheres in its generic intermingling of tragedy, comedy, romance, pastoral, and the history play. In addition to dates and sources, the introduction attends to iterative patterns, the nature and cause of Leontes' jealousy, the staging and meaning of the bear episode, and the thematic and structural implications of the figure of Time. Special attention is paid to the ending and its tempered happiness.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51x4nu9RcHL._SX309_BO1,204,203,200_.jpg"
	},
	{
		"id": 21,
		"title": "Macbeth",
		"author": "William Shakespeare",
		"num_fans":632777,
		"topics":{"play": True, "tragedy": True, "murder": True, "fates": True}, 
		"summary": "One night on the heath, the brave and respected general Macbeth encounters three witches who foretell that he will become king of Scotland. At first skeptical, he’s urged on by the ruthless, single-minded ambitions of Lady Macbeth, who suffers none of her husband’s doubt. But seeing the prophecy through to the bloody end leads them both spiralling into paranoia, tyranny, madness, and murder.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81u5a4j4HnL.jpg"
	},
	{
		"id": 22,
		"title": "Little Fires Everywhere",
		"author": "Celeste Ng",
		"num_fans":488731,
		"topics":{"fiction": True, "suburbs": True, "family": True, "mystery": True}, 
		"summary": "In Shaker Heights, a placid, progressive suburb of Cleveland, everything is planned--from the layout of the winding roads, to the colors of the houses, to the successful lives its residents will go on to lead. And no one embodies this spirit more than Elena Richardson, whose guiding principle is playing by the rules.  Enter Mia Warren – an enigmatic artist and single mother – who arrives in this idyllic bubble with her teenage daughter Pearl, and rents a house from the Richardsons. Soon Mia and Pearl become more than just tenants: all four Richardson children are drawn to the alluring mother-daughter pair. But Mia carries with her a mysterious past, and a disregard for the rules that threatens to upend this carefully ordered community.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/91twTG-CQ8L.jpg"
	},
	{
		"id": 23,
		"title": "Station Eleven",
		"author": "Emily Mandel",
		"num_fans":279078,
		"topics":{"fiction": True, "apocalypse": True, "King Lear": True, "survival": True}, 
		"summary": "One snowy night a famous Hollywood actor slumps over and dies onstage during a production of King Lear. Hours later, the world as we know it begins to dissolve. Moving back and forth in time—from the actor's early days as a film star to fifteen years in the future, when a theater troupe known as the Traveling Symphony roams the wasteland of what remains—this suspenseful, elegiac, spellbinding novel charts the strange twists of fate that connect five people: the actor, the man who tried to save him, the actor's first wife, his oldest friend, and a young actress with the Traveling Symphony, caught in the crosshairs of a dangerous self-proclaimed prophet.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/919wLDRgyuL.jpg"
	},
	{
		"id": 24,
		"title": "How to Murder Your Life",
		"author": "Cat Marnell",
		"num_fans":11223,
		"topics":{"memoir": True, "editorial": True, "drugs": True, "beauty industry": True}, 
		"summary": "At the age of 15, Cat Marnell unknowingly set out to murder her life. After a privileged yet emotionally-starved childhood in Washington, she became hooked on ADHD medication provided by her psychiatrist father. This led to a dependence on Xanax and other prescription drugs at boarding school, and she experimented with cocaine, ecstasy… whatever came her way. By 26 she was a talented ‘doctor shopper’ who manipulated Upper East Side psychiatrists into giving her never-ending prescriptions; her life had become a twisted merry-go-round of parties and pills at night, and trying to hold down a high profile job at Condé Naste during the day.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/81zT87SMCmL.jpg"
	},
	{
		"id": 25,
		"title": "Paradise Lost",
		"author": "John Milton",
		"num_fans":124428,
		"topics":{"epic": True, "Adam": True, "Eve": True, "serpent": True}, 
		"summary": "John Milton's Paradise Lost is one of the greatest epic poems in the English language. It tells the story of the Fall of Man, a tale of immense drama and excitement, of rebellion and treachery, of innocence pitted against corruption, in which God and Satan fight a bitter battle for control of mankind's destiny. The struggle rages across three worlds - heaven, hell, and earth - as Satan and his band of rebel angels plot their revenge against God. At the center of the conflict are Adam and Eve, who are motivated by all too human temptations but whose ultimate downfall is unyielding love.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/517cj0FtKbL.jpg"
	},
	{
		"id": 26,
		"title": "Chemistry",
		"author": "Weike Wang",
		"num_fans": 14038,
		"topics":{"fiction": True, "romance": True, "science": True, "immigration": True}, 
		"summary": "At first glance, the quirky, overworked narrator [of this] novel seems to be on the cusp of a perfect life: she is studying for a prestigious PhD in chemistry that will make her Chinese parents proud (or at least satisfied), and her successful, supportive boyfriend has just proposed to her. But instead of feeling hopeful, she is wracked with ambivalence: the long demanding hours at the lab have created an exquisite pressure cooker, and she doesn't know how to answer the marriage question. When it all becomes too much and her life plan veers off course, she finds herself on a new path of discoveries about everything she thought she knew.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/618hrON9nnL.jpg"
	},
	{
		"id": 27,
		"title": "Prep",
		"author": "Curtis Sittenfeld",
		"num_fans":58692,
		"topics":{"fiction": True, "high school": True, "youth": True}, 
		"summary": "Lee Fiora is an intelligent, observant fourteen-year-old when her father drops her off in front of her dorm at the prestigious Ault School in Massachusetts. She leaves her animated, affectionate family in South Bend, Indiana, at least in part because of the boarding school’s glossy brochure, in which boys in sweaters chat in front of old brick buildings, girls in kilts hold lacrosse sticks on pristinely mown athletic fields, and everyone sings hymns in chapel.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/417KvWn%2BnSL._SX301_BO1,204,203,200_.jpg"
	},
	{
		"id": 28,
		"title": "When Breath Becomes Air",
		"author": "Paul Kalanithi",
		"num_fans":360726,
		"topics":{"memoir": True, "cancer": True, "doctor": True}, 
		"summary": "At the age of thirty-six, on the verge of completing a decade's worth of training as a neurosurgeon, Paul Kalanithi was diagnosed with stage IV lung cancer. One day he was a doctor treating the dying, and the next he was a patient struggling to live. And just like that, the future he and his wife had imagined evaporated. When Breath Becomes Air chronicles Kalanithi's transformation from a naïve medical student \"possessed,\" as he wrote, \"by the question of what, given that all organisms die, makes a virtuous and meaningful life\" into a neurosurgeon at Stanford working in the brain, the most critical place for human identity, and finally into a patient and new father confronting his own mortality.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/717KRq4xxxL.jpg"
	},
	{
		"id": 29,
		"title": "To the Lighthouse",
		"author": "Virginia Woolf",
		"num_fans":121299,
		"topics":{"fiction": True, "loss": True, "perception": True, "family": True}, 
		"summary": "The serene and maternal Mrs. Ramsay, the tragic yet absurd Mr. Ramsay, and their children and assorted guests are on holiday on the Isle of Skye. From the seemingly trivial postponement of a visit to a nearby lighthouse, Woolf constructs a remarkable, moving examination of the complex tensions and allegiances of family life and the conflict between men and women.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/51uTxSbMjDL._SX327_BO1,204,203,200_.jpg"
	},
	{
		"id": 30,
		"title": "Song of Solomon",
		"author": "Toni Morrison",
		"num_fans":79632,
		"topics":{"fiction": True, "magical realism": True, "journey": True}, 
		"summary": "Milkman Dead was born shortly after a neighborhood eccentric hurled himself off a rooftop in a vain attempt at flight. For the rest of his life he, too, will be trying to fly. With this brilliantly imagined novel, Toni Morrison transfigures the coming-of-age story as audaciously as Saul Bellow or Gabriel García Márquez. As she follows Milkman from his rustbelt city to the place of his family’s origins, Morrison introduces an entire cast of strivers and seeresses, liars and assassins, the inhabitants of a fully realized black world.", 
		"cover": "https://images-na.ssl-images-amazon.com/images/I/41P-CfLMjwL._SX323_BO1,204,203,200_.jpg"
	},

];

@app.route('/')
def homepage():
		return render_template('home.html', data=data, current_id=current_id)

@app.route('/create')
def create_data():
		return render_template('create.html', data=data)

@app.route('/view/<id>')
def load_view(id): 
	global data

	get_id = int(id)

	for book in data: 
		if book["id"] == get_id: 
			b_id=book["id"]
			title=book["title"]
			author=book["author"]
			num_fans=book["num_fans"]
			summary=book["summary"]
			cover=book["cover"]
			topics=book["topics"]

	return render_template('book_template.html', b_id=b_id, title=title, author=author, num_fans=num_fans, summary=summary, cover=cover, topics=topics)

@app.route('/edit/<id>')
def edit_page(id):
	global data

	get_id = int(id)

	for book in data: 
		if book["id"] == get_id: 
			b_id=book["id"]
			title=book["title"]
			author=book["author"]
			num_fans=book["num_fans"]
			summary=book["summary"]
			cover=book["cover"]
			topics=book["topics"]

	return render_template('edit_template.html', b_id=b_id, title=title, author=author, num_fans=num_fans, summary=summary, cover=cover, topics=topics)

	
@app.route('/update_num', methods=['GET', 'POST'])
def update_num():
	global data

	new_data = request.get_json()
	get_id = new_data["id"]
	new_num = new_data["new_val"]

	for book in data:
		if book["id"] == get_id: 
			book["num_fans"]= new_num
			num_fans = book["num_fans"]

	return jsonify(num_fans=num_fans)


@app.route('/update_sum', methods=['GET', 'POST'])
def update_sum():
	global data

	new_data = request.get_json()
	get_id = new_data["id"]
	new_sum = new_data["new_val"]

	for book in data:
		if book["id"] == get_id: 
			book["summary"]= new_sum
			summary = book["summary"]

	return jsonify(summary=summary)


@app.route('/search/<searchval>')
def search_data(searchval):
	global data

	search_data = []

	searchval = searchval.lower()

	for book in data: 
		if searchval in book["title"].lower() or searchval in book["author"].lower():
			search_data.append(book)

	return render_template('search.html', data=search_data, searchval=searchval)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book(): 
	global data 
	global current_id

	new_book = request.get_json()
	# print(new_book)

	current_id += 1
	new_id = current_id
	new_book_entry = {
		"id": new_id, 
		"title": new_book["title"], 
		"author": new_book["author"], 
		"num_fans": new_book["num_fans"], 
		"summary": new_book["summary"], 
		"cover": new_book["cover"], 
		"topics": new_book["topics"]
	}

	data.append(new_book_entry)

	return jsonify(data=data, new_book_entry=new_book_entry)


@app.route('/delete_topic', methods=['GET', 'POST'])
def delete_topic():
	global data

	topic_dict = request.get_json()

	get_id = topic_dict["id"]
	get_topic = topic_dict["topictodelete"]

	for book in data:
		if book["id"] == get_id: 
			book["topics"][get_topic] = False
			topics = book["topics"]

	return jsonify(topics=topics)

@app.route('/undelete_topic', methods=['GET', 'POST'])
def undelete_topic():
	global data

	topic_dict = request.get_json()

	get_id = topic_dict["id"]
	get_topic = topic_dict["topictosave"]

	for book in data:
		if book["id"] == get_id: 
			book["topics"][get_topic] = True
			topics = book["topics"]

	return jsonify(topics=topics)


if __name__ == '__main__':
   app.run(debug = True)
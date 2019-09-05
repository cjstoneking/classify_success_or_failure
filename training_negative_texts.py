
#these are positive cases for training an algorithm to find descriptions of failure in text data
#they consist of sentences or parts of sentences that describe failure in various fields
#(e.g. software, construction, science, charity, miscellaneous companies)

# sources:
#https://raygun.com\blog\costly-software-errors-history\
#https://www.tricentis.com\softwaretesting\real-life-examples-software-development-failures
#https://www.projectmanager.com\blog\failed-projects
#https://www.workfront.com\blog\project-failure-10-famous-failures-and-5-ways-to-spot-them-before-they-happen
#http://calleam.com\WTPF\?p=8540
#https://www.lovemoney.com/gallerylist/65252/the-very-public-failures-of-16-famous-businesses
#https://www.lovemoney.com/galleries/56183/epic-business-fails-that-cost-companies-cash-and-reputation?page=1
#https://www.computerworld.com/article/2533563/it-s-biggest-project-failures----and-what-we-can-learn-from-them.html?page=2
#https://spectrum.ieee.org/riskfactor/computing/it/it-failures-2018-all-the-old-familiar-faces
#https://www.forentrepreneurs.com/why-startups-fail/
#https://www.cbinsights.com/research/startup-failure-reasons-top/
#https://www.quora.com/Why-do-customization-startups-fail
#http://www.forbesindia.com/article/real-issue/the-rise-and-fall-of-educomp/34993/0
#https://medium.com/swlh/inside-the-failure-of-a-startup-b4a123c962bb
#https://www.fastcompany.com/90239881/your-startup-is-failing-now-what
#https://www.fastcompany.com/90296151/coming-clean-on-a-painful-failure-allowed-me-to-move-on-from-it
#https://www.fastcompany.com/90314465/these-are-the-lessons-i-learned-from-failure
#https://medium.com/@jasonhuertas/my-startup-failed-6c54bd68c654
#https://medium.com/swlh/what-i-learned-from-my-failed-startup-98e8ecf64ef3
#https://medium.com/swlh/why-90-of-startups-fail-and-what-to-do-about-it-b0af17b65059
#http://bfwa.com/2013/09/18/10-billion-16-billion-it-failure-yep-its-the-uk-again/
#http://brucefwebster.com/2008/06/16/anatomy-of-a-runaway-it-project/
#https://projectfailures.wordpress.com/2008/06/24/project-from-hell/


training_negative_texts = {
  "The disaster resulted in a 32-month hiatus in the shuttle program":0,\
  "The spacecraft disintegrated over the Atlantic Ocean":0,\
  "Marshall and Thiokol realized that they had a potentially catastrophic problem on their hands":0,\
  "Hindenburg was an airship made in Germany and led to a big disaster that killed 36 passengers including crew members":0,\
  "The airship caught fire and also crashed while trying to dock itself in New Jersey":0,\
  "The Quebec Bridge collapsed twice in Canada":0,\
  "This disaster is known to have killed as many as 88-89 workers":0,\
  "It was a big disaster for them, and they thought they had learned their lesson":0,\
  "Yet again, disaster struck in 1916 and the central span of the bridge crumbled down":0,\
  "This time, it killed 13 workers":0,\
  "Titanic is one of the most well-known engineering disasters in the world that claimed the lives of more than 1500 people onboard":0,\
  "In 1986, nuclear reactors failed and led to a series of explosions and radioactive fallout":0,\
  "The airport was inaugurated in May 2004, and soon after, a huge portion of the roof of Terminal 2E collapsed":0,\
  "Due to the collapse, 4 people died immediately and 3 people incurred heavy injuries":0,\
  "After this disaster, they reconstructed the terminal which cost them as much as $120 million":0,\
  "Finally, in 1928, the dam burst 2 hours after his inspection and killed over 450 people":0,\
  "Ultimately, it led to the collapse of the bridge":0,\
  "The disaster happened when 3 out of the 4 boilers of Sultana exploded and the steamboat sunk almost 7 miles from Memphis":0,\
  "The estimated death toll was somewhere between 1500-1800 passengers":0,\
  "The NASA Space Shuttle Challenger disaster took place on January 28, 1986, when the shuttle broke apart precisely 73 seconds into flight":0,\
  "The disaster killed 7 astronauts who were on board":0,\
  "The Concorde flight of Air France on 25th July 2000 crashed soon after its take-off from the Charles De Gaulle International Airport":0,\
  "It killed 113 people in total":0,\
  "May 1915 saw one of the worst rail disasters that have ever happened in British history":0,\
  "After an investigation, it was found that the reason behind the disaster, as expected, was human error.":0,\
  "This tragedy killed more than 226 people":0,\
  "On 20th October 1944, a gas explosion took place in Cleveland, Ohio":0,\
  "What happened next was a series of explosions and fires that claimed the lives of 130 people":0,\
  "Thereafter, it ignited and resulted in a catastrophe that caused a substantial dent on the natural gas industry":0,\
  "On 17th July 1981 in Kansas City, two vertical walkways collapsed in the lobby of the Hyatt Regency Hotel":0,\
  "The walkways fell down and claimed the lives of 114 people":0,\
  "The Space Shuttle Columbia killed a crew of 7 astronauts on 1st February 2003":0,\
  "It disintegrated when reentering the Earth’s atmosphere":0,\
  "The tiles failed and caused a rapid chain of events that finally disintegrated the shuttle":0,\
  "This catastrophe almost completely wiped off Johnstown and a total of 2209 deaths were reported soon after":0,\
  "In 1975, the Banqiao Dam in China failed and was considered as one of the worst engineering disasters that time":0,\
  "However, disaster struck and claimed the lives of an unprecedented 230,000 people in the calamity":0,\
  "Furthermore, at least 11 million people were forced to relocate post the catastrophe":0,\
  "This disaster also resulted in a staggering economic loss that cost the country $1.6 billion":0,\
  "The Bhopal gas tragedy took place in the year 1984 when toxic gas was released at a pesticide plant of Union Carbide in Bhopal, India":0,\
  "This disaster resulted in the immediate death of 2259 people, and more than 11,000 deaths followed after the catastrophe":0,\
  "The disaster took place when more than 42 tons of Methyl Isocyanate got contaminated with water and caused an exothermic reaction":0,\
  "According to a government affidavit released in 2006, this tragedy resulted in 558,125 injuries from which 3900 people suffered from permanently disabling injuries":0,\
  "Even 34 years after this horrific disaster took place, the lands in Bhopal are toxic to humans as well as animals":0,\
  "An oxygen tank on Apollo 13 exploded merely two days after its launch from the Kennedy Space Center in Florida on 11th April 1970":0,\
  "This explosion caused massive hardship to the crew members as they suffered from limited power, lack of potable water, loss of cabin heat and much more":0,\
  "Three astronauts died when a fire broke out in the midst of a preflight test in 1967":0,\
  "The command module of the craft ruptured as the fire created problems":0,\
  "In Boston, a large tank of molasses collapsed at 529 Commercial Street":0,\
  "This disaster also resulted in the crushing of the foundations of the nearby buildings":0,\
  "It claimed 21 lives and 150 people were reported injured":0,\
  "It sustained severe damage during the launch, and one of the more severe damages was the loss of its primary solar panels and the micrometeoroid shield\sunshade of the station":0,\
  "This prevented the deployment of Skylab and caused an exorbitant cost of $3.6 billion to be incurred by the orbiting space station":0,\
  "Software failures have wreaked havoc at banks, airlines and the NHS, doing billions of pounds of damage and devastating disruption":0,\
  "On its mission to Mars in 1998 the Climate Orbiter spacecraft was ultimately lost in space":0,\
  "Unfortunately, the Ariane 5’s faster engines exploited a bug that was not found in previous models":0,\
  "Thirty-six seconds into its maiden launch the rocket’s engineers hit the self destruct button following multiple computer failures":0,\
  "The resulting overflow conditions crashed both the primary and backup computers (which were both running the exact same software)":0,\
  "The Ariane 5 had cost nearly $8 billion to develop, and was carrying a $500 million satellite payload when it exploded":0,\
  "The two pieces of software were completely incompatible, and irreversible errors were introduced as a result":0,\
  "After being hacked in June, 2011, Mt. Gox stated that they’d lost over 850,000 bitcoins (worth around half a billion US dollars at the time of writing)":0,\
  "It is thought that “real life” scenarios such as removing a bag from the system manually when a passenger had left an important item in their luggage, had caused the entire system to become confused and shut down":0,\
  "On a mission to fly-by Venus in 1962, this spacecraft barely made it out of Cape Canaveral when a software-coding error caused the rocket to veer dangerously off-course, threatening to crash back to earth":0,\
  "One of the biggest American market makers for stocks struggled to stay afloat after a software bug triggered a $440 million loss in just 30 minutes":0,\
  "The firm’s shares lost 75 percent in two days after the faulty software flooded the market with unintended trades":0,\
  "An inquiry into the mishap determined that it was caused by a lack of procedural discipline throughout the facility":0,\
  "In 2015, CareFusion’s Alaris Pump was recalled over a software error that caused the pump, designed to automatically deliver medicine and fluids to hospital patients, to delay an infusion":0,\
  "The consequences, which can range anywhere from medicine being withheld at critical points or accidental over-dosing, can be deadly":0,\
  "Just four days later CareFusion issued a Class I recall over a separate line of ventilators, citing a software flaw that could cause the patient to suffocate":0,\
  "This spring a serious software glitch in the F-35 Joint Strike Fighter air crafts garnered wide public attention":0,\
  "Equifax, one of the United States’ largest credit reporting agencies, announced that up to 143 million of their consumer records were stolen by hackers":0,\
  "As details of the hack have emerged, it quickly became clear that much of the damage done was a result of vast negligence on Equifax’s part":0,\
  "Investigations found that while the problem was largely due to human error, there were “troubling” design flaws in the Hawaii Emergency Management Agency’s alert origination software":0,\
  "But soon the market had options that were cheaper and better than Betamax, making it a failed project":0,\
  "Sony’s mistake was thinking that the project was complete once the product went to market":0,\
  "The fact is, New Coke sunk like a stone":0,\
  "But after spending $4 million in development and losing another $30 million in backstocked product, the taste for New Coke evaporated":0,\
  "It’s not that Coca-Cola neglected market research to see if there was a need for developing a new product, but they were blind to their own customers’ motivations":0,\
  "New Coke was a failed project because the researchers needed to do more than a mere taste test":0,\
  "Though Stretch could handle a half-million instructions per second and was the fastest computer in the world up to 1964, the project was deemed a failure":0,\
  "While the project was a failure in that it never achieved the goal it set, there was much IBM could salvage from the project":0,\
  "On January 28, 1986, that risk became a horrible reality as space shuttle Challenger exploded 73 seconds after launch":0,\
  "The cause was a leak in one of the two solid rocket boosters that set off the main liquid fuel tank":0,\
  "But it was not only a technical error that NASA discovered, but human error":0,\
  "NASA officials went ahead with the launch even though engineers were concerned about the safety of the project":0,\
  "Problems started at the beginning when the state solicited only one bid for the contract, Tandem Computers, locking the state into buying their hardware":0,\
  "Then, to make things worse, tests showed that the new computers were even slower than the ones they were to replace":0,\
  "The story of Betamax has become nearly synonymous with failed marketing because while it was innovative and hit the market before its competition did, other products proved to be cheaper and better":0,\
  "Product loyalty and old-fashioned habit got in the way and people didn’t buy New Coke as expected, costing the company $4 million in development and a loss of $30 million in backstocked product it couldn’t sell":0,\
  "It was groundbreaking at the time, but the two-and-a-half minute time limit, lack of sound, and the fact that you couldn’t watch the videos on your regular TV meant this project lasted just two years":0,\
  "The Polavision was revolutionary, but Polaroid dropped the ball when they failed to stay abreast of developing marketing needs":0,\
  "But people soon lost interest and the novelty wore off, making it impossible for Crystal Pepsi to gain a strong market share":0,\
  "David Novak was the COO of PepsiCo during the project and didn’t listen when bottlers told him the Crystal Pepsi flavor wasn’t quite right":0,\
  "I learned there that you have to recognize that when people are bringing up issues, they might be right":0,\
  "In 1996, McDonald’s put more than $150 million into advertising—more than it had ever spent on an ad campaign—for its new Arch Deluxe Burger, only to find out its customers weren’t interested in the more grown-up, sophisticated menu option":0,\
  "This is another case that highlights the importance of letting customer data drive product strategy":0,\
  "If McDonald’s had a more accurate picture of what its customers wanted, it could have saved millions in advertising and resources":0,\
  "Consumers weren’t as interested as Apple anticipated, and it was a case of over promising and under delivering":0,\
  "There’s no better way to describe the lesson learned here other than to say that Apple was not transparent enough about the Lisa":0,\
  "The company ran a Super Bowl ad (that’s one project you don’t want to fumble!) that only confused customers and the style never caught on, forcing Levi’s to walk away from this flop":0,\
  "IBM released its PCjr in 1983 in an attempt to attract home computer users, but the PCjr offered fewer features than its competitors and was twice as expensive as an Atari or Commodore":0,\
  "After customers complained about the low-quality keyboard, IBM offered an alternative, which had its own issues, and couldn’t revive interest in the PCjr":0,\
  "Unfortunately, its response wasn’t quite enough because the product was low quality and didn’t help improve users’ experience with the PCjr":0,\
  "Even the futuristic shape, gull-wing doors, and gold-plated models weren’t enough to save the DeLorean DMC-12, which experienced problems throughout production, giving it a rough start":0,\
  "In 2016, a new DeLorean was announced and then delayed due to some legal issues":0,\
  "But by the time all this research was done and the car was unveiled in 1957, Ford had missed its chance with its market, which had already moved on to buying compact cars, which didn’t include the Edsel":0,\
  "The Ford Edsel is the perfect example of the importance of speed to market and how even a major brand and product can fail if a project loses velocity":0,\
  "Things like poor communication, inaccurate deadlines, and out-of-touch project managers can majorly slow a project down, to the point that it’s no longer relevant or valuable":0,\
  "People stop showing up for meetings":0,\
  "Stakeholders stop participating or giving timely feedback":0,\
  "Tasks stop getting completed on time.":0,\
  "The team doesn't know when things are getting done, what's not getting done, or why it's not getting done":0,\
  "The project lead isn't communicating changes to the rest of the team":0,\
  "When communications do go out, they are either late or inaccurate":0,\
  "Assignments are long past due, stalled on the approval of an elusive stakeholder":0,\
  "At any rate, contrary to your best projected completion dates, your project has come to a full stop":0,\
  "Maybe team members are spending more and more time on other projects":0,\
  "The project leader finds out about late assignments long after they were due":0,\
  "When project questions are emailed out, answers are slow in coming":0,\
  "Individual reports in meetings are especially rosy and don't match the chaos that seems to be engulfing a project":0,\
  "The project starts to barely resemble the requirements as they were given at its outset":0,\
  "Timelines have stretched beyond the original projections":0,\
  "In a marketing campaign gone awry, US based ‘Build-a-Bear Workshop’ gained world-wide attention by attracting too many customers to their stores":0,\
  "With limited in store capacity, locations quickly filled up and management had to quickly deploy staff to marshal line ups outside":0,\
  "Within hours it was clear that the one-day promotion could not accommodate all of the children wanting to participate and many families were left in tears as they found their wait was in vain":0,\
  "The story is obviously an illustration of what can happen when risks aren’t managed and you could consider attracting more customers than anticipated to be an upside risk (opportunity risk)":0,\
  "Lack of risk management – failure to develop contingency plans":0,\
  "Failure to anticipate demand":0,\
  "Poor assumptions":0,\
  "a list of failed and troubled projects from around the world":0,\
  "The program was eventually cancelled in March of 2018 at which point the suburban market was considerably higher than it was when the program was first launched":0,\
  "For those who did buy using the program, and for those attracted in because of FOMO, they are now faces potentially significant loses because a deflating bubble":0,\
  "Poorly designed program that triggered unanticipated consequences":0,\
  "Inventory is building and there are clear signs of trouble ahead":0,\
  "If the analysis in the business case turns out to be incorrect or incomplete the organization may have invested significant amounts of money which they will never recoup":0,\
  "Sadly, in Feb 2019 Airbus has announced that the A380 production program is to be wound up with just 253 aircraft built, far short of the 700 plus predicted by Airbus when the aircraft was first launched":0,\
  "Airbus is not declaring the net loss for the project as a whole, but given that development costs are said to have been in the order of $20 to $25 billion and only about 35% of the anticipated aircraft were built, the write offs are likely to be considerable":0,\
  "Not only are the development costs being spread across fewer aircraft, but the lower build total will likely have meant higher unit costs due to the failure to scale the production line up to the full capacity originally planned (failure to achieve economies of scale)":0,\
  "the project has not lived up to expectations":0,\
  "That of course begs the question of what went wrong":0,\
  "A number of industry overseers have been predicting the failure of the program since day one":0,\
  "In fact, the cancellation of the production program concludes a long-held debate in the aviation industry":0,\
  "As a lesson learned it appears that the problem was that the business case focused on initial sales and did not anticipate that the second-hand market simply would not be there.":0,\
  "Perhaps if Airbus had put more thought into how they could stimulate a strong second-hand market right from day one, the A380 story may have had a different ending":0,\
  "Issues with the scope of the business case (not enough attention to the second-hand market).":0,\
  "Bad assumptions":0,\
  "Given that only 2% of Afghanistan is forest, the use of a forest pattern does seem like a poor choice":0,\
  "Non-experts being allowed to make unilateral decisions":0,\
  "Lack of quality control activities (failure to test the uniforms or do a peer review)":0,\
  "Lack of management oversight":0,\
  "Failure to engage appropriate stakeholders":0,\
  "We wasted $28 million of taxpayers’ money in the name of fashion, because the defense minister thought that that pattern was pretty":0,\
  "Reasons cited for about 50, 000 non-functioning water are amongst others; poor construction, lack of expertise and experience, poor supervision, failure caused by well users, and poor technology choice":0,\
  "People tend to make assumptions about why water sources fail and blame a lack of spare parts, financing, maintenance problems or climate change, for example":0,\
  "Those reasons for failure make sense but may not tell the full story":0,\
  "Lack of capacity building underlies many failed donor funded projects":0,\
  "Operational dysfunction":0,\
  "lack of support to ensure long-term sustainability (Focal imbalance failures)":0,\
  "insufficient capacity building at local level":0,\
  "lack of project management training and support":0,\
  "failure to ensure availability of sufficient resources":0,\
  "Money wasted on water projects in Africa":0,\
  "the city of Montreal has recently completed the demolition of an overpass that was only built a year previously":0,\
  "Failure to coordinate across multiple projects":0,\
  "Lack of internal communications":0,\
  "Lack of long term planning":0,\
  "Failure to utilize program management practices":0,\
  "Brand new $11 million overpass torn down in Montreal":0,\
  "Highway 15 overpass, completed last year, now being demolished":0,\
  "Back to the drawing board":0,\
  "Instead of rising, Canada’s new federal government payroll system (called Phoenix) seems to be stuck firmly in the flames":0,\
  "a good percentage of public servants have been incorrectly paid":0,\
  "you know your project is in trouble when":0,\
  "As soon as the system was launched it was clear there were problems":0,\
  "As many as 7,000 calls per day were received by the system help desk":0,\
  "Being sized for a maximum of 2,200 calls per day the help desk was quickly overcome":0,\
  "By July of 2016, the number of outstanding problems reported by government employees had reached a staggering 82,000 cases":0,\
  "An analysis of the problems by government staff and IBM (the IT systems provider) found that the costs to address the ousting issues could be as a high as $50M":0,\
  "Failure to provide users with adequate training":0,\
  "Failure to have sufficient resources on hand to address launch glitches and problems":0,\
  "Failure to cleanse data prior to migration to the new system":0,\
  "Software quality issues":0,\
  "Liberals agree to emergency meeting Thursday over Phoenix payroll mess":0,\
  "an airport that may turn out to be too dangerous to land at":0,\
  "At the time of writing the decision to indefinitely postpone the opening of the airport has been made.":0,\
  "It is a shame that more serious consideration wasn’t given prior to the investment being made":0,\
  "Options for how to overcome the issues are currently being considered":0,\
  "Those warnings were apparently ignored (or misjudged) and it appears the project failed to conduct appropriate environmental \ flight operations studies prior to construction":0,\
  "It is a shame that more serious consideration wasn’t given prior to the investment being made":0,\
  "Berlin’s long awaited Brandenburg airport still has no confirmed opening date":0,\
  "Failure to listen to the advice of experts":0,\
  "St Helena airport costing £285m of UK money is delayed over safety concerns":0,\
  "Failure to assess or address risks":0,\
  "However, the failure to analysis the full implications of the move resulted in lead leaching into the water supply exposing many residents to hazardous levels of the poisonous metal":0,\
  "In January 2016 both state and federal levels declared Flint an official disaster area allowing additional funds to be channeled into fixing the damaged pipes":0,\
  "This is a project that has harmed real people and a reminder of the safety concerns that some classes or project carry.":0,\
  "Cost cutting (putting money ahead of quality)":0,\
  "Failure to apply appropriate quality standards":0,\
  "Cavalier attitude towards safety risks":0,\
  "Failure to head warnings from stakeholders":0,\
  "Lack of effective governance":0,\
  "Leadership failures":0,\
  "Events That Led to Flint’s Water Crisis":0,\
  "Arguably one of the most expensive scandals in modern corporate history":0,\
  "the revelation that Volkswagen cheated government emission testing has shaken people’s confidence in a once solid brand":0,\
  "the story is both an embarrassment for the company and a financial disaster for the shareholders":0,\
  "In addition to fines of up to $18 billion at least $25 billion has been lost due to a dive in stock price":0,\
  "In many projects the failure is because of mistakes or poor management":0,\
  "In this particular case the problem was man-made and intentional":0,\
  "Trust and confidence in loyal customers has been shaken":0,\
  "the goodwill they enjoyed is now questioned and looked at through a magnifying glass":0,\
  "knowledge of the disaster is now in the public domain":0,\
  "Volkswagen has apologized to its customers and the public and has ordered an external investigation into the matter pledging full cooperation in uncovering of the facts":0,\
  "The project started in 2008 but unfortunately, 8 years later, there is still no operational system in place":0,\
  "Reports from Port Elizabeth indicate that flaws in the design process have resulted in bus lanes that are impractical, zebra crossings that obstruct traffic flow and design flaws that represent a danger to users of the system":0,\
  "The busses themselves typify the types of mistakes made":0,\
  "A faulty specification process resulted in the purchase of buses that were too big for the driving lanes":0,\
  "Challenges in the project have also resulted in significant turnover in key resources working on the project":0,\
  "The challenges the project has encountered also raises serious concerns over the governance process in use":0,\
  "How could a project go for so long with so much dysfunction":0,\
  "Lack of oversight (six years after fact the matter is being pursued)":0,\
  "Failure to engage stakeholders":0,\
  "High staff turnover levels":0,\
  "Poor requirements management and a lack of attention to detail (resulting in faulty requirements), and dysfunctional decision-making":0,\
  "Bus Crisis in Nelson Mandela Bay":0,\
  "Nelson Mandela Bay buses worth R100m gather dust in failed project":0,\
  "having a noble goal doesn't make a project any easier":0,\
  "turned into a debacle that has fingers pointing and red faces across the board":0,\
  "From the initial rollout the problems were clear":0,\
  "the system suffered reliability problems that frequently rendered the content inaccessible anyway":0,\
  "the letter also noted that even when used, the content failed to meet all appropriate requirements":0,\
  "failure to fully recognize the transformational shift in learning that e-enabled learning represents":0,\
  "quality related issues":0,\
  "missing requirements":0,\
  "Failure to gain stakeholder support":0,\
  "What Schools Must Learn From LA’s iPad Debacle":0,\
  "Zellers had sold similar products to Target, but had failed to attain consistent profits":0,\
  "Unfortunately those expectations weren’t met":0,\
  "Compounding the problem was the fact Target Canada suffered from supply chain problems that meant empty shelves that should have been stuffed with key products":0,\
  "today’s buyers don’t have much patience for a store that doesn’t have what they want when they want it":0,\
  "The impact was immediate and financial performance was lacklustre at best":0,\
  "Target Canada’s financial results remained weak":0,\
  "Various promises to address the concerns were made, but none gained the traction needed to put the project on the road to success":0,\
  "With reports indicating that Target Canada may not have enough cash to make the next payroll Target Canada filed from bankruptcy":0,\
  "Total losses from their Canadian adventure are said to be in the order of $7B":0,\
  "the expansion was very rapid and appears to be based on the assumption that the openings would be successful":0,\
  "J.C. Penny also failed to use risk management practices":0,\
  "failure to establish a reliable supply chain when first opening":0,\
  "Failure to live up to customer expectations":0,\
  "lack of stakeholder analysis ":0,\
  "Lack of situational awareness":0,\
  "Lack of risk management ":0,\
  "Timeline of Canada Targets rise and fall":0,\
  "Billion-dollar mistake: How inferior IT killed Target Canada":0,\
  "Target Canada was running out of cash":0,\
  "Bankruptcy filing court documents":0,\
  "Top 5 reasons why Target Canada was an epic failure":0,\
  "government can’t run projects":0,\
  "a headache for the municipal staff who operate the system at the city level and for those receiving payments":0,\
  "Shortly after the system’s launch in Nov 2014, the system erroneously made overpayments totalling $20 million to 17,000 recipients":0,\
  "Other problems reported include: payment of incorrect amounts (either too much or too little), financial records being inaccurate (the database not reflecting the value of the cheques issued) and cheques being sent to incorrect addresses":0,\
  "Requiring significant overtime from municipal staff, the cities already strained budgets have little room to absorb the additional overtime and training costs associated with the SAMS implementation":0,\
  "Five months after its initial launch cities report that the problems are ongoing and the Ontario government has been forced to pay millions in additional payments to the cities to accommodate the problems":0,\
  "some organizations don’t seem to learn from their past experiences":0,\
  "The SDMT system (Service Delivery Model Technology) project suffered major issues as well":0,\
  "After a cost overrun that saw the project’s budget balloon from $284M to more than $500M the system suffered similar flaws when first launched":0,\
  "Incorrectly issued cheques, payments made to the wrong people, failure to maintain correct financial records, etc":0,\
  "Lack of quality control ":0,\
  "Launching the product before it was ready":0,\
  "Challenges in defining the requirements fully":0,\
  "Ineffectual training":0,\
  "Ontario’s new welfare computer system a costly failure, says city report":0,\
  "On opening day reality and expectations unfortunately collided":0,\
  "the product as opened was a significant miss of expectations":0,\
  "Resulting negative feedback from the public forced the event to shut down again so that the event could be polished and refined prior to its reopening":0,\
  "there is a broader message underlying the troubles and failures outlined above: the need to actively manage product quality and customer expectations":0,\
  "they run the very real risk that the perception of failure will outweigh any positives they did achieve":0,\
  "Poorly managed expectations":0,\
  "False advertising":0,\
  "Lack of quality controls (allowing the events to open despite significant quality issues in the underlying product and its delivery)":0,\
  "visitors said they were appalled by the experience":0,\
  "parents and children were still underwhelmed":0,\
  "Even a single missed detail has the potential to cause significant problems":0,\
  "Having purchased 2,000 new trains French Railway company SNCF found out how one bad assumption can ‘derail’ a project":0,\
  "SNCF discovered that the newly designed trains are too wide to fit into many of the railway stations they were intended to serve":0,\
  "Such breakdowns can easily occur even within a single organization and the project stands as a reminder of the need to challenge assumptions and pay attention to the details":0,\
  "Communications breakdown between organizations":0,\
  "the now cancelled ‘e-Borders’ project has resulted in a £224M settlement in favour of the suppliers of the system":0,\
  "While the project itself clearly encountered significant difficulties, perhaps the most embarrassing misstep is the handling of the Raytheon contract":0,\
  "Following the contract’s termination in 2010, Raytheon threatened to sue the British government":0,\
  "the lengthy delays were caused by the UK Border Agency’s mismanagement of the project rather than deficiencies in their own execution":0,\
  "Lack of control over procurements":0,\
  "Failure to establish appropriate benchmarks against which to track project progress and vendor performance":0,\
  "Failure to engage appropriate Subject Matter Experts during procurements":0,\
  "Failure to define and stabilize requirements":0,\
  "Under-estimation of complexity":0,\
  "Government IT projects fail because of politicians, not programmers":0,\
  "The sinking of the White Star Line’s Titanic on her first voyage is one of the world’s classic disaster stories":0,\
  "Fifty-eight years before the Titanic, the RMS Tayleur sank having completed less distance than even the Titanic":0,\
  "the ship had a number of design flaws which set the context within which an accident could happen":0,\
  "Neither the ship nor the crew had been properly prepared for the journey ":0,\
  "Because of the iron hull, her compass didn’t work properly":0,\
  "slack in the ropes made it nearly impossible to control the sails":0,\
  "Sailing into fog and rough waters the crew lost situational awareness":0,\
  "Despite dropping anchor as soon as Lambay Island was sighted the ship struck the rocks and was wrecked":0,\
  "360 lives were lost and other than the tip of her mast the ship became submerged":0,\
  "She hit the rocks":0,\
  "she was set up from failure right from the start":0,\
  "there was an inexperienced crew":0,\
  "there was minimal testing":0,\
  "As for many businesses, a major catastrophe is soon forgot and history is happy to repeat itself":0,\
  "Those at the most senior of levels with responsibility for overseeing the work failed in their due diligence and as a result unnecessary risks were taken":0,\
  "Lack of due diligence by those overseeing the project":0,\
  "Lack of training for the crew":0,\
  "Failure to establish and adhere to standards in recruiting the crew":0,\
  "Failure to do appropriate tests of the vessel before sailing":0,\
  "Pressure from management to set sail because of the high profile nature of the ship":0,\
  "Design flaws":0,\
  "Lack of risk management":0,\
  "Poor quality work":0,\
  "a catalogue of blunders and a blood curdling disaster":0,\
  "In Oct 2013, President Obama’s Healthcare.gov website caused a stir by becoming the year’s biggest troubled IT project story":0,\
  "When the President of the United States has to address the issue in front of the whole nation, you know you’ve created a serious mess":0,\
  "reports are now emerging of how the system developed for the State of Minnesota encountered its own set of problems":0,\
  "things did not go as smoothly as hoped":0,\
  "Following the Oct 2013 launch, system problems and glitches prevented Minnesotan’s completing their transactions":0,\
  "The problems continued into Dec 2013 and in a sign of increasing frustrations Minnesota’s governor Mark Dayton sent a “robust” letter direct to the IBM CEO requesting immediate action":0,\
  "the Curam product did not properly perform eligibility determinations or verify individuals’ application information, as required under federal law":0,\
  "The fact that this functionality was not working was known to Curam staff, but was not communicated to MNsure":0,\
  "However as with many such problems once they are in a system it can be a tough job to get them out":0,\
  "There are also reports of problems with the healthcare exchanges in Maryland and Hawaii ":0,\
  "Failure to appreciate the complexity of integrating a new system with existing systems":0,\
  "it was an unproven product at the time that it was selected":0,\
  "It appears the implications of that gap may not have been fully appreciated":0,\
  "Dayton slams IBM for failures with MNsure website":0,\
  "Avon did indeed loose the confidence of its Canadian sales reps by introducing a new sales order management system":0,\
  "the project has now been abandoned with a write-off of between $100 and $125M":0,\
  "the system did not show a clear return on investment":0,\
  "the decision to stop the project ":0,\
  "Reports available in the press indicate that the issues were with the front-end e-commerce components rather than the back-end systems":0,\
  "Basic functions such as logging in, saving orders and checking inventory were not working properly":0,\
  "Furthermore, complaints about usability have surfaced":0,\
  "the Avon user interface was poorly structured and did not meet the expectations users have of a modern tablet app":0,\
  "One senior sales executive reported that she lost more than 300 of her sales agents as a result of the project":0,\
  "Lack of stakeholder analysis and the failure to understand the sale’s agents expectations of an app":0,\
  "Inside Avon’s Failed Order-Management Project":0,\
  "Avon Pulls Plug On $125 Million SAP Project":0,\
  "reports of problems with the website started to surface on its very first day":0,\
  "the system suffered from slow responses, access denied errors and other mysterious glitches that prevented some users from completing their transactions":0,\
  "Three weeks after its launch the problems are persisting":0,\
  "the President had to admit that the performance of the system was below what would be expected":0,\
  "the list of projects that underestimated the volume of transactions they would be facing":0,\
  "Compounding the problem reports of quality defects in the software have added a further layer of frustration in front of those trying to utilize the new system.":0,\
  "fixing the problems could still be long road ahead":0,\
  "Schedule pressure resulting in lack of time for appropriate testing":0,\
  "Obamacare Website Programmers Complained About Unrealistic Deadlines":0,\
  "President Obama acknowledges healthcare website faults":0,\
  "As work proceeded still further problems were encountered":0,\
  "the failure to deliver a working system resulted in the project being abandoned in May 2013":0,\
  "a terrible shock and clearly completely shambolic":0,\
  "The BBC’s Chief Technology Officer was suspended pending an enquiry and £100M was written off":0,\
  "Underestimation of complexity":0,\
  "DMI was the BBC’s second technology project failure in 2013":0,\
  "In March 2013, a project designed to translate foreign news reports into English was also abandoned ":0,\
  "BBC digital catastrophe criticized":0,\
  "BBC abandons £100m digital project":0,\
  "After years of waste and chaos, failing IT scheme is finally axed by humiliated corporation":0,\
  "Former BBC technology boss sacked over failed project ":0,\
  "Customers were unimpressed":0,\
  "The effect on the bottom line was immediate":0,\
  "Revenues for the 2012 year dropped by a staggering 28%, a net loss of $1B mounted up and same store sales dropped by 32%":0,\
  "As for many failed projects the visionary leader paid for the failure with his job":0,\
  "Top down decision-making and a failure to engage effectively with the front line staff who understood the customer better":0,\
  "Prior successes (the Apple stores) result in over-confidence which sets the stage for future failures":0,\
  "The 5 Big Mistakes That Led to CEO’s Ouster at JC Penney":0,\
  "J.C. Penney Pricing Disaster Destroyed Employee Morale":0,\
  "The tactic failed because management grossly underestimated its customers’ desire for deal-seeking":0,\
  "Who dropped the ball on this":0,\
  "a shocking 70% of organizations included in the survey had experienced a failed project over a 12-month period":0,\
  "following a number of delays the project only reached operationally status in Aug of 2012":0,\
  "Immediately following its operational launch problems were encountered":0,\
  "Those problems continued to grow and the issues became headline news in New Zealand":0,\
  "the operational staff supporting the system appear to have been overwhelmed by the amount of manual intervention needed to correct those errors":0,\
  "Tracking and analysis of the errors identified after the launch, identified more than 500 distinct defects in the system":0,\
  "Many of those problems were traced back to errors in the original project requirements and the design of the new system that allowed incorrect data to be entered into the system thereby leading to incorrect payroll payments and related problems":0,\
  "Implementing the system with a high number of unresolved defects":0,\
  "Novopay errors rise":0,\
  "In an incident that drew worldwide attention, J.P. Morgan lost billions of dollars in the so called London Whale incident":0,\
  "a poorly positioned trade resulted in losses that eventually totalled up into the billions of dollars.":0,\
  "failures in the project that developed the tool were the driving forces that lead to the debacle":0,\
  "In this case, the Model Review Group required only limited back-testing of the new model, and it insufficiently analyzed the results that were submitted":0,\
  "The Model Review Group’s review of the new model was not as rigorous as it should have been and focused primarily on methodology and CIO-submitted test results":0,\
  "The CIO’s implementation of the model was flawed":0,\
  "Data were uploaded manually without sufficient quality control":0,\
  "Failure to follow through with quality related action items identified in a risk assessment review":0,\
  "pricing errors that in part lead to the £700M legal wrangle between the two parties":0,\
  "Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses":0,\
  "$6.1B in additional costs due to project delays":0,\
  "Often when a project gets into trouble it is the result of the interaction of many poorly made decisions":0,\
  "Occasionally it is a single decision that can be isolated out as the source of trouble":0,\
  "At the heart of the problems were difficulties integrating the complex wiring system needed to operate the aircraft with the metal airframe through which the wiring needed to thread":0,\
  "the project that created this behemoth suffered its fair share of problems and delays":0,\
  "Originally scheduled for delivery in 2006, the aircraft’s entry into service was delayed by almost 2 years and the project was several billion dollars over budget":0,\
  "Internal reviews identified that the heart of the problem was the fact that the different design groups working on the project had used different Computer Aided Design (CAD) software to create the engineering drawings":0,\
  "The root of the problem can be traced back to a single decision":0,\
  "As for many failed decisions there is a lot of context that lead up to that decision":0,\
  "Five years later that issue was to cost him his job and he resigned as part of the house cleaning that resulted once the magnitude of the issue became clear":0,\
  "the seed from which a billion dollar delay matured":0,\
  "Failure to address issues when they were first identified resulted in snowballing costs and significantly higher costs once the problems were finally faced up to":0,\
  "Failure to form a single project team across the multiple design centres in use":0,\
  "The errors in the SAP system affect everyday lives":0,\
  "the system had failed to produce a payroll that didn’t contain significant deficiencies":0,\
  "Reports indicate that hundreds of separate problems were present in the payroll and even simple functions could not be relied upon":0,\
  "Early reports do not yet indicate the cause of the problems":0,\
  "California ends contract with SAP over troubled IT project":0,\
  "Project termination announcement from the State Controllers Office":0,\
  "The fact that the payroll system had so many problems":0,\
  "duplicative, stand-alone and ineffective.":0,\
  "By 2010 signs of major problems had surfaced":0,\
  "one of the most egregious examples of mismanagement in recent memory":0,\
  "In a project of this size the causes of failure are often wide ranging":0,\
  "Failure to baseline existing practices and to establish effective measures for the desired outcomes":0,\
  "The hierarchical decision making structures in the military were poorly aligned with the governance structure in use by the project ":0,\
  "Lack of trust between groups":0,\
  "Unwillingness to adapt operating processes to match the capabilities of the software":0,\
  "lack of focus on actual project performance resulting in quality related issues being swept under the carpet":0,\
  "Lack of experience in large scale, complex integrated systems development and deployment":0,\
  "Air Force scraps massive ERP project after racking up $1B in costs":0,\
  "More than 3 years late and many billions of dollars over budget":0,\
  "Difficulty managing and integrating across a large supply chain and development partners":0,\
  "The failure to print the original amount of money loaned on the statements given to customers violated the law ":0,\
  "The paperwork errors amount to a total of £270M further increasing the loses the government has incurred as a result of the sub-prime debacle":0,\
  "Northern Rock to repay £270m due to paperwork error":0,\
  "Lack of technical knowledge and skills":0,\
  "The 2012 US Presidential election illustrates how the failure to properly test a key system can cause an embarrassing failure at a critical point in time":0,\
  "Frustration from the users rose rapidly and trying to fix the issues took critical resources away from managing the campaign":0,\
  "At the core of the problem was a failure to subject the system (or it’s users and support personnel) to the same level of testing as Narwhal had received":0,\
  "Failure to do so can dramatically raise stress levels at critical points in time":0,\
  "Failure to perform dress rehearsals":0,\
  "Failure to stress test a new system in its full operational environment":0,\
  "The system had major technical problems during Election Day that prevented many volunteers from using it.":0,\
  "Frustrated volunteers reported being unable to access ORCA and criticised a lack of prior briefing, misleading instructions and patchy on-the-day support":0,\
  "Throughout election day, volunteers experienced frequent and widespread problems using ORCA, which crashed periodically":0,\
  "Unfortunately the design fell short of the market requirements and the machine was savaged by the press following its launch":0,\
  "just 11 months after the failed launch, Sinclair Vehicles went bankrupt":0,\
  "Failure to consider all of the requirements needed to make a practical solution":0,\
  "the project exceeds its original cost estimates by $240M":0,\
  "the troubled project did achieve partial deployment":0,\
  "rising costs resulted in a decision to cancel the project in 2012":0,\
  "In the end the base system was largely rewritten which resulted in the massive cost overruns":0,\
  "An audit of the project found a lack of planning and criticized the project for failing to do sufficient analysis before making key strategic decisions":0,\
  "Failure to develop a solid business case before making key strategic implementation decisions":0,\
  "Poor planning":0,\
  "Troubled HealthSMART System Finally Cancelled in Victoria Australia":0,\
  "The project’s problems continued even after engaging an outside supplier to complete the work":0,\
  "Lack of due diligence on behalf of the Bureau and failure to establish effective communications with the supplier resulted in a significant number of missing requirements":0,\
  "Despite warnings from external auditors the problems were allowed to persist and ultimately time ran out":0,\
  "The failure of the project resulted in the Bureau having to request an addition $3B in funding to complete the work using the existing manual procedures":0,\
  "Failure to create an effective governance structure in the early years of the project":0,\
  "Lack of communication between Census Bureau and its prime contractor":0,\
  "Failure to establish and stabilize requirements resulting in significant requirements volatility":0,\
  "initial reaction from the press was poor":0,\
  "In the end none of the teams were interested":0,\
  "Lack of vision":0,\
  "Failure to manage expectations":0,\
  "Failure to plan properly for the post event disposition of the venue":0,\
  "Despite significant technical problems with the prototype":0,\
  "failure to right itself after the bend and major mechanical failures":0,\
  "Pushing the fleet into public service before the technical issues were resolved resulted in a major public relations disaster and the ultimate cancellation of the project":0,\
  "Pushing a product into full service before quality issues were fully resolved, thereby resulting in the product being ridiculed":0,\
  "the tendering process was flawed":0,\
  "Inappropriate management of communications during bidder process":0,\
  "Failure to ensure all bidders were given equal access to information during the bid process":0,\
  "Lack of quality control measures to ensure fairness":0,\
  "total chaos as government scraps franchise deal":0,\
  "Following the incidents the fleet was grounded and an enquiry into the accidents conducted":0,\
  "Sadly a few months later a third aircraft broke up in flight":0,\
  "This time it was found that the crash (and the two prior ones) had been caused by cracks in the metal airframe":0,\
  "the failure affected a complete industry rather than just a single project or organization":0,\
  "Lack of technical knowledge available at the time ":0,\
  "Breakdown in communications":0,\
  "unwillingness of those responsible to tell those in power of the flawed design or results of the testing":0,\
  "the critical mistakes made by the committee were":0,\
  "it proved to be a commercial failure":0,\
  "Airlines failed to order a single aircraft":0,\
  "Failure to recognize changing market needs and the impact of disruptive technology":0,\
  "After ten years of effort and millions of dollars spent, the project is abandoned as it becomes clear that the system will never work as planned":0,\
  "Efforts to move form paper based stock trading to a computerized system becomes a classic tale of failure":0,\
  "The Taurus failure is really two failures in one":0,\
  "After 5 years of development and the realization that changing the business processes was a significant technical challenge as well, the design was dropped in 1989":0,\
  "Modifying the US system to comply with British regulations and the requirements of the many stakeholders proved to be more difficult than anticipated":0,\
  "Such significant modification essentially negated the value of purchasing the system and resulted in major challenges developing and testing the software":0,\
  "After a number of such delays and external audits that suggested the underlying design that had been adopted had become unworkable, the project was eventually scrapped in 1993":0,\
  "Poor strategic decision making":0,\
  "In 2009 the Stock Exchange had to replace another system following system performance concerns":0,\
  "Management failure":0,\
  "Software failure":0,\
  "Learning from the world’s worst computer disasters":0,\
  "purchasing a system that was a poor fit to requirements":0,\
  "Poor communications and poorly selected job candidates resulted in very poor turnout":0,\
  "Failure to appreciate the size and complexity of the project.":0,\
  "Failure to hire appropriately committed staff":0,\
  "Failure to train staff adequately":0,\
  "Poor internal communications and a failure to establish appropriate controls and management processes to ensure the project was properly organized":0,\
  "G4S shambles revealed in internal report":0,\
  "Two G4S directors resign in wake of Olympics fiasco":0,\
  "Unfortunately the gap between the local requirements and the functionality of the base system from the USA required modifications that were much greater than envisaged":0,\
  "An audit of the project found a lack of planning and criticized the project for failing to do sufficient analysis before making key strategic decisions ":0,\
  "A project aimed at providing live camera links from police cars and other fixed locations to a central command location fails to achieve the desired results":0,\
  "Equipment failures, poor planning and poor training mean that as a integrated whole the system was worthless":0,\
  "the data collected through the system is of questionable value":0,\
  "The implementation of a package system from a Canadian company ran into difficulty due to the complexity of integrating it with other existing systems":0,\
  "In an incident that drew worldwide attention, J.P. Morgan lost billions of dollars in the so called London Whale incident":0,\
  "the dimensions and weight of the watercraft meant they were unsuitable to be launched from these ships":0,\
  "As with many large scale IT projects, the project did not proceed as planned":0,\
  "The phase one delivery schedule slipped again":0,\
  "Despite the extensions the project continued to have difficulties":0,\
  "the system caused significant operational issues":0,\
  "This painful deployment period lasted until Feb 2002 and only at that point was a manageable degree of operational stability reached":0,\
  "EDS had not done sufficient due diligence in submitting their bid ":0,\
  "there was a gap between BSkyB’s expectations and what actually transpired":0,\
  "the court case reports Excel calculation errors which resulted in under bidding on price":0,\
  "City’s new time recording system for employees goes 10 times over budget and is delivered 6 month late":0,\
  "investigations reveal suspected fraud":0,\
  "Company in CityTime Payroll Scandal to Pay $500 Million":0,\
  "The United Kingdom abandons 9 newly constructed regional fire control centers and scraps plans to reorganize by centralizing fire dispatch functions":0,\
  "the phone lacked some basic functions that users required":0,\
  "Microsoft pulls the plug on Kin":0,\
  "A review by the Auditor-General questioned whether the project could now deliver any value to the residents of Victoria":0,\
  "Already 4 years behind schedule, the initial pilot releases in London England were branded a shambles":0,\
  "failure to address culture change issues interacted with technical faults to produce weeks of chaos at hospitals":0,\
  "hospitals wait for the problems to be resolved before allowing the rollout to proceed":0,\
  "Department of Health announces that efforts to centralize health records has now been abandoned":0,\
  "Original scope and cost of project was radically underestimated":0,\
  "Hospital boss appologises for NHS IT problems ":0,\
  "First London NHS care records rollout causes chaos":0,\
  "NHS care record rollout grinds to a halt":0,\
  "Project to modernize and consolidate Sydney Water’s Customer Management Systems runs into trouble":0,\
  "Project is delayed by 18 months and exceeds its original budget by more than 100%.":0,\
  "Reports indicate that is is not the first troubled project for Sydney Water":0,\
  "a project to modernize the customer information and billing system was cancelled once it had run over budget by four fold":0,\
  "Banks lost millions on digital cheque project":0,\
  "Efforts to implement a new customized reservations system cancelled amid delays and quality concerns":0,\
  "Unfortunately the switch is reported to have caused on going problems for customers":0,\
  "Westjet debacle shows why business must have disaster plans":0,\
  "WestJet Announces Suspension of aiRES Implementation ":0,\
  "That project has become a classic case study in project failure":0,\
  "London Stock Exchange to abandon failed Windows platform ":0,\
  "London Stock Exchange Crippled by Outages":0,\
  "VA cites ineffective code as the reason for cancellation":0,\
  "After seven years of development the Veterans Affairs (VA) Replacement Scheduling Application (RSA) is scrapped":0,\
  "The systemic nature of the problems has resulted in a further 45 poorly performing projects being put on hold pending review":0,\
  "Problems logging in, problems making payments and problems reserving a machine have resulted in some smelly students in the Oslo area":0,\
  "Pentagon cancels work on Marine One helicopter project":0,\
  "the project was first put on hold and then cancelled by the newly elected Obama administration in early 2009":0,\
  "Efforts to integrate prison and probation systems from different local authorities into one national system fail":0,\
  "Poor supplier management practices":0,\
  "System designed to share intelligence between separate groups in the UK intelligence gathering community is cancelled due to technical concerns":0,\
  "The British are not alone in having troubles sharing information between intelligence agencies":0,\
  "Following the 2009 global financial collapse and the decline in real estate prices the lender defaulted on their obligations leaving the project unfunded":0,\
  "Following more than 3 years of development effort, Air Canada suspends its efforts to implement a next-generation air reservation and departure control system":0,\
  "Air Canada suspends implementation of next-gen reservation system":0,\
  "US terror threat system crippled by technical flaws":0,\
  "Implementation of a new on-line ticketing tool fails the day after production release":0,\
  "Seven weeks later after repeated outages, not a single ticket had been mailed out":0,\
  "Breakdown in advanced sales result in cash flow problems for organizers, venues and performers leading to claims for compensation":0,\
  "Organization responsible for the new system forced into administration following the debacle":0,\
  "Volume related performance problems":0,\
  "Edinburgh Fringe faces ticketing turmoil as e-booking system collapses":0,\
  "Edinburgh Fringe ticket site dead as a parrot":0,\
  "Another box office disaster as Fringe ticket firm goes bust ":0,\
  "Errors in the software and the processes used for handling data result in over payment of billions of dollars worth of tax credits for parents with children in the United Kingdom":0,\
  "On discovering the errors, government efforts to reclaim the money result in hardship for many of Britain’s poorest families":0,\
  "Software glitches at heart of £2.8bn tax credit fiasco":0,\
  "Programming / calculation errors embedded in the software":0,\
  "navigation between pages resulted in lost data and hence incorrect data in the system":0,\
  "Problems with local property tax collection system result in $260M worth of payments going uncollected":0,\
  "Calculation errors result in one person receiving a disability allowance of £2.9M":0,\
  "System lacked basic functions such as the ability to send late payment notices or initiating collection proceedings if payment not received":0,\
  "Audit and internal control functions serious compromised resulting in serious fraud concerns":0,\
  "Failure to deliver the helicopters for operational use leaves a critical gap in the British military capability in Afghanistan":0,\
  "Efforts to correct the situation abandoned and helicopters converted back to regular operations":0,\
  "Shifting operational missions combined with slow progress rendered certain key strategic decisions worthless resulting in project resets":0,\
  "Lack of planning and underestimation cited as a primary contributors to a 9 year delay in the full deployment of the Criminal Justice Enhancement Program (CJEP) for use by the Australian Justice department":0,\
  "Justice IT project 9 years late":0,\
  "An inadequate business case which contributed to poor scoping of the project and a failure to identify realistic funding requirements":0,\
  "Development and implementation issues associated with contractor performance":0,\
  "Smart card system to allow bus, rail and tram travel on a single ticket delayed by as much as 5 years and over budget by between $200M and $350M depending on press reports":0,\
  "In 2007 a similar project was cancelled in Sydney Australia (TCARD)":0,\
  "Myki delayed in $216m hit":0,\
  "Program to improve efficiency in the UK’s Department of Transport ends up costing more than it saves":0,\
  "A May 2008 study the the UK National Audit Office however finds the projects is in deep trouble and that the project will actually cost $160M more than it saves":0,\
  "The Department for Transport planned and implemented its shared corporate services project with stupendous incompetence":0,\
  "Excessive schedule pressure resulting in inadequate procurement and testing":0,\
  "Opening of Heathrow Terminal 5 labeled a fiasco after 28,000 bags get lost and hundreds of flights are cancelled":0,\
  "Problems resulted in British Airways having to cease accepting passengers with bags to check-in while a backlog of thousands of passengers built up in the terminal":0,\
  "Problems persisted for more than a week drawing attention of the media from around the world":0,\
  "Enterprise Resource Planning system implementation fails to meet needs":0,\
  "Who’s to Blame For Failed ERP Project that Prompted SAP Lawsuit":0,\
  "a system that the engineers deemed to be unusable once it was launched":0,\
  "the system is dumped and a new system introduced":0,\
  "the failure to engage the right stakeholders resulted in the total rejection of the project and the need to start from scratch with a replacement":0,\
  "Jetsmart dumped as Qantas nets Marlin":0,\
  "$40M Qantas parts system flop":0,\
  "Smart card transit project to allow single ticket across train, ferry and bus transit cancelled after years of delays and cost overruns":0,\
  "System riddled with software faults":0,\
  "Scandal of $60m wasted on Tcard":0,\
  "Tcard smartcard project scrapped":0,\
  "New system to unify Army, Navy and Air Force payrolls results in a deluge of complaints about missing pay, incorrect pay and bungled allowances":0,\
  "Failure to address culture change issues":0,\
  "New airline passenger reservation system cancelled after 2 years of work":0,\
  "Lufthansa Systems ceases development on FACE passenger management platform":0,\
  "Lufthansa Annual Report 2007 acknowledging cancellation":0,\
  "we could no longer assume that we would be able to provide our customers with a product that would meet their requirements within a reasonable time frame and at reasonable costs":0,\
  "Special panel to investigate pension fiasco":0,\
  "Junior doctors forced to reapply directly to hospitals after a new centralized system for matching doctors and postings disintegrates":0,\
  "Publicity of the problems resulted in journalists identifying significant security flaws that allowed them to see confidential data":0,\
  "Government later forced to admit system was seriously flawed":0,\
  "Government eventually ditches the system altogether":0,\
  "Hewitt apology for training chaos":0,\
  "When the new system was switched on reports indicate that production was thrown into chaos resulting in disruption to cash flow and ultimately a liquidity crisis":0,\
  "reports indicate serious deficiencies that affected the cut-over resulting in loss of information and severe operational disruption":0,\
  "Firetruck maker files for bankruptcy":0,\
  "Implementation results in chaos when system cannot handle volume of data being processed":0,\
  "Registry offices officially told to abandon the system after just 2 months of use":0,\
  "Chaos as registry offices are told to abandon computer system":0,\
  "Registry office meltdown":0,\
  "Replacement for a 1970’s system used for tracking unemployment claims cancelled after only 1 of 7 phases is successfully completed":0,\
  "Customization proves to be more complex than anticipated and project is cancelled after the $10M spent on phase 2 fails to deliver a working system":0,\
  "Failure to review business process prior to starting the project and an unwillingness to adapt business processes to match functionality available in the packaged system":0,\
  "State scraps computer project":0,\
  "Efforts to combine billing systems for electrical and gas supply into a single system dissolve into a shambles":0,\
  "Level of manual intervention required to handle billings exceeds ability of staff to keep up with the system":0,\
  "Inadequate computer hardware":0,\
  "Failure to integrate the system properly":0,\
  "British Gas sues Accenture over billing shambles":0,\
  "New payroll system goes seriously wrong":0,\
  "Problems lead to $53M in over payments to state employees and an additional $37M is spent to get the system working correctly and cover costs due to the problems caused":0,\
  "No accounting for L.A. Unified’s payroll fiasco":0,\
  "it becomes clear the project has headed off in the wrong direction":0,\
  "early problems left the project fatally flawed":0,\
  "DHS Scuttles Emerge2 Program":0,\
  "Emerge2’s failure sends DHS back to the drawing board":0,\
  "In what may be the worst budget overrun in history, the costs to implement a registry of firearms balloons from $2M to $860M":0,\
  "Radical underestimation of complexity and scope of project":0,\
  "Justice Department failed to communicate cost overruns to parliament":0,\
  "Payroll and benefits system project is abandoned after 5 years of effort":0,\
  "Regents were in dark on failed IT project":0,\
  "Australian Navy first grounds (May 2006) and then scraps (Mar 2008) a fleet of 10 helicopters because of safety concerns arising from the avionics software used":0,\
  "Problems integrating 1960’s airframes with modern avionics software ":0,\
  "Failure to develop software in accordance with Australian defense standards resulted in a failure to gain full air worthiness certification":0,\
  "Technical problems ground navy helicopters":0,\
  "Lack of management and poor decision making cause DEFRA to miss implementation deadline exposing the UK to possibility of significant EU fines":0,\
  "Failure to make payments on schedule leaves farmers without required cash flow resulting in financial hardship":0,\
  "a failure by the management team to face up to the unfolding crisis":0,\
  "Two top officials blamed by MPs for farm cash fiasco":0,\
  "Ambitious program to replace paper based reporting of crimes and investigations with an online system is scrapped":0,\
  "the project was in serious trouble and was eventually deemed unfit for use":0,\
  "the baggage handling system at the new Denver International Airport was to become one of the most notorious examples of project failure":0,\
  "the problems building the system resulted in the newly complete airport sitting idle for 16 months while engineers worked on getting the baggage system to work":0,\
  "Even the portion of the system that was implemented never functioned properly and in Aug 2005 the system was scrapped altogether":0,\
  "After just a few months in service the complete fleet was withdrawn from service":0,\
  "Even the auction process is said to have been flawed":0,\
  "1999 Auditors report hinting at the problems to come":0,\
  "initial reaction from the press was poor":0,\
  "Delays in delivery and the failure to fully realize the business benefits results in the organization being unable to profitably service contracts it had entered into":0,\
  "When the system was delayed and when it failed to meet performance requirements the company was unable to service the contract profitably and cash flow issues forced the company into Chapter 11 bankruptcy":0,\
  "Fox-Meyer blames the problem on the integrator and suppliers they had engaged to perform the work":0,\
  "What was to be the world’s largest automated airport baggage handling system, became a classic story in how technology projects can go wrong":0,\
  "Despite the good intentions the plan rapidly dissolved":0,\
  "the system never worked well":0,\
  "those making key decisions underestimated the complexity involved":0,\
  "Accepting these changes into a project that was already in deep trouble raises some further troubling questions":0,\
  "it began to undermine the performance goals the system was trying to meet.":0,\
  "Following the embarrassing public demonstration to the press in Apr 1994,":0,\
  "The demonstration had been an unmitigated disaster":0,\
  "the disastrous demonstration of the system had shown to the world how bad the state of the project really was":0,\
  "the project suffered many other difficulties":0,\
  "the electrical system suffered from power fluctuations that crashed the system":0,\
  "Mr Slinger’s replacement lacked the in depth engineering knowledge required to understand the system":0,\
  "the business thrived up until the 1970s, but following the Air Transportation Deregulation Act of 1978, it fell into a downward spiral":0,\
  "By 1989 the company was forced into bankruptcy":0,\
  "rising oil prices led to a decline in sales":0,\
  "the company's failure to withstand turbulent times was its death knell":0,\
  "the airline ceased operations in December 1991":0,\
  "Despite attempting a relaunch under the name Commodore USA between 2010-2013, the brand ultimately went defunct":0,\
  "the company filed for bankruptcy":0,\
  "In July 2002, WorldCom filed for bankruptcy":0,\
  "the product performed poorly":0,\
  "the brand was restricted to a small number of budget models until it was quietly discontinued in 2013":0,\
  "Unable to turn the business around, Woolworth’s announced in July 1997 it would close more than 400 five-and-dime stores in the US":0,\
  "the chain was forced to go bankrupt in September 2017":0,\
  "deliveries failed to leave its depot":0,\
  "The failure was blamed on poor management and understaffing":0,\
  "United Airlines took a huge reputational hit":0,\
  "All music uploaded to the site before 2016 plus photos and videos were lost after a faulty server migration":0,\
  "The app-based taxi service Uber has been beset by PR disaster after PR disaster since its launch in 2011":0,\
  "Toyota has been forced to issue a number of recalls in recent years":0,\
  "The Japanese firm also recalled millions of vehicles over the summer of 2016,":0,\
  "the company's reputation is in tatters":0,\
  "its share price has plummeted ":0,\
  "the firm potentially faces billions of dollars in fines from the US Justice Department and the EU":0,\
  "the backlash was swift and brutal":0,\
  "some thought the campaign was naive and patronising":0,\
  "leading to a drop in sales and a dip in its share price":0,\
  "Hoover UK eventually lost millions as a result of the promo":0,\
  "Ratner's misjudged remarks hit sales hard":0,\
  "Two Western states spent the 1990s attempting to computerize their departments of motor vehicles, only to abandon the projects after spending millions of dollars.":0,\
  "the new system was slower than the one it was designed to replace":0,\
  "an unworkable system that could not be fixed without the expenditure of millions more":0,\
  "the system promptly ran into what were then described as horrendous barcode-reading errors":0,\
  "Two years later, the entire project was scrapped, and Sainsbury's wrote off £150 million in IT costs":0,\
  "In April 2005, SAIC delivered 700,000 lines of code that the FBI considered so bug-ridden and useless that the agency decided to scrap the entire VCS project":0,\
  "Congress learned that the pilot project was being delayed":0,\
  "PSA Airlines, a wholly owned subsidiary of American Airlines, experienced a problem with its crew scheduling and tracking system that led to nearly 3,000 flights being cancelled over seven days in June, and cost the airline an estimated US $35 million":0,\
  "Spirit Airlines had multiple IT issues in 2018, including problems in February and March":0,\
  "A Southwest Airlines computer problem with its gate and lobby check-in systems at LAX in January lasted more than three hours, causing hundreds of flight delays across its system":0,\
  "Delta Airlines had a three-hour “physical device issue” in September, causing a system-wide ground stop for more than an hour and the delay of some 600 flights":0,\
  "Air Canada experienced two network-related failures in February and March":0,\
  "British Airways suffered a world-wide computer system problem in July and another computer issue at London Heathrow Terminal Five in September":0,\
  "An air traffic control computer failure at the Eurocontrol centre in Brussels delayed an estimated 14,000 European flights in April":0,\
  "the U.S. Customs and Border Protection computer systems experienced an outage, leaving thousands of international passengers across the country in long queues waiting to clear customs":0,\
  "Fiat Chrysler recalled 5.3 million multiple car models for a cruise control issue":0,\
  "GM recalled one million pickups and SUVs to fix a steering problem":0,\
  "Google decided in October to close its Google Plus social network because of a security flaw":0,\
  "A botched migration to a new software platform in April at TSB bank in the United Kingdom caused major disruptions for weeks, angered the bank’s 5 million customers, and eventually led to the resignation of its CEO":0,\
  "Minnesota’s multi-year effort to deliver a fully functional vehicle and driver services system continues to have annoying problems":0,\
  "The U.S. Coast Guard finally admitted defeat after spending $67 million in its mismanaged attempt to develop an electronic health record":0,\
  "German supermarket company Lidl decided in July to scrap an ineffective three-year old merchandise management system after spending more than $565 million on it":0,\
  "Amazon suffered glitches for several hours in July when demand exceeded expectations on Prime Day":0,\
  "Demand also couldn’t be met by KFC in the United Kingdom after the failure of the logistics management system at its new supplier caused it to shut down 470 stores for several days because of a lack of chicken to fry":0,\
  "There is not a compelling enough value proposition, or compelling event, to cause the buyer to actually commit to purchasing":0,\
  "There is little or no market for the product that they have built":0,\
  "The market timing is wrong":0,\
  "The market size is simply not large enough":0,\
  "entrepreneurs are too optimistic about how easy it will be to acquire customers":0,\
  "it rapidly becomes an expensive task to attract and win customers":0,\
  "An incredibly common problem that causes startups to fail is a weak management team":0,\
  "building a product that no-one wants to buy":0,\
  "they failed to do enough work to validate the ideas before and during development":0,\
  "This can carry through to poorly thought through go-to-market strategies":0,\
  "They are usually poor at execution":0,\
  "this leads to issues with the product not getting built correctly or on time":0,\
  "the go-to market execution will be poorly implemented":0,\
  "They will build weak teams below them":0,\
  "the rest of the company will end up as weak, and poor execution will be rampant":0,\
  "A major reason that startups fail is because they ran out of cash":0,\
  "management did not achieve the next milestone before cash ran out":0,\
  "What frequently goes wrong, and leads to a company running out of cash, and unable to raise more":0,\
  "Another reason that companies fail is because they fail to develop a product that meets the market need":0,\
  "the product will be way off base, and a complete re-think is required":0,\
  "Dwelling or being married to a bad idea can sap resources and money as well as leave employees frustrated by a lack of progress":0,\
  "We were caught mid-pivot – half way between a strategy we knew wouldn’t work and one which we believed could be successful but was not able to be aggressively pursued":0,\
  "This was a very difficult place to be both professionally and personally":0,\
  "We were extremely frustrated at not being able to properly go after our new strategy and every day that passed without meaningful progress was one step closer to the failure of my first company":0,\
  "Even though we put everything we had into getting through this phase we were never able to make it through the pivot":0,\
  "the risk of burning out is high":0,\
  "entrepreneurs who said they did not properly utilize their own network":0,\
  "I think we made the mistake early on of trying to do (and know) everything ourselves":0,\
  "We received a notice from them informing us we weren’t compliant and unless we removed it they’d suspend our affiliate account":0,\
  "It’s an incredibly expensive venture to pursue and a hard industry to work with":0,\
  "We had to shut down our growth because we couldn’t launch internationally":0,\
  "a number of startup founders explicitly cited a lack of investor interest":0,\
  "The software and concept simply didn’t scale beyond its physical borders":0,\
  "lack of teamwork and planning could lead to failure":0,\
  "The most significant drawback to a remote team is the administrative hassle":0,\
  "it was a major annoyance and distraction":0,\
  "9% of startup post-mortem founders found that a lack of passion for a domain and a lack of knowledge of a domain were key reasons for failure no matter how good an idea is":0,\
  "I think it’s fair to say we didn’t really care about journalism":0,\
  "Or they can start you down the wrong road":0,\
  "Pivoting for pivoting’s sake is worthless":0,\
  "Discord with a cofounder was a fatal issue for startup post-mortem companies":0,\
  "when things go bad with an investor, it can get ugly pretty quickly":0,\
  "surrendered market leadership and thought leadership":0,\
  "a vastly higher cost structure":0,\
  "Getting sidetracked by distracting projects, personal issues, and/or general loss of focus":0,\
  "Ultimately when we came back from SXSW, we all started losing interest":0,\
  "If you release your product too early, users may write it off as not good enough":0,\
  "getting them back may be difficult if their first impression of you is negative":0,\
  "if you release your product too late, you may have missed your window of opportunity in the market":0,\
  "we moved faster than our customers could move":0,\
  "We moved with tech that wasn’t really ready for them – ie, with 32-bit when they wanted 64-bit.":0,\
  "We moved when the operating-system environment was still being fleshed out":0,\
  "We were too early":0,\
  "Ignoring users is a tried and true way to fail":0,\
  "We spent way too much time building it for ourselves and not getting feedback from prospects":0,\
  "Tunnel vision and not gathering user feedback are fatal flaws for most startups":0,\
  "We didn’t spend enough time talking with customers":0,\
  "we didn’t gather enough input from clients":0,\
  "We didn’t realize it until it was too late":0,\
  "It’s easy to get tricked into thinking your thing is cool":0,\
  "an inability to market was a common failure":0,\
  "founders who liked to code or build product but who didn’t relish the idea of promoting the product":0,\
  "Then we hit the ceiling of what we could achieve effortlessly":0,\
  "Unfortunately no one of us was skilled in that area":0,\
  "Even worse, no one had enough time to fill the gap":0,\
  "failing to find ways to make money at scale":0,\
  "staying wedded to a single channe":0,\
  "investors hesitant":0,\
  "founders unable to capitalize on any traction gained":0,\
  "Although we achieved a lot with Tutorspree, we failed to create a scalable business":0,\
  "Tutorspree didn’t scale because we were single channel dependent":0,\
  "we didn’t have money to spend on acquisition":0,\
  "Bad things happen when you ignore what a users wants and need":0,\
  "Ultimately I believe PMOG lacked too much core game compulsion to drive enthusiastic mass adoption":0,\
  "Looking back I believe we needed to clear the decks":0,\
  "The concept was too abstruse for the bulk of folks to take up.":0,\
  "the difficulty in pricing a product high enough to eventually cover costs but low enough to bring in customers":0,\
  "We just didn’t deliver up to their expectation":0,\
  "Delight IO saw this struggle in multiple ways":0,\
  "ignoring them was also a recipe for failure":0,\
  "Between the worse data aggregation method and the much higher amount of work Wesabe made you do":0,\
  "But none of them matter if the product is harder to use":0,\
  "they shouldn’t be founding a startup":0,\
  "the founding team can’t put out product on its own":0,\
  "the founding team wished they had more checks and balances":0,\
  "I didn’t have a partner to balance me out and provide sanity checks for business and technology decisions made":0,\
  "the underlying problem":0,\
  "running out of cash":0,\
  "the company wasn’t able to raise this additional funding.":0,\
  "what eventually killed Flud":0,\
  "Flud eventually ran out of money":0,\
  "Tackling problems that are interesting to solve rather than those that serve a market need":0,\
  "we had no customers":0,\
  "no one was really interested in the model we were pitching":0,\
  "Startups fail when they are not solving a market problem":0,\
  "We were not solving a large enough problem that we could universally serve with a scalable solution":0,\
  "what we didn’t have was technology or business model that solved a pain point in a scalable way":0,\
  "where we went wrong":0,\
  "Not mobile friendly":0,\
  "Difficult to integrate with ecommerce systems":0,\
  "Most customers abandon configurators because they get creatively frustrated":0,\
  "These legacy problems lead to really low sales conversion rates for custom-coded configurators":0,\
  "we had  accidentally built a services company":0,\
  "We couldn't find a way to standardize customization":0,\
  "We just couldn't make the economics work":0,\
  "the quality of leads was really bad":0,\
  "we still struggled to ship the configurator quickly":0,\
  "we confused interest with traction":0,\
  "which was encouraging, but often didn’t lead to money in the bank in the short-term":0,\
  "long sales cycle and lots of red tape which we couldn’t afford to deal with":0,\
  "They will bleed you dry":0,\
  "Most clients who are dealing with rubbish code end up deciding to keep babysitting it rather than ripping and replacing it":0,\
  "a pain in the ass and prone to complication":0,\
  "they never spend any money promoting it and it goes unused and is left to die":0,\
  "not optimized for sales":0,\
  "a dying industry":0,\
  "It’s probably a bad sign when you don’t have any direct competitors":0,\
  "One reason generizing the configurator is problematic":0,\
  "why marketplaces like Zazzle, CafePress, and eBay struggle":0,\
  "the project management nightmare":0,\
  "Probably the biggest reason we failed":0,\
  "they dropped the ball because the project wasn’t dead simple":0,\
  "I don’t think we ever used the same CSS, design, ecommerce, or image creation vendor twice because they all suck":0,\
  "Configurators are too complex to standardize":0,\
  "technology doesn't necessarily solve the right problem for the customer":0,\
  "some of our client projects were not finished after as long as TWO YEARS":0,\
  "Often the project was out of our control after we did the heavy-lifting":0,\
  "clients just left it hanging":0,\
  "It's so frustrating to not control the button that pushes the build live":0,\
  "We really build a platform for configurator engineers, which was another fatal flaw":0,\
  "we mistakenly thought if we served his need we would serve the market’s need":0,\
  "The wrong problem":0,\
  "We mistakenly thought the primary problem to solve was guidance":0,\
  "Never make your customers do hard work":0,\
  "they quickly get frustrated and seek out expert recommendations":0,\
  "The main headache was the manufacturing process":0,\
  "clients were using something bloated and archaic like NetSuite":0,\
  "a few horror stories that we experienced on the sales side":0,\
  "In the end we just couldn’t accept those terms":0,\
  "Startups fail when they are not solving a market problem":0,\
  "We were not solving a large enough problem that we could universally serve with a scalable solution":0,\
  "Many startups do not realize that customization per se provides no customer value":0,\
  "Bad execution and no scalable fulfillment systems":0,\
  "I saw several startups killed by their own success":0,\
  "they couldn't deliver when lots of orders came in after a big press hit":0,\
  "No focus on a great consumer choice process":0,\
  "many MC startups do not really implement all the factors":0,\
  "not mastering the difficult change management process required there":0,\
  "it's not scalable":0,\
  "veer off into a death spiral":0,\
  "never reaching your business idea's potential":0,\
  "To miss the gail winds is to lose the race":0,\
  "they don’t understand positioning":0,\
  "network randomly, without focus":0,\
  "Do not waste money getting fancy office-space and furniture":0,\
  "You might fail because you haven't come up with a solid Problem/Solution fit":0,\
  "rushing to grow without any hints of a fit":0,\
  "you don't have a user feedback loop strategy in place":0,\
  "Little or no knowledge of pricing":0,\
  "lack of proper budgeting and operational mismanagement drains start-up capital and sales revenue":0,\
  "lack of clear focus":0,\
  "an idea will sink in a wake of frustration":0,\
  "Did they misjudge the fundamental risk at the outset":0,\
  "Did the team succumb to groupthink and thereby overestimate their own probability of success":0,\
  "fundamental misjudgments":0,\
  "unforeseen environmental changes":0,\
  "you fail to change your original idea upon realizing that things are not going as planned":0,\
  "most startup failure revolves around people issues":0,\
  "No demonstrated user need":0,\
  "Management that doesn't really care for the employees":0,\
  "A team that has a hard time being pragmatic will spend a lot of their time and money on shit that doesn't matter":0,\
  "Despite all that most ideas never succeeded":0,\
  "New ideas fail everywhere with a high probability":0,\
  "Walmart entered ecommerce late as they believed people were not likely to buy through computers":0,\
  "There is no process to hold the discipline and no brand to lean on":0,\
  "There is no real HR process to manage talent and no good financial management":0,\
  "the executives have no experience wading through tough times":0,\
  "There is no established relationship with customers and no established channels":0,\
  "Product quality is often poor in the early days and customer support not as professional":0,\
  "the endless supply of amateurs that fall victim to the siren's enticing call":0,\
  "These people have no idea about how to price products ":0,\
  "I know they are pitfalls because I have fallen into them all":0,\
  "advisers who can single-handedly wipe out your budget and ability to spend money where it matters most":0,\
  "The cost of compliance at the outset can cripple a cafe in such a way that they never really recover":0,\
  "the order taking and payment system is not efficient":0,\
  "you begin the slow spiral slide into failure":0,\
  "you can go broke being obsessed with profit":0,\
  "an unsuitable location can be the single biggest reason why cafes fail":0,\
  "Add to this some poor pricing strategies and you set up a guaranteed failure":0,\
  "your customers have to spend a long time finding you or looking for parking":0,\
  "Things have been bleak internally as well during the last two years":0,\
  "the debt and liabilities on its stressed balance sheet":0,\
  "Educomp’s net profit margin has fallen 61 percent during the last four years;":0,\
  "four consecutive company secretaries would resign":0,\
  "Educomp missed contractual deadlines for installation and commissioning":0,\
  "many schools across the country weren’t paying it in time":0,\
  "That’s too much to bear":0,\
  "Analysts and investors were aghast":0,\
  "That was the beginning of the downfall of their stock":0,\
  "this was a clear example of a promoter who was pursuing an unsustainable path":0,\
  "they still have a mountain of debt to cross":0,\
  "it’s a toxic wasteland from a security perspective":0,\
  "WordPress is the outdated disaster behind most of the world’s websites":0,\
  "that’s where most of the existing security and performance problems live":0,\
  "WordPress doesn’t scale horizontally like a modern application and it has no real security baked in":0,\
  "It’s awful":0,\
  "I started to feel there was something seriously wrong in early October":0,\
  "the road went nowhere":0,\
  "nobody came back to us":0,\
  "it was confusing, poorly explained or too complicated":0,\
  "it was becoming internally confusing what we offering on any given day":0,\
  "it was clear they didn’t want to hear from us anymore":0,\
  "their answer effectively ended the business":0,\
  "We could never get to that first paying customer":0,\
  "my million-dollar valuation evaporated":0,\
  "Security products are impossible to sell":0,\
  "People won’t pay for it":0,\
  "they don’t understand the problem":0,\
  "large companies will never try anything new":0,\
  "solving a problem nobody has":0,\
  "We had only wasted our own time and about a thousand dollars between the three of us":0,\
  "There is an apathy in the marketplace":0,\
  "Unfortunately, it is very common in the startup world that a venture has to close down":0,\
  "The market wasn’t ready,":0,\
  "The product wasn’t ready":0,\
  "We were burning through cash too quickly":0,\
  "a bad place to be":0,\
  "the idea is never going to make it":0,\
  "we realized that the program wasn’t meeting the high standards it required":0,\
  "we couldn’t assure the scale or quality of the program on the ground":0,\
  "everyone who looked in at us could see our dismay":0,\
  "a challenge we couldn’t meet":0,\
  "I could see that they were making reckless decisions":0,\
  "nearly running the company into the ground":0,\
  "I realized that I had failed in my role":0,\
  "the firm wasn’t acting in the best interest of the company":0,\
  "This resulted in two major customers terminating their agreement with the company":0,\
  "which prompted a series of lawsuits":0,\
  "we couldn’t undo the damage":0,\
  "Money Centers of America Inc had a major crisis":0,\
  "this crushed my spirit and dampened my motivation to keep going":0,\
  "It was a very frustrating and dark place to be in":0,\
  "If you’re focusing all your time on the wrong things, you end up going nowhere, burning out":0,\
  "They run out of money, or they have some sort of founder breakup":0,\
  "He failed to execute several tasks that he assigned to himself":0,\
  "He cracked under slightest pressure":0,\
  "He would compromise all of the business in a critical situation":0,\
  "They are not representing the real picture":0,\
  "First I failed with my co-founder and then I failed again with my hire":0,\
  "I tried to sell my product to academia and no one was interested":0,\
  "We have applied to both Y Combinator and TechStars and got rejected":0,\
  "I pitched many times and couldn’t raise the money":0,\
  "It felt bad":0,\
  "I was extremely ignorant and had no idea what I was doing":0,\
  "the delivered service no longer complies with the specifications":0,\
  "An abandoned NHS patient record system has so far cost the taxpayer nearly £10bn":0,\
  "new regional IT systems for the NHS, introduced to replace the National Programme for IT, are also being poorly managed":0,\
  "This saga is one of the worst and most expensive contracting fiascos in the history of the public sector":0,\
  "years behind schedule and over budget":0,\
  "The project was launched in 2002 but was beset by changing specifications, technical challenges and disputes with suppliers":0,\
  "it would eventually be canceled and the work products abandoned":0,\
  "a major IT project can go so far off the tracks that nothing useful is ever delivered":0,\
  "found problems on every page he selected":0,\
  "it is not producing world-class, or even minimally-professional, results":0,\
  "What the team is producing will not only be very difficult to support and modify, it will in all likelihood be unusable":0,\
  "Project planning and execution is all to often poor or missing completely":0,\
  "Necessary and useful activities are delayed or canceled ":0,\
  "You lose credibility and influence":0,\
  "FUBAR is massively late":0,\
  "There appears to be a systemic inability to establish good testing criteria ":0,\
  "The defect tracking process is poor":0,\
  "crippling its own core business":0,\
  "BigFirm leaves itself open to potential liabilities":0,\
  "the effort to transition directly into the Rational Unified Process (RUP) is not being given sufficient time and will likely grind development to a halt":0,\
  "FUBAR doesn’t have a viable, consistent architecture":0,\
  "a problem that has been made big, complex, and possibly unsolvable in the current implementation":0,\
  "FUBAR never stabilizes enough to go into production for any length of time, or if it does, proves to be extremely difficult to support or enhance":0,\
  "FUBAR was never properly architected and designed for the performance required":0,\
  "developers are having to scale the performance of and debug a seriously flawed application at the same time":0,\
  "that will probably make the application even more difficult to modify and support":0,\
  "Many of the people involved in FUBAR — developers, testers, team leads, managers — lack the qualifications, insight, or experience to make FUBAR a success":0,\
  "The project is overstaffed for the actual complexity of FUBAR":0,\
  "poor quality of work, poor quality assurance, poor scheduling and delivery, poor architecture, poor application performance":0,\
  "the qualified people become frustrated and leave":0,\
  "the plane will crash and people will die":0,\
  "a fallacy, and one that costs corporations millions (if not billions) of dollars a year in missed schedules and failed projects":0,\
  "There isn’t enough intellectual honesty within the FUBAR project":0,\
  "you run the very real risk of looking dishonest or incompetent":0,\
  "there are some profound problems and flaws with the FUBAR project that will not go away until the project team acknowledges and addresses them":0,\
  "In fact, it is probably one of the worst computer languages in terms of complexity":0,\
  "you get an idea of how far insanity can reach in the realm of software engineering":0,\
  "Check-in needs to go through a painful procedure":0,\
  "given the abysmal quality of this thing":0,\
  "Technical knowledge is low":0,\
  "We lost all our money":0,\
  #start self-generated here
  "We lost everything":0,\
  "No one liked the product":0,\
  "The company went under":0,\
  "It kept crashing":0,\
  "Eventually we gave up":0,\
  "He gave up":0,\
  "It went out of business":0,\
  "It lost too much money":0,\
  "{People/Potential customers/participants} {were not interested/did not understand it/found it too complicated/did not want it/did not care}":0,\
  "No one {wanted it/wanted to buy it/cared/was interested/wanted to try it/liked it/wanted to listen}":0,\
  "{We/They/he/she/the group} {lost confidence/couldn't find a market niche/lost interest/lost motivation}":0,\
  "{We/They/he/she/the group}  ran out of {new/good/} {ideas/plans/strategies/things to try/approaches}":0,\
  "{It/the product/the app/the website/the service} failed to {take off/make any impact/get anyone's attention}":0,\
  "We had too few customers":0,\
  "It kept falling apart":0,\
  "It was hell":0,\
  "The project from hell":0,\
  "Everyone hated it":0,\
  "It was a {train wreck/disaster/mess/nightmare/car crash/total failure/catastrophe/project from hell}":0,\
  "It was nothing but trouble":0,\
  "We made so many mistakes":0,\
  "{We/he/she/the team/the company/the group/the CEO} just couldn't {do/handle/manage} {it/the work/the tasks/the responsibility}":0,\
  "{It/The project/the website/the app} did not {function/work/work well enough/work convincingly}":0,\
  "The {demo/project/prototype/webpage/MWP/new version} {failed/performed badly/was unconvincing}":0,\"
  "The {demo/project/prototype/webpage/MWP/new version} did not {impress/convince/attract} {anyone/customers/investors/paying clients/businesses}":0,\
  "It was a massive disappointment":0,\
  "Too many mistakes":0,\
  "A big step backwards":0,\
  "{A lot/too many/never-ending} {of problems/of setbacks/of failures/of performance issues/of software bugs/of crashes}":0,\
  "{We/They/he/she/the company/the product} {had/were getting/were experiencing} {negative press/bad publicity}":0,\
  "We {were missing/lacked/did not have/did not have enough of} the {time/traction/expertise/knowledge/skill/money/funding/clients/interest/paying customers/investors}":0,\
  "{We/everyone/the team} {burned out/lost interest/gave up/quit working on it/decided to kill the project}":0,\
  "It crashed":0,\
  "They ran into more and more problems":0,\
  "{He/She/We/They/The company/the group/the CEO} {made a serious mistake/were wrong about that/failed to see the problems that would result}":0,\
  "{It/the product/the company/the startup/the group} continued to {fail/underperform/fail to meet expectations}":0,\
  "{We/They/He/She/The company/The startup} ran out of {money/cash/funds}":0,\
  "{Everything/The situation} {went downhill/kept getting worse/deteriorated}":0,\
  "It all {fell apart/went to hell/broke down/went to pieces} {in the end/after a few months/at the end of the year}":0,\
  "No matter how hard {we/they/he/she/the founder} tried, {we/they/she/he} {could not/failed to/never managed to} {make money/get customers/attract interest}":0,\
  "{We/They/He/She/the CEO/the company/the group/the team} {noticed this/realized this/was/acted/took action} {much/} {too late/too slowly}":0,\
  "{We/They/He/She/The company} didn't solve a {problem/pain point/issue} that {mattered/was important/people cared about/people were willing to pay for}":0,\
  "{We/They/He/She/The company} didn't have a {sustainable/sensible/profitable} {business model/strategy/approach}":0,\
  "{We/They/He/She/The company/The product/The app/The first version} failed to {make a profit/make money/break even/return on investment/get customers/get traction} {despite extensive effort/even after months of work/}":0,\
}

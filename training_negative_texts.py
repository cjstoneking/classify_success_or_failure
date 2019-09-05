#negative texts - negative in the sense that they are the opposite of failure

training_negative_texts = {
  "{He/She/We/They} succeeded {in the end/finally/}":0,\
  "{His/Her/Our/Their/The} struggle paid off":0,\
  "it felt {great/really good}":0,\
  "{it/this/the project} was a success":0,\
  "{it/the project} was making money":0,\
  "{We/They} were rewarded":0,\
  "{He/She} was rewarded":0,\
  "{that/it} was {very/} encouraging":0,\
  "things were looking up":0,\
  "{things seemed to be going/he was doing/we were doing} {OK/alright/well/fine/better}":0\
  "positive cash flow":0,\
  "{He/She/We/They/the project} had {happy/satisfied/positive} {customers/clients}":0,\
  "{everyone/he/she} {liked it/was satisfied/was ecstatic/was thrilled/was pleased}":0,\
  "{it/the software/the demo/the project/the first version} {worked/was functional/was convincing/had people convinced}":0,\
  "{He/She/We/They/the team} had {positive results/good outcomes/some success}":0,\
  "come up with creative solutions":0,\
  "solved the {problem/issue}":0,\
  "dealt with it":0,\
  "managed to succeed":0,\
  "kept growing and getting customers":0,\
  "raised enough {capital/money/funds/cash}":0,\
  "{we/he/she/they} {assembled/found/put together} a {great/excellent} {team/group/bunch of people}":0,\
  "it all {came together/worked out/paid off}":0,\
  "hard work {paid off/was rewarded} {in the end/}":0,\
  "{we/he/she/they} won the competition":0,\
  "succeeding at any cost":0,\
  "{we/they} {finally/} {managed/were able to} to {succeed/achieve the goals}":0,\
  "{he/she/the team} {finally/} {managed/was able to} to {succeed/achieve the goals}":0,\
  "{things/it} started to {improve/get better/look up}":0,\
  "{we/they/he/she} {got/attracted/obtained/found} more {paying/} customers":0,\
  "people {liked it/were positive/were enthusiastic/loved it/thought it was great}":0,\
  "the best thing ever":0,\
  "the greatest {thing/moment}":0,\
  "it was {very/highly/extremely} satisfying":0,\
  "people we could trust":0,\
  "{we/they/the team} had strong support":0,\
  "managed to establish ourselves":0,\
  "{the product is / we are / the team is} {still going strong/doing well/performing well/making money/earning well} {at the moment/right now/}":0,\
  "{we/they/the team/everyone} kept {improving/doing better/enjoying it/loving it/liking it/making money/earning more money}":0,\
  "it {was/has been} a {great/really good/ useful/very useful/excellent/invaluable} {thing/help/resource/product/service/source of advice/mentor}":0,\
  "a winning product":0,\
  "{we/he/she/they} managed to {make everything work/get everything to work}":0,\
  "the {product/project/idea} was a {great/massive/unqualified} success":0,\
  "it all worked out":0,\
  "It’s extremely rewarding to know that we’re able to fulfil the mission we started the company for":0,\
  "we’re able to attract other talented and like-minded individuals who share this passion with us":0,\
  "a very {talented/hardworking/capable/successful/inspiring} {individual/team/group/leader/mentor}":0,\
  "it really helped a lot":0,\
  "{we/he/she/they/the team} {reached the goals/met the targets/ put together a great project/ put on a great presentation/ made a convincing show}":0,\
  "{we/he/she/they/the team/the group} {found/got/obtained} {inspiration/great ideas/encouragement/support/useful advice}":0,\
  "{we/he/she/they/the team/the group} kept {focused/believing/committed} and {it/this} {paid off/succeeded/was rewarded/was worth it} {in the end/eventually/}":0,\
  "{the struggle/the hard work/the effort} {paid off/led to success/was richly rewarded/led to a great product}":0,\
  "{eventually/after some time/after a few months}, {we were/they were/the project was} {making a profit/becoming profitable}":0,\
  "after a lot of {hard work/struggle/long nights}, {we/they} {were successful/succeeded/managed to succeed/achieved success/achieved the goals}":0,\
  "the dream became reality":0,\
  "the {product/website/service/app/first version/beta version/MWP} {took off/was successful/generated a lot of interest/started making money/attracted customers}":0,\
  "{we/he/she/they/the group} {had more/managed to get more} {clients/paying customers/revenue/income/money/success/views/hits/leads/good press/favorable press}":0,\
  "it kept growing and becoming more profitable":0,\
  "play hard for success":0,\
  "{we/they/the team} keep {loving/liking} {the work/the journey}":0,\
  "{it was/it has been} an {awesome/incredible/unforgettable/amazing} {journey/experience/adventure}":0,\
  "we've been privileged to {work with/learn from/team up with} {so many/a number of} {hardworking/talented/inspiring/committed/ highly capable} {people/individuals/guys}":0,\
  "I am fortunate in that I had a successful business that I had sold previously":0,\
  "{we/he/she/they} were {lucky/blessed/fortunate/happy/very grateful} {to have such an advantage/to have this resource/to get this funding/to get this support/}":0,\
  "being {successful/profitable/sustainable} is {hard/tough}, but we {achieved it/managed it} {in the end/finally/eventually/}":0,\
  "it was an {outstanding/incredible/amazing/superlative} {performance/product/piece of work/effort/team/group/group of people/piece of advice}":0,\
  "{it/this/this advice} {really helped a lot/was a great help/was really important for our success}":0,\
  "things were {looking up/becoming more positive/becoming more encouraging}":0,\
  "{we/he/she/they/the company} started to have the first small signs of {success/profitability}":0,\
  "it turned out to be a {winning/great/excellent} {plan/idea/strategy}":0,\
  "a {great/amazing/unbelievable} success {story/}":0,\
  "{we/he/she/they/the team} {had/experienced/found} {a stroke of luck/good fortune/success}":0,\
  "{it was/} a truly innovative and efficient {product/service/website}":0,\
  "{we had/ we were/ we found/} a {highly/very/truly/} {efficient/hardworking/reliable/excellent/committed/competent/capable/knowledgeable} {team/worker/group of people}":0,\
  "this {powered/drove/supported/was essential for/was the basis for} {all/most} of our {success/good results/achievements}":0,\
  "{belief in ourselves/trust/comittment/stubbornness/willpower/sheer will} kept {us/the team} going, and we succeeded {in the end/eventually/after many months/after some effort/}":0,\
  "{it all worked out/it was a success} despite the challenges":0,\
  "{we/the team} kept {learning/improving/getting better/making money/growing}":0,\
  "{we/the team/he/she} managed to build a product that {people/customers/clients/businesses/vendors} {liked/loved/wanted to use/ wanted to pay for/enjoyed}":0,\
  "{we/he/she/the team} {enjoyed/loved/really liked} {it/everything/every minute of it}":0,\
  "{we/he/she/the team} {managed/were able to} {develop/grow/nurture/sustain} a {profitable/successful/respected} {business/company/startup}":0,\
  "the startup {kept growing/kept making money/got a lot of positive attention}, we {sold more product/found more customers/sold more units} and succeeded":0,\
  "ultimately, {we/he/she/the team} did manage to succeed {in our goals/}":0,\
  }

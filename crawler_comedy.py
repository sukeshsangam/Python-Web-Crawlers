import urllib2
from BeautifulSoup import BeautifulSoup
import csv
import json

class EX:
	array_final=[];
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
#sample=csv.writer(open('data.csv','w'),delimiter=' ')
csvFile = open('drama.csv', 'wb')
wr = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
#for i in range(1993,2016):
for num in range(1,32):
	#page = urllib2.urlopen("http://www.imdb.com/search/title?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2406822102&pf_rd_r=195MFAS7R5Q0NRJT9JRS&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&page="+str(num)+"&ref_=adv_nxt")
	#=18
	page = urllib2.urlopen("http://www.imdb.com/search/title?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2406822102&pf_rd_r=0QBWBE41Y9HBC8CVNSHY&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&page="+str(num)+"&ref_=adv_nxt")
	soup = BeautifulSoup(page)
	#jsondata = {"ne":{ "2016":{"Post_Season":[{"RND":"DIV","Date":"Sat, Jan 14 2016","Opponent":{"Ground":"ne","Team":"Houston"},"Result":{"WinOrLose":"ne","Score":"34,16"},
	#"Passing":{"Player":"Brady","Yards":"287"},"Rushing":{"Player":"Lewis","Yards":"41"},"Receiving":{"Player":"Edelman","Yards":"137"}},{}],"Regular_Season":[]},"2017":{}},"af":{}}
	#json={}
	#postSeason=0
	#regularSeason=0
	#team="ne"
	#year="2016"
	#json[team]={}
	#json[team][year]={}
	#json[team][year]["Post_Season"]=[]
	#json[team][year]["Regular_Season"]=[]
	#for tr in soup('tr'):

	temp=soup.findAll("h3",{"class":"lister-item-header"})
	#print soup.findAll("div",{"class":"lister-item-content"})
	#print soup.findAll("h3",{"class":"lister-item-header"})
	#print soup
	#print temp
	temp_main=soup.findAll("div",{"class":"lister-item-content"})

	#print temp_main
	for div in temp_main:
		links=div.findAll('a')
		#print links[0]
		link_to="https://www.imdb.com"+links[0].get('href')
		#print link_to
		#print "hello"
		#print links[0]
		#link=links.findAll('a')
		#print link[1]
		#for i in links:
		#	print i
		span_tag=div.findAll('span')
		length=len(span_tag)
		temp_string=str(span_tag[length-2])
		if "Gross" not in temp_string:
			temp1_string=str(span_tag[length-1])
			#print temp1_string
			s0=find(temp1_string,">")
			s1=find(temp1_string,"<")
			#print s0
			#print s1
			votes=temp1_string[s0[0]+1:s1[1]]
			print votes
			gross=" "
			print gross
		else:
			temp1_string=str(span_tag[length-4])
			s0=find(temp1_string,">")
			s1=find(temp1_string,"<")
			#print s0
			#print s1
			votes=temp1_string[s0[0]+1:s1[1]]
			print votes
			temp2_string=str(span_tag[length-1])
			s0=find(temp2_string,">")
			s1=find(temp2_string,"<")
			#print s0
			#print s1
			gross=temp2_string[s0[0]+1:s1[1]]
			print gross
			
		
			
		span_str0=str(span_tag[2])
		span_str=str(span_tag[4])
		if "min" not in span_str0:
			s0=find(span_str,">")
			s1=find(span_str,"<")
			duration=span_str[s0[0]+1:s1[1]]
		else:
			s0=find(span_str0,">")
			s1=find(span_str0,"<")
			duration=span_str0[s0[0]+1:s1[1]]
		print duration
		strong_tag=div.findAll('strong')
		strong_str=str(strong_tag[0])
		r0=find(strong_str,">")
		r1=find(strong_str,"<")
		rating=strong_str[r0[0]+1:r1[1]]
		print rating
		s=str(links[0])
		
			#print s
		a=find(s,"\"")
			#print a
		link_ex=s[a[0]+1:a[1]]
		final_link=str("http://www.imdb.com"+link_ex)
		b=find(s,">")
		#print b
		c=find(s,"<")
		title=s[b[0]+1:c[1]]
		print title
		span=div.findAll('span')
		span_string=str(span[1])
		y_a=find(span_string,"(")
		y_b=find(span_string,")")
		if span_string[y_a[0]+1:y_b[0]]=='I':
			year=span_string[y_a[1]+1:y_b[1]]
		else:
			year=span_string[y_a[0]+1:y_b[0]]
		print year	
		
		paragraph=div.findAll('p')
		para_temp=str(paragraph[2])
		#print paragraph[2]
		
		
		if "Directors:" not in para_temp:
			#print "test"
			p1=para_temp.index("Director:")
			p2=para_temp.index("<span")
		else:
			p1=para_temp.index("Directors:")
			p2=para_temp.index("<span")
		#print p1
		#print p2
		Direc=para_temp[p1:p2]
		#print Direc
		soup_temp=BeautifulSoup(Direc)
		#print soup_temp
		Director_name=""
		#i=0
		for link in soup_temp:
			try:
				dd=link+"1"
				#print ""
				
			except:
				if type(link.text) == str:
					temp_name=value(link.text,"utf-8",errors="ignore")
					Director_name=Director_name+"|"+temp_name
					#print Director_name
				else:
					temp_name=(link.text).encode('ascii','ignore')
					Director_name=Director_name+"|"+temp_name
					#print Director_name
				#print "hello"
				
		print Director_name
		
		stars_name=""
		
		if "Stars" in para_temp:
			p11=para_temp.index("Stars:")
			p22=para_temp.index("</p>")
		else:
			p11=para_temp.index("Star:")
			p22=para_temp.index("</p>")
		Star=para_temp[p11:p22]
		#print Star
		soup_temp2=BeautifulSoup(Star)
		Star_name=""
		for link in soup_temp2:
			try:
				dd=link+"1"
			except:
				if type(link.text) == str:
					temp_name=value(link.text,"utf-8",errors="ignore")
					Star_name=Star_name+"|"+temp_name
					#print Director_name
				else:
					temp_name=(link.text).encode('ascii','ignore')
					Star_name=Star_name+"|"+temp_name
		print Star_name
		page_1 = urllib2.urlopen(link_to)
		soup_1 = BeautifulSoup(page_1)
		mydivs = soup_1.findAll("div",{"class":"txt-block"})
		country=""
		Budget=""
		for div in mydivs:
			temp=str(div)
			if "Country" in temp:
				#print temp
				soup_temp3=BeautifulSoup(temp)
				for link in soup_temp3:
					#print link
					try:
						dd=link+"1"
					except:
						if type(link.text) == str:
							temp_name=value(link.text,"utf-8",errors="ignore")
							
							country=country+"|"+temp_name
					#print Director_name
						else:
							temp_name=(link.text).encode('ascii','ignore')
							country=country+"|"+temp_name
			if "Budget:" in temp:
				soup_temp3=BeautifulSoup(temp)
				for link in soup_temp3:
					#print link
					try:
						dd=link+"1"
					except:
						if type(link.text) == str:
							temp_name=value(link.text,"utf-8",errors="ignore")
							
							Budget=Budget+"|"+temp_name
					#print Director_name
						else:
							temp_name=(link.text).encode('ascii','ignore')
							Budget=Budget+"|"+temp_name
							
		print Budget
				
		print country
		final_String=[title,year,rating,country,Director_name,Budget,gross,votes,duration]
		#final_String[0]=title
		#final_String[1]=year
		#final_String[2]=rating
		#final_String[3]=country
		#final_String[4]=Director_name
		#final_String[5]=Budget
		#final_String[6]=gross
		#final_String[7]=votes
		#final_String[8]=duration
		dic={}
		dic['title']=title
		dic['year']=year
		dic['rating']=rating
		dic['country']=country
		dic['director_name']=Director_name
		dic['budget']=Budget
		dic['gross']=gross
		dic['votes']=votes
		dic['duration']=duration
		dic['stars']=Star_name
		dic['genre']="Comedy"
		#print dic
		EX.array_final.append(dic)
		
		
		
		#print final_String
		#exit();
		#wr.writerow(final_String)
print "test"

with open('data_comedy.json', 'w') as outfile:
    json.dump(EX.array_final, outfile)		
	
	
		
	
	
	
	#print title
#char1 = '"'
#char2 = '"'
#print temp.find_all('a',href=True)

#for links in temp:
#	link=links.findAll('a')
#	span=links.findAll('span')
#	span_string=str(span[1])
#	asd=str(link[0])
#	#print "Dude"
	#print span_string
#	y_a=find(span_string,"(")
#	y_b=find(span_string,")")
#	if span_string[y_a[0]+1:y_b[0]]=='I':
#		year=span_string[y_a[1]+1:y_b[1]]
#	else:
#		year=span_string[y_a[0]+1:y_b[0]]
	#print year
		
	
#	a=find(asd,"\"")
	#print asd
	#a=asd.find("\"")
	#b=asd.find("\"")
#	fs=asd[a[0]+1:a[1]]
#	fss=str("http://www.imdb.com"+fs)
	#print fss
#	b=find(asd,">")
	#print b
#	c=find(asd,"<")
	#print c
#	title=asd[b[0]+1:c[1]]
	#print(fs1)
#	rating_tag=links.findAll('strong')
	#print rating_tag
	#page2= urllib2.urlopen(fss)
	#soup2 = BeautifulSoup(page2)
	#print soup2
	#print links
#	break
	

#temp2= soup.findAll("div",{"class":"lister-item-content"})
#print temp2
#for i in temp2:
	
	
'''
	if 'RND' in tr.contents[0].contents[0]:
		postSeason = 1
		regularSeason = 0
	elif 'WK' in tr.contents[0].contents[0]:
		if regularSeason == 0:
			postSeason = 0
			regularSeason = 1
		elif regularSeason == 1:
			postSeason = 0
			regularSeason = 0
	else:
		if "Schedule" not in tr.contents[0].contents[0]:
			if postSeason == 1 and regularSeason == 0:
				if len(tr('td')) != 2:
					element = tr('td')
					#print element
					row={}
					row["RND"] = element[0].contents[0]
					row["Date"] = element[1].contents[0]
					row["Opponent"] = {}
					#print element[2].contents[0]('li')[0].contents[0]
					ground = element[2].contents[0]('li')[0].contents[0]
					opponent_team = BeautifulSoup(str(element[2].contents[0]('li')[-1].contents)).findAll('a')[0].contents[0]
					if ground == "vs":
						row["Opponent"]["Ground"] = "Home"
					else:
						row["Opponent"]["Ground"] = "Away"
					row["Opponent"]["Team"] = opponent_team
					row["Result"]={}
					winorlose = element[3].contents[0]('li')[0].contents[0].contents[0]
					#print winorlose
					score = BeautifulSoup(str(element[3].contents[0]('li')[-1].contents)).findAll('a')[0].contents[0]
					row["Result"]["WinOrLose"] = winorlose
					row["Result"]["Score"] = score
					####href for next page
					row["Passing"] = {}
					row["Rushing"] = {}
					row["Receiving"] = {}
					passing_player="NA"
					passing_yards="NA"
					rushing_player="NA"
					rushing_yards="NA"
					receiving_player="NA"
					receiving_yards="NA"
					try:
						passing_player = BeautifulSoup(str(element[4].contents[0])).findAll('a')[0].contents[0]
						passing_yards = element[4].contents[1]
					except:
						continue


					try:
						rushing_player = BeautifulSoup(str(element[5].contents[0])).findAll('a')[0].contents[0]
						rushing_yards = element[5].contents[1]
					except:
						continue

					try:
						receiving_player = BeautifulSoup(str(element[6].contents[0])).findAll('a')[0].contents[0]
						receiving_yards = element[6].contents[1]	
					except:
						continue

					row["Passing"]["Player"] = passing_player
					row["Passing"]["Yards"] = passing_yards

					
					row["Rushing"]["Player"] = rushing_player
					row["Rushing"]["Yards"] = rushing_yards

					
					row["Receiving"]["Player"] = receiving_player
					row["Receiving"]["Yards"] = receiving_yards
					json[team][year]["Post_Season"].append(row)
					#print rushing_player,rushing_yards,receiving_player,receiving_yards

				#print "________________"
			elif regularSeason == 1 and postSeason == 0:
				#print tr.contents
				#print len(tr('td'))
				if len(tr('td')) != 2:
					
					element = tr('td')
					print element
					row={}
					row["WK"] = element[0].contents[0]
					row["Date"] = element[1].contents[0]
					row["Opponent"] = {}
					#print element[2].contents[0]('li')[0].contents[0]
					ground = element[2].contents[0]('li')[0].contents[0]
					opponent_team = BeautifulSoup(str(element[2].contents[0]('li')[-1].contents)).findAll('a')[0].contents[0]
					if ground == "vs":
						row["Opponent"]["Ground"] = "Home"
					else:
						row["Opponent"]["Ground"] = "Away"
					row["Opponent"]["Team"] = opponent_team
					row["Result"]={}
					winorlose = element[3].contents[0]('li')[0].contents[0].contents[0]
					#print winorlose
					score = BeautifulSoup(str(element[3].contents[0]('li')[-1].contents)).findAll('a')[0].contents[0]
					row["Result"]["WinOrLose"] = winorlose
					row["Result"]["Score"] = score
					####href for next page
					row["Passing"] = {}
					row["Rushing"] = {}
					row["Receiving"] = {}
					passing_player="NA"
					passing_yards="NA"
					rushing_player="NA"
					rushing_yards="NA"
					receiving_player="NA"
					receiving_yards="NA"
					try:
						passing_player = BeautifulSoup(str(element[4].contents[0])).findAll('a')[0].contents[0]
						passing_yards = element[4].contents[1]
					except:
						continue


					try:
						rushing_player = BeautifulSoup(str(element[5].contents[0])).findAll('a')[0].contents[0]
						rushing_yards = element[5].contents[1]
					except:
						continue

					try:
						receiving_player = BeautifulSoup(str(element[6].contents[0])).findAll('a')[0].contents[0]
						receiving_yards = element[6].contents[1]	
					except:
						continue

					row["Passing"]["Player"] = passing_player
					row["Passing"]["Yards"] = passing_yards

					
					row["Rushing"]["Player"] = rushing_player
					row["Rushing"]["Yards"] = rushing_yards

					
					row["Receiving"]["Player"] = receiving_player
					row["Receiving"]["Yards"] = receiving_yards
					json[team][year]["Regular_Season"].append(row)





print json

'''






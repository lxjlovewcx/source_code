vuser_end()
{

	lr_think_time(4);

	web_url("welcome.pl_3", 
		"URL=http://127.0.0.1:1080/WebTours/welcome.pl?signOff=1", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?page=menu&in=itinerary", 
		"Snapshot=t184.inf", 
		"Mode=HTML", 
		LAST);

	return 0;
}
Action()
{

	lr_think_time(5);

	lr_rendezvous("打开登录主页集合点");

	lr_start_transaction("打开登录主页事务");

	web_url("welcome.pl", 
		"URL=http://127.0.0.1:1080/WebTours/welcome.pl?page=search", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?page=menu&in=home", 
		"Snapshot=t178.inf", 
		"Mode=HTML", 
		LAST);

	lr_end_transaction("打开登录主页事务", LR_AUTO);



	lr_think_time(4);
/*
	web_submit_data("reservations.pl", 
		"Action=http://127.0.0.1:1080/WebTours/reservations.pl", 
		"Method=POST", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/reservations.pl?page=welcome", 
		"Snapshot=t180.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=advanceDiscount", "Value=0", ENDITEM, 
		"Name=depart", "Value=London", ENDITEM, 
		"Name=departDate", "Value=10/22/2016", ENDITEM, 
		"Name=arrive", "Value=Paris", ENDITEM, 
		"Name=returnDate", "Value=10/23/2016", ENDITEM, 
		"Name=numPassengers", "Value=1", ENDITEM, 
		"Name=seatPref", "Value=Aisle", ENDITEM, 
		"Name=seatType", "Value=Business", ENDITEM, 
		"Name=.cgifields", "Value=roundtrip", ENDITEM, 
		"Name=.cgifields", "Value=seatType", ENDITEM, 
		"Name=.cgifields", "Value=seatPref", ENDITEM, 
		"Name=findFlights.x", "Value=45", ENDITEM, 
		"Name=findFlights.y", "Value=15", ENDITEM, 
		LAST);

	web_submit_form("reservations.pl_2", 
		"Snapshot=t181.inf", 
		ITEMDATA, 
		"Name=outboundFlight", "Value=242;149;10/22/2016", ENDITEM, 
		"Name=reserveFlights.x", "Value=20", ENDITEM, 
		"Name=reserveFlights.y", "Value=4", ENDITEM, 
		LAST);

	lr_think_time(6);

	web_submit_form("reservations.pl_3", 
		"Snapshot=t182.inf", 
		ITEMDATA, 
		"Name=firstName", "Value=Joseph", ENDITEM, 
		"Name=lastName", "Value=Marshall", ENDITEM, 
		"Name=address1", "Value=234 Willow Drive", ENDITEM, 
		"Name=address2", "Value=San Jose/CA/94085", ENDITEM, 
		"Name=pass1", "Value=Joseph Marshall", ENDITEM, 
		"Name=creditCard", "Value=0123456789", ENDITEM, 
		"Name=expDate", "Value=", ENDITEM, 
		"Name=saveCC", "Value=<OFF>", ENDITEM, 
		"Name=buyFlights.x", "Value=37", ENDITEM, 
		"Name=buyFlights.y", "Value=9", ENDITEM, 
		LAST);

	web_url("welcome.pl_2", 
		"URL=http://127.0.0.1:1080/WebTours/welcome.pl?page=itinerary", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?page=menu&in=flights", 
		"Snapshot=t183.inf", 
		"Mode=HTML", 
		LAST);
*/
	return 0;
}

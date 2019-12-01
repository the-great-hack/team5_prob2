# team5_prob2

Multi-mode transportation will be preferred to reach from point A to point D using different transport modes and with stops in between.

# Considerations: 

To make the trip cost-effective and less hectic by having minimal transport switches

# Assumptions:
* Careem Bus will have restricted timetables and routes. All vehicles will be available in unlimited amount.
* There will be enough captain-supply availability and constant fares estimation. Hence, project demo will be user-centric.
* Data is designed and generated by us for User, Driver, Vehicle, Location.
* Latitude and longitude obtained from user for pickup and destination are being hardcoded to a location based grid.
* To formulate accurate optimal solution, user is asked two below queries before booking: 
	* Total number of passengers and Preference among cost or time.
* In any grid field,<br />
	5 = All vehicles (Bike, Rickshaw, Go, Go Mini, Bus)<br />
	4 = All vehicles except bus<br />
	2 = Bike and rickshaw<br />
	1 = Only bike<br />
	NULL = Vehicle is not allowed to travel on this route

![alt text](https://github.com/the-great-hack/team5_prob2/blob/master/image-2.png "")

# Technology Stack:
	* Back-end: Python
	* Front-end: iOS App
	* Continuous Development: GitHub

# Future Prospects:
* Carpooling for people coming from same areas and on same time. This would be quite useful for students/ office colleagues etc. 
* Cost effective trips to other cities e.g., using Careem bus from Lahore to Islamabad and then Go from Islamabad to Shakarparian
* Suggestion of alternate routes in case of traffic jam or peak factor
* Once this feature will get functional in Careem, suggested routes will get further optimized because of actual test data.
* User can be asked his/her specific budget constraints. E.g., Trip under PKR 500
* User can suggest feature to 5 friends and get incentives/ bonus
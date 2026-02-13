# Ex03 Places Around Me
## Date: 12-02-2026

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE

### WelcomeHomeOdisha.html
```html
{% load static %}

<html>
<head>
<title>Places Around Me</title>
</head>

<body>

<h1 align="center"><font color="purple">Places Around My House</font></h1>

<center>
    <img src="{% static 'images/orissa-tourist-map.jpg' %}" usemap="#OdishaMap">
</center>



<map name="OdishaMap">
    <area shape="circle" coords="426,315,8" href="/JagannathPuri/">
    <area shape="circle" coords="387,327,15" href="/ChilikaLake/">
    <area shape="circle" coords="480,300,15" href="/KonarkSunTemple/">
    <area shape="circle" coords="472,119,19" href="/SimilipalNationalPark/">
    <area shape="circle" coords="299,155,14" href="/UshaKothiWildlifeSanctuary/">   
</map>

</body>
</html>
```

### UshaKothiWildlifeSanctuary.html
```html
{% load static %}

<html>
<head>
    <title>Ushakothi Wildlife Sanctuary</title>
</head>
<body>
<br>
<h1 align="center"><font color="brown">Ushakothi Wildlife Sanctuary</font></h1>

<center><img src="{% static 'images/UshaKothiWildlifeSanctuary.jpg' %}" width="500"></center> <br><br><br>
<p><font face="Comic Sans MS" size="4" color="blue"><b>Ushakothi Wildlife Sanctuary, also known as Badrama Wildlife Sanctuary, is located in the Sambalpur district of Odisha. It was established in 1962.</b></font></p>
</p>

<p><font face="Comic Sans MS" size="4" color="blue"><b>
The sanctuary consists mainly of dry deciduous forests
with trees like sal and neem.
It is home to elephants, leopards, sambar deer and bison.</b></font></p>

<p><font face="Comic Sans MS" size="4" color="blue"><b>
It is an important protected area for wildlife conservation
and attracts nature lovers and wildlife enthusiasts.</b></font></p>

<a href="/">⬅ Back to Map</a>

</body>
</html>
```

### SimilipalNationalPark.html
```html
{% load static %}

<html>
<head>
    <title>Similipal National Park</title>
</head>
<body>
<br><br>
<h1 align="center"><font color="darkgreen">Similipal National Park</font></h1>

<center>
<img src="{% static 'images/SimilipalNationalPark.jpg' %}" ><br><br><br>
</center>
<br><br>
<p><font face="Verdana" size="4" color="orange"><b>Similipal National Park is located in the Mayurbhanj district of Odisha. It is a tiger reserve and also a UNESCO Biosphere Reserve.</b></font></p>

<p><font face="Verdana" size="4" color="orange"><b>It covers an area of about 2750 square kilometers and is part of the Similipal Biosphere Reserve. The park is home to Bengal tigers, elephants, leopards,
gaur, deer and many bird species.
It has dense forests and rich biodiversity.</b>
</font></p>

<p><font face="Verdana" size="4" color="orange"><b>
Popular attractions inside the park include Barehipani Falls
and Joranda Falls, which are among the highest waterfalls in India.</b>
</font></p>

<a href="/">⬅ Back to Map</a>

</body>
</html>
```
### KonarkSunTemple.html
```html
{% load static %}

<html>
<head>
    <title>Konark Sun Temple</title>
</head>
<body>
<br><br>
<h1 align="center"><font color="darkyellow">Konark Sun Temple</font></h1>
<center>
<img src="{% static 'images/KonarkSunTemple.jpg' %}" ><br><br><br>
</center>
<br><br>
<p><font face="Trebuchet MS" size="4" color="blue"><b>The Konark Sun Temple is a UNESCO World Heritage Site located in Odisha. It was built in the 13th century by King Narasimhadeva I.</b></font></p> 

<p><font face="Trebuchet MS" size="4" color="blue"><b>The temple is designed in the shape of a gigantic chariot
with 24 beautifully carved stone wheels and seven horses.   It is dedicated to Surya, the Sun God.</b></font></p>   


<p><font face="Trebuchet MS" size="4" color="blue"><b>The temple is an outstanding example of Kalinga architecture
and is famous for its detailed stone carvings. The Konark Dance Festival is held here every year.</b></font></p>

<a href="/">⬅ Back to Map</a>

</body>
</html>

```
### JagannathPuri.html
```html
{% load static %}

<html>
<head>
    <title>Jagannath Puri</title>
</head>
<body>

<h1 align="center"><font color="magenta">Jagannath Temple, Puri</font></h1>
<br><br>
<center>
<img src="{% static 'images/JagannathPuri.jpg' %}"><br><br><br>
</center>
<br><br>
<p><font face="Arial" size="4" color="purple"><b>The Jagannath Temple is a famous Hindu temple located in Puri, Odisha. It was built in the 12th century by King Anantavarman Chodaganga Deva. The temple is dedicated to Lord Jagannath, a form of Lord Vishnu.</b></font></p>    


<p><font face="Arial" size="4" color="purple"><b>It is one of the four sacred Char Dham pilgrimage sites in India.
The temple is especially famous for the annual Ratha Yatra (Chariot Festival),
during which the deities Jagannath, Balabhadra and Subhadra are taken out
in grand chariots.</b></font></p>       

<p><font face="Arial" size="4" color="purple"><b>The temple is constructed in Kalinga architectural style and attracts
millions of devotees and tourists every year.</b></font></p>

<a href="/">⬅ Back to Map</a>

</body>
</html>

```
### ChilikaLake.html
```html
{% load static %}

<html>
<head>
    <title>Chilika Lake</title>
</head>
<body>
<br><br>
<h1 align="center"><font color="olive">Chilika Lake</font></h1>
<br><br>
<center>
<img src="{% static 'images/ChilikaLake.jpg' %}"><br><br><br>
</center>

<p><font face="Courier New" size="4" color="magenta"><b>
Chilika Lake is the largest brackish water lagoon in Asia,
located in Odisha, India.
It spreads across the districts of Puri, Khurda, and Ganjam.
</b></font></p>

<p><font face="Courier New" size="4" color="magenta"><b>
The lake is famous for being one of the largest wintering grounds
for migratory birds in the world.
Thousands of birds from Siberia and other cold regions visit Chilika every year.
</b></font></p>

<p><font face="Courier New" size="4" color="magenta"><b>
It is also known for the rare Irrawaddy dolphins found near Satapada.
Boating and bird watching are popular tourist activities here.
</b></font></p>

<a href="/">⬅ Back to Map</a>

</body>
</html>

```
## OUTPUT

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205208.png"

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205308.png"

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205333.png"

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205351.png"

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205408.png"

"C:\Users\Trisha Priyadarshni\Pictures\Screenshots\Screenshot 2026-02-13 205428.png"


## RESULT
The program for implementing image maps using HTML is executed successfully.

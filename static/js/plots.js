
$("#btnregsubmit").click(function(){
	debugger;
	
	var name=document.getElementById('name').value;
	var pswd=document.getElementById('pswd').value;
	var email=document.getElementById('email').value;
	var phone=document.getElementById('phone').value;
	var addr=document.getElementById('addr').value;
	var age=document.getElementById('age').value;
	
	  if ( document.getElementById('name').value =='' &&
	            document.getElementById('pswd').value =='' && document.getElementById('email').value =='' &&
                 document.getElementById('phone').value =='' && document.getElementById('addr').value =='' && document.getElementById('age').value =='')
	        {
	            alert('Please Fill All Fields');
	        }
       var flag = true;

	       

	        var namer = document.getElementById('name').value;
	        var intRegexnamer = /^[A-Za-z ]+$/;
	        if (!intRegexnamer.test(namer)) {
	            alert('Please enter a  name.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
	        var email = document.getElementById('email').value;
	        var emailReg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	        if (!emailReg.test(email) || email == '') {
	            alert('Please enter a valid email id.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }


	        var phone = document.getElementById('phone').value;
	        var intRegex = /^(7|8|9)[0-9]{9}$/;
	        if (!intRegex.test(phone)) {
	            alert('Please enter a valid phone number.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }

			var age = document.getElementById('age').value;
			var intRegexAge = /^[0-9]+$/;
			if (!intRegexAge.test(age)) {
				alert('Please enter a valid age.');
				flag = false;
				return flag;
			} else {
				flag = true;
			}
			
	        //return flag;
	      //  return flag;
	    //}
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
	$.ajax({
            type: 'GET',
            url: '/regdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'name': name,
            'email': email,
            'phone': phone,
            'pswd': pswd,
            'addr': addr,
			'age': age
			

        },
            
        dataType:"json",
            success: function(data) {
				alert('Data saved Successfully');
				acheck();
               window.location='login';
            },
        });
	
});


$("#btnbookapp").click(function(){
	debugger;
	
	var name=document.getElementById('name').value;
	var date=document.getElementById('date').value;
	var car=document.getElementById('car').value;
	var prob=document.getElementById('prob').value;
	var time=document.getElementById('time').value;
	
	  if ( document.getElementById('name').value =='' &&
	            document.getElementById('date').value =='' && document.getElementById('car').value =='' &&
                 document.getElementById('prob').value =='')
	        {
	            alert('Please Fill All Fields');
	        }
      

	       
	
	$.ajax({
            type: 'GET',
            url: '/appdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'name': name,
            'date': date,
            'car': car,
            'prob': prob,
			'time':time
			

        },
            
        dataType:"json",
            success: function(data) {
				alert('Appointment booked Successfully');
				acheck();
               window.location='myapppat';
            },
        });
	
});


$("#btnpredict").click(function(){
	debugger;
	var loc=document.getElementById('loc').value;
	
	
	window.location='/locdata?loc='+loc;
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
/*	$.ajax({
            type: 'GET',
            url: '/locdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'loc': loc	

        },
            
        dataType:"json",
            success: function(data) {
				alert('Data saved Successfully');
				acheck();
              // window.location='register';
            },
        });*/
	
});


$("#btnlogsubmit").click(function(){
	debugger;
	var email=document.getElementById('email').value;
	var pswd=document.getElementById('pswd').value;
	 if (document.getElementById('email').value =='' && document.getElementById('pswd').value =='')
	        {
	            alert('Please Enter email and password');
	        }
	
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
	$.ajax({
            type: 'GET',
            url: '/logdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'email': email,
            'pswd': pswd
			

        },
            
        dataType:"json",
            success: function(data) {
				if(data=="Failure")
				{
					alert("Credentials not found");
					window.location='register';
				}
				if(data=="Success")
				{
					//alert('Logged in Successfully');
				   window.location='chatbox';
				}
            },
			 error: function(data) {
               
            }
        });
	
});




$("#btndregsubmit").click(function(){
	debugger;
	
	var name=document.getElementById('name').value;
	var pswd=document.getElementById('pswd').value;
	var email=document.getElementById('email').value;
	var phone=document.getElementById('phone').value;
	var darea=document.getElementById('darea').value;
	var dtype=document.getElementById('dtype').value;
	var location=document.getElementById('location').value;
	
	  if ( document.getElementById('name').value =='' &&
	            document.getElementById('pswd').value =='' && document.getElementById('email').value =='' &&
                 document.getElementById('phone').value =='' && document.getElementById('darea').value =='')
	        {
	            alert('Please Fill All Fields');
	        }
       var flag = true;

	       

	        var namer = document.getElementById('name').value;
	        var intRegexnamer = /^[A-Za-z ]+$/;
	        if (!intRegexnamer.test(namer)) {
	            alert('Please enter a  name.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
	        var email = document.getElementById('email').value;
	        var emailReg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	        if (!emailReg.test(email) || email == '') {
	            alert('Please enter a valid email id.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }


	        var phone = document.getElementById('phone').value;
	        var intRegex = /^(7|8|9)[0-9]{9}$/;
	        if (!intRegex.test(phone)) {
	            alert('Please enter a valid phone number.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }

	$.ajax({
            type: 'GET',
            url: '/regddata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'name': name,
            'email': email,
            'phone': phone,
            'pswd': pswd,
            'darea': darea,
            'dtype': dtype,
			'location': location
		        },
            
        dataType:"json",
            success: function(data) {
				alert('Data saved Successfully');
               window.location='showroomreg';
            },
        });
	
});




$("#btndlogsubmit").click(function(){
	debugger;
	var email=document.getElementById('email').value;
	var pswd=document.getElementById('pswd').value;
	 if (document.getElementById('email').value =='' && document.getElementById('pswd').value =='')
	        {
	            alert('Please Enter email and password');
	        }
	
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
	$.ajax({
            type: 'GET',
            url: '/logddata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'email': email,
            'pswd': pswd
			

        },
            
        dataType:"json",
            success: function(data) {
				if(data=="Failure")
				{
					alert("Credentials not found");
					window.location='doctorreg';
				}
				if(data=="Success")
				{
					//alert('Logged in Successfully');
				   window.location='myapp';
				}
            },
			 error: function(data) {
               
            }
        });
	
});































function acheck()
{
	debugger;
}

$("#chat_btnsubmit").click(function(){
	debugger;
			var val=document.getElementById('eq').value;
						var response="";
						var dt=document.getElementById('data');
						dt.innerHTML+="User : "+val+"<br/>";
						if(val.toLowerCase()=="hi")
						response="Hello";
						if(val.toLowerCase()=="how are you")
						response="I am good. How about you";
						if(val.toLowerCase()=="what is your name")
						response="I am your Mob-Bot.";
						if(val.toLowerCase()=="goodbye")
						response="See you later";
						if(val.toLowerCase()=="transaction")
						response="Your transaction history is";
						if(val.toLowerCase()=="transfer")
						response="transfer complete";
						if(val.toLowerCase()=="statements")
						response="Your statements are";
						if(val.toLowerCase()=="help")
						response="How can i help you";
						if(val.toLowerCase()=="card")
						response="ATM card";
					
						if(val.toLowerCase().includes("nearest"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "block";
							document.getElementById("faq").style.display = "none";
							document.getElementById("fd").style.display = "none";
						}
						
						if(val.toLowerCase().includes("faq") || val.toLowerCase().includes("frequently asked question"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "none";
							document.getElementById("faq").style.display = "block";
							document.getElementById("fd").style.display = "none";
						}
						
						if(val.toLowerCase().includes("fd") || val.toLowerCase().includes("fixed deposit") || val.toLowerCase().includes("deposit") || val.toLowerCase().includes("interest"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "none";
							document.getElementById("faq").style.display = "none";
							document.getElementById("fd").style.display = "block";
						}
						if(val.toLowerCase()=="cancel")
						response="Process canceled"
						dt.innerHTML+="Bot : "+response+"<br/>";
	});
	
	
	
	
$( "#eq" ).change(function() {
 var val=document.getElementById('eq').value;
						var response="";
						var dt=document.getElementById('data');
						dt.innerHTML+="User : "+val+"<br/>";
						if(val.toLowerCase()=="hi")
						response="Hello";
						if(val.toLowerCase()=="how are you")
						response="I am good. How about you";
						if(val.toLowerCase()=="what is your name")
						response="I am your Mob-Bot.";
						if(val.toLowerCase()=="goodbye")
						response="See you later";
						if(val.toLowerCase()=="transaction")
						response="Your transaction history is";
						if(val.toLowerCase()=="transfer")
						response="transfer complete";
						if(val.toLowerCase()=="statements")
						response="Your statements are";
						if(val.toLowerCase()=="help")
						response="How can i help you";
						if(val.toLowerCase()=="card")
						response="ATM card";
					
						if(val.toLowerCase().includes("nearest"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "block";
							document.getElementById("faq").style.display = "none";
							document.getElementById("fd").style.display = "none";
						}
						
						if(val.toLowerCase().includes("faq") || val.toLowerCase().includes("frequently asked question"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "none";
							document.getElementById("faq").style.display = "block";
							document.getElementById("fd").style.display = "none";
						}
						
						if(val.toLowerCase().includes("fd") || val.toLowerCase().includes("fixed deposit") || val.toLowerCase().includes("deposit") || val.toLowerCase().includes("interest"))
						{
							response="Please click on the below link";
							document.getElementById("bank").style.display = "none";
							document.getElementById("faq").style.display = "none";
							document.getElementById("fd").style.display = "block";
						}
						if(val.toLowerCase()=="cancel")
						response="Process canceled"
						dt.innerHTML+="Bot : "+response+"<br/>";
});	

	
	
	
	
	
	
$("#dataload_btnsubmit").click(function(){
	debugger;
   var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Data stored successfully');
            },
        });
});

$("#dataload_btnclear").click(function(){
   var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/cleardataset',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Dataset has been cleared');
            },
        });
});
